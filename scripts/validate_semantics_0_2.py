#!/usr/bin/env python3
"""DUSRM 0.2-draft semantic consistency validator.

Validates typed references and selected cross-record consistency rules after
JSON Schema validation. It is not a conformance, safety, security, or
implementation-verification tool.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schema" / "dusrm-description-0.2.schema.json"
DEFAULT_REGISTRY = ROOT / "profiles" / "registry.json"

COLLECTIONS = {
    "element": "elements",
    "responsibility": "responsibilities",
    "property": "properties",
    "specification": "specifications",
    "operation": "operations",
    "execution": "executions",
    "event": "events",
    "stateVariable": "stateVariables",
    "state": "states",
    "transition": "transitions",
    "interface": "interfaces",
    "interaction": "interactions",
    "resource": "resources",
    "allocation": "allocations",
    "capability": "capabilities",
    "service": "services",
    "requirement": "requirements",
    "constraint": "constraints",
    "invariant": "invariants",
    "assertion": "assertions",
    "decision": "decisions",
    "evidence": "evidence",
}
PARTICIPANT_KINDS = {"system", "element", "environmentParticipant"}
CORE_LAYERS = {f"L{i}" for i in range(1, 9)}

RELATIONSHIP_SIGNATURES = {
    "memberOf": ({"element"}, {"system", "element"}),
    "decomposesInto": ({"system", "element"}, {"element"}),
    "containedWithin": ({"element"}, {"element", "boundary"}),
    "dependsOn": (PARTICIPANT_KINDS, PARTICIPANT_KINDS),
    "exposes": (PARTICIPANT_KINDS, {"interface"}),
    "requires": (PARTICIPANT_KINDS, {"interface", "capability", "resource"}),
    "interactsWith": (PARTICIPANT_KINDS, PARTICIPANT_KINDS),
    "allocates": (PARTICIPANT_KINDS, {"resource"}),
    "performs": ({"execution"}, {"operation"}),
    "triggers": ({"event"}, {"transition", "operation"}),
    "transitionsTo": ({"state"}, {"state"}),
    "observes": (PARTICIPANT_KINDS, {"element", "event", "property", "state"}),
    "controls": (PARTICIPANT_KINDS, {"element", "operation", "execution"}),
    "constrainedBy": ({"element", "operation", "execution"}, {"constraint"}),
    "satisfies": ({"element", "responsibility", "operation", "capability", "service"}, {"requirement"}),
    "derivedFrom": ({"requirement", "decision", "assertion"}, {"evidence", "requirement", "decision", "assertion"}),
    "implements": ({"element"}, {"specification"}),
}

REALIZATION_RANK = {
    "notStarted": 0,
    "planned": 1,
    "inProgress": 2,
    "implemented": 3,
    "retired": 4,
}


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    path: str
    message: str


def _list(document: dict[str, Any], key: str) -> list[dict[str, Any]]:
    value = document.get(key, [])
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _same_ref(left: Any, right: Any) -> bool:
    return (
        isinstance(left, dict)
        and isinstance(right, dict)
        and left.get("kind") == right.get("kind")
        and left.get("id") == right.get("id")
    )


def validate_semantics(
    document: dict[str, Any],
    registry: dict[str, Any] | None = None,
) -> list[Finding]:
    """Return deterministic semantic findings for a schema-shaped 0.2 description."""
    findings: list[Finding] = []

    def add(code: str, severity: str, path: str, message: str) -> None:
        findings.append(Finding(code, severity, path, message))

    if not isinstance(document, dict):
        return [Finding("DUSRM-02-M-000", "error", "$", "Description root must be an object.")]

    context = document.get("context") or {}
    soi = context.get("systemOfInterest") or {}
    boundary = context.get("boundary") or {}
    environment = context.get("environment", [])
    if not isinstance(environment, list):
        environment = []

    records: dict[str, dict[str, dict[str, Any]]] = {
        "system": {},
        "boundary": {},
        "environmentParticipant": {},
    }
    records["system"][soi.get("id")] = soi if isinstance(soi.get("id"), str) else {}
    records["boundary"][boundary.get("id")] = boundary if isinstance(boundary.get("id"), str) else {}
    for item in environment:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            records["environmentParticipant"][item["id"]] = item
    for kind, collection in COLLECTIONS.items():
        records[kind] = {
            item["id"]: item
            for item in _list(document, collection)
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }

    # M-001: IDs are globally unique across every object namespace in one description.
    seen_ids: dict[str, str] = {}
    object_groups: list[tuple[str, list[dict[str, Any]]]] = [
        ("system", [soi] if soi else []),
        ("boundary", [boundary] if boundary else []),
        ("environmentParticipant", environment),
    ]
    object_groups.extend((collection, _list(document, collection)) for collection in COLLECTIONS.values())
    for group, items in object_groups:
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            identifier = item.get("id")
            if not isinstance(identifier, str):
                continue
            location = f"{group}[{index}].id"
            if identifier in seen_ids:
                add(
                    "DUSRM-02-M-001", "error", location,
                    f"Identifier '{identifier}' is duplicated; first declared at {seen_ids[identifier]}.",
                )
            else:
                seen_ids[identifier] = location

    def resolve_ref(ref: Any, path: str, allowed: set[str] | None = None) -> dict[str, Any] | None:
        if not isinstance(ref, dict):
            add("DUSRM-02-M-002", "error", path, "Typed reference must be an object.")
            return None
        kind, identifier = ref.get("kind"), ref.get("id")
        if not isinstance(kind, str) or not isinstance(identifier, str):
            add("DUSRM-02-M-002", "error", path, "Typed reference must contain string kind and id fields.")
            return None
        if allowed is not None and kind not in allowed:
            add(
                "DUSRM-02-M-003", "error", f"{path}.kind",
                f"Reference kind '{kind}' is not permitted here; expected one of {sorted(allowed)}.",
            )
            return None
        group = records.get(kind)
        if group is None:
            add("DUSRM-02-M-003", "error", f"{path}.kind", f"Unknown reference kind '{kind}'.")
            return None
        target = group.get(identifier)
        if target is None:
            add(
                "DUSRM-02-M-002", "error", f"{path}.id",
                f"Reference '{kind}:{identifier}' does not resolve to a declared object.",
            )
        return target

    def check_participant(ref: Any, path: str) -> dict[str, Any] | None:
        return resolve_ref(ref, path, PARTICIPANT_KINDS)

    def check_evidence_refs(record: dict[str, Any], path: str) -> None:
        refs = record.get("evidenceRefs", [])
        if refs is None:
            return
        if not isinstance(refs, list):
            add("DUSRM-02-M-010", "error", f"{path}.evidenceRefs", "evidenceRefs must be an array.")
            return
        for index, identifier in enumerate(refs):
            if not isinstance(identifier, str) or identifier not in records["evidence"]:
                add(
                    "DUSRM-02-M-010", "error", f"{path}.evidenceRefs[{index}]",
                    f"Evidence reference '{identifier}' does not resolve.",
                )

    # Validate evidence references on the SOI and environment as well as collection records.
    check_evidence_refs(soi, "context.systemOfInterest")
    for i, item in enumerate(environment):
        if isinstance(item, dict):
            check_evidence_refs(item, f"context.environment[{i}]")

    # Check all typed references at their declared locations.
    for collection, items in ((name, _list(document, name)) for name in COLLECTIONS.values()):
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            path = f"{collection}[{index}]"
            check_evidence_refs(item, path)

    for i, item in enumerate(_list(document, "responsibilities")):
        parent = item.get("parentResponsibilityRef")
        if parent is not None:
            target = records["responsibility"].get(parent)
            if target is None:
                add("DUSRM-02-M-002", "error", f"responsibilities[{i}].parentResponsibilityRef",
                    f"Parent responsibility '{parent}' does not resolve.")
            if parent == item.get("id"):
                add("DUSRM-02-M-021", "error", f"responsibilities[{i}].parentResponsibilityRef",
                    "A responsibility cannot be its own parent.")

    def check_typed_field(record: dict[str, Any], field: str, path: str,
                          allowed: set[str] | None = None) -> dict[str, Any] | None:
        if field not in record:
            return None
        return resolve_ref(record[field], f"{path}.{field}", allowed)

    def check_participant_field(record: dict[str, Any], field: str, path: str) -> dict[str, Any] | None:
        if field not in record:
            return None
        return check_participant(record[field], f"{path}.{field}")

    # Element -> Responsibility realization and allocation consistency.
    realization_pairs: set[tuple[str, str]] = set()
    realization_counts: dict[str, int] = {}
    for i, item in enumerate(_list(document, "realizations")):
        path = f"realizations[{i}]"
        element_id = item.get("elementRef")
        responsibility_id = item.get("responsibilityRef")
        element = records["element"].get(element_id)
        responsibility = records["responsibility"].get(responsibility_id)
        if element is None:
            add("DUSRM-02-M-002", "error", f"{path}.elementRef",
                f"Element reference '{element_id}' does not resolve.")
        if responsibility is None:
            add("DUSRM-02-M-002", "error", f"{path}.responsibilityRef",
                f"Responsibility reference '{responsibility_id}' does not resolve.")
        if isinstance(element_id, str) and isinstance(responsibility_id, str):
            pair = (element_id, responsibility_id)
            if pair in realization_pairs:
                add("DUSRM-02-M-012", "error", path, "Duplicate element-to-responsibility realization pair.")
            realization_pairs.add(pair)
            realization_counts[responsibility_id] = realization_counts.get(responsibility_id, 0) + 1
        state = item.get("realizationState")
        if element and state == "implemented" and element.get("realizationState") != "implemented":
            add("DUSRM-02-E-001", "error", f"{path}.realizationState",
                "A realization cannot be marked implemented when its realizing element is not implemented.")

    for i, item in enumerate(_list(document, "responsibilities")):
        identifier = item.get("id")
        state = item.get("realizationState")
        if identifier and realization_counts.get(identifier, 0) == 0 and state in {"inProgress", "implemented"}:
            add("DUSRM-02-M-013", "warning", f"responsibilities[{i}]",
                "Responsibility is marked in progress or implemented but has no realizing element; record an architecture gap or revise its state.")

    # Responsibility parent hierarchy must be acyclic.
    parent_of = {
        item.get("id"): item.get("parentResponsibilityRef")
        for item in _list(document, "responsibilities")
        if isinstance(item.get("id"), str) and isinstance(item.get("parentResponsibilityRef"), str)
    }
    for identifier in parent_of:
        trail: set[str] = set()
        current = identifier
        while current in parent_of:
            if current in trail:
                add("DUSRM-02-M-021", "error", "responsibilities",
                    f"Responsibility parent hierarchy contains a cycle involving '{current}'.")
                break
            trail.add(current)
            current = parent_of[current]

    # Layer applicability: one declaration per layer; a notApplicable layer cannot own a core responsibility.
    applicability: dict[str, str] = {}
    for i, item in enumerate(_list(document, "layerApplicability")):
        layer = item.get("layer")
        if layer in applicability:
            add("DUSRM-02-M-014", "error", f"layerApplicability[{i}].layer",
                f"Layer '{layer}' has more than one applicability declaration.")
        else:
            applicability[layer] = item.get("applicability")
    for i, item in enumerate(_list(document, "responsibilities")):
        layer = item.get("primaryLayer")
        if applicability.get(layer) == "notApplicable":
            add("DUSRM-02-M-014", "error", f"responsibilities[{i}].primaryLayer",
                f"Responsibility '{item.get('id')}' is assigned to layer {layer}, which is declared notApplicable.")

    # Relationship endpoints and relationship scope.
    for i, item in enumerate(_list(document, "relationships")):
        path = f"relationships[{i}]"
        relation_type = item.get("type")
        signature = RELATIONSHIP_SIGNATURES.get(relation_type)
        source = check_typed_field(item, "source", path, signature[0] if signature else None)
        target = check_typed_field(item, "target", path, signature[1] if signature else None)
        scope = check_typed_field(item, "scopeRef", path, {"system", "boundary"})
        if scope is not None:
            for ref_name, ref in (("source", item.get("source")), ("target", item.get("target"))):
                if isinstance(ref, dict) and ref.get("kind") in PARTICIPANT_KINDS:
                    if ref.get("kind") == "system" and ref.get("id") != soi.get("id"):
                        add("DUSRM-02-M-015", "error", f"{path}.scopeRef",
                            "Relationship participant is a different system of interest from the declared description.")
        if relation_type == "transitionsTo" and source and target:
            if source.get("stateVariableRef") != target.get("stateVariableRef"):
                add("DUSRM-02-M-016", "error", path,
                    "transitionsTo endpoints must belong to the same state variable.")

    # Operations, executions and typed event/state references.
    for i, item in enumerate(_list(document, "operations")):
        check_participant_field(item, "ownerRef", f"operations[{i}]")
        for field in ("inputRefs", "outputRefs"):
            for j, ref in enumerate(item.get(field, [])):
                resolve_ref(ref, f"operations[{i}].{field}[{j}]")

    for i, item in enumerate(_list(document, "executions")):
        path = f"executions[{i}]"
        check_typed_field(item, "operationRef", path, {"operation"})
        check_participant_field(item, "subjectRef", path)
        state = item.get("executionState")
        if state in {"running", "suspended", "completed", "failed", "cancelled", "aborted"} and not item.get("startedAt"):
            add("DUSRM-02-M-017", "error", f"{path}.startedAt",
                f"Execution state '{state}' requires a startedAt timestamp.")
        if state in {"completed", "failed", "cancelled", "aborted"} and not item.get("endedAt"):
            add("DUSRM-02-M-017", "error", f"{path}.endedAt",
                f"Terminal execution state '{state}' requires an endedAt timestamp.")
        started, ended = _parse_time(item.get("startedAt")), _parse_time(item.get("endedAt"))
        if started and ended and ended < started:
            add("DUSRM-02-M-017", "error", f"{path}.endedAt",
                "Execution endedAt precedes startedAt.")

    for i, item in enumerate(_list(document, "events")):
        check_typed_field(item, "sourceRef", f"events[{i}]")

    state_variables = records["stateVariable"]
    states = records["state"]
    for i, item in enumerate(_list(document, "stateVariables")):
        check_participant_field(item, "subjectRef", f"stateVariables[{i}]")

    for i, item in enumerate(_list(document, "states")):
        path = f"states[{i}]"
        state_variable = check_typed_field(item, "stateVariableRef", path, {"stateVariable"})
        if state_variable is not None:
            values = state_variable.get("allowedValues")
            if isinstance(values, list) and item.get("value") not in values:
                add("DUSRM-02-M-018", "error", f"{path}.value",
                    f"State value {item.get('value')!r} is outside the allowedValues domain.")

    for i, item in enumerate(_list(document, "transitions")):
        path = f"transitions[{i}]"
        subject = check_participant_field(item, "subjectRef", path)
        source_state = check_typed_field(item, "fromStateRef", path, {"state"})
        target_state = check_typed_field(item, "toStateRef", path, {"state"})
        for j, ref in enumerate(item.get("triggerEventRefs", [])):
            resolve_ref(ref, f"{path}.triggerEventRefs[{j}]", {"event"})
        if source_state and target_state:
            source_variable = source_state.get("stateVariableRef")
            target_variable = target_state.get("stateVariableRef")
            if not _same_ref(source_variable, target_variable):
                add("DUSRM-02-M-019", "error", path,
                    "Transition source and target states must belong to the same state variable.")
            variable = states.get(source_state.get("id"), {}).get("stateVariableRef", {})
            variable_record = state_variables.get(variable.get("id")) if isinstance(variable, dict) else None
            if variable_record and subject and not _same_ref(
                {"kind": "element" if subject is not None and subject.get("id") in records["element"] else subject.get("kind"), "id": subject.get("id")},
                variable_record.get("subjectRef"),
            ):
                add("DUSRM-02-M-019", "warning", f"{path}.subjectRef",
                    "Transition subject differs from the state variable subject; confirm the modeled state scope.")

    # Interfaces and interactions preserve participant roles and interface membership.
    for i, item in enumerate(_list(document, "interfaces")):
        roles_seen: set[str] = set()
        participants_seen: set[tuple[str, str, str]] = set()
        for j, assignment in enumerate(item.get("participantRoles", [])):
            role = assignment.get("role")
            ref = assignment.get("participantRef")
            check_participant(ref, f"interfaces[{i}].participantRoles[{j}].participantRef")
            if role in roles_seen:
                add("DUSRM-02-M-020", "error", f"interfaces[{i}].participantRoles[{j}].role",
                    f"Interface role '{role}' is duplicated.")
            roles_seen.add(role)
            if isinstance(ref, dict):
                key = (str(ref.get("kind")), str(ref.get("id")), str(role))
                if key in participants_seen:
                    add("DUSRM-02-M-020", "error", f"interfaces[{i}].participantRoles[{j}]",
                        "Duplicate participant/role assignment.")
                participants_seen.add(key)
        check_typed_field(item, "contractSpecificationRef", f"interfaces[{i}]", {"specification"})
        for j, ref in enumerate(item.get("operationRefs", [])):
            resolve_ref(ref, f"interfaces[{i}].operationRefs[{j}]", {"operation"})

    interface_by_id = records["interface"]
    for i, item in enumerate(_list(document, "interactions")):
        path = f"interactions[{i}]"
        interface = check_typed_field(item, "interfaceRef", path, {"interface"})
        role_names: set[str] = set()
        interaction_participants: set[tuple[str, str, str]] = set()
        for j, assignment in enumerate(item.get("participantRoles", [])):
            role = assignment.get("role")
            ref = assignment.get("participantRef")
            check_participant(ref, f"{path}.participantRoles[{j}].participantRef")
            if role in role_names:
                add("DUSRM-02-M-020", "error", f"{path}.participantRoles[{j}].role",
                    f"Interaction role '{role}' is duplicated.")
            role_names.add(role)
            if isinstance(ref, dict):
                interaction_participants.add((str(ref.get("kind")), str(ref.get("id")), str(role)))
        if interface is not None:
            interface_roles = {
                (str(x.get("participantRef", {}).get("kind")),
                 str(x.get("participantRef", {}).get("id")),
                 str(x.get("role")))
                for x in interface.get("participantRoles", [])
            }
            if not interaction_participants.issubset(interface_roles):
                add("DUSRM-02-M-020", "error", f"{path}.participantRoles",
                    "Interaction contains a participant/role not declared by its referenced interface.")

    # Resources, allocation quantities and validity.
    for i, item in enumerate(_list(document, "resources")):
        check_participant_field(item, "ownerRef", f"resources[{i}]")

    for i, item in enumerate(_list(document, "allocations")):
        path = f"allocations[{i}]"
        check_participant_field(item, "allocatorRef", path)
        resource = check_typed_field(item, "resourceRef", path, {"resource"})
        check_participant_field(item, "recipientRef", path)
        start, end = _parse_time(item.get("validFrom")), _parse_time(item.get("validTo"))
        if start and end and end < start:
            add("DUSRM-02-M-022", "error", f"{path}.validTo",
                "Allocation validTo precedes validFrom.")
        if resource:
            capacity = resource.get("capacity")
            if isinstance(capacity, dict):
                cap_unit = capacity.get("unit")
                if cap_unit and cap_unit != item.get("unit"):
                    add("DUSRM-02-M-022", "warning", f"{path}.unit",
                        "Allocation unit differs from the resource capacity unit; verify conversion or document it.")
                if cap_unit == item.get("unit") and isinstance(capacity.get("value"), (int, float)):
                    if isinstance(item.get("quantity"), (int, float)) and item["quantity"] > capacity["value"]:
                        add("DUSRM-02-M-022", "error", f"{path}.quantity",
                            "Allocation quantity exceeds the declared resource capacity.")

    # Capabilities, services and references to requirements/constraints/invariants.
    for i, item in enumerate(_list(document, "capabilities")):
        check_participant_field(item, "providerRef", f"capabilities[{i}]")
        for j, ref in enumerate(item.get("operationRefs", [])):
            resolve_ref(ref, f"capabilities[{i}].operationRefs[{j}]", {"operation"})

    for i, item in enumerate(_list(document, "services")):
        path = f"services[{i}]"
        check_participant_field(item, "providerRef", path)
        check_typed_field(item, "capabilityRef", path, {"capability"})
        check_typed_field(item, "interfaceRef", path, {"interface"})
        for j, ref in enumerate(item.get("consumerRefs", [])):
            check_participant(ref, f"{path}.consumerRefs[{j}]")

    for collection in ("constraints", "invariants", "assertions", "decisions"):
        for i, item in enumerate(_list(document, collection)):
            for j, ref in enumerate(item.get("subjectRefs", [])):
                resolve_ref(ref, f"{collection}[{i}].subjectRefs[{j}]")
    for i, item in enumerate(_list(document, "requirements")):
        check_typed_field(item, "sourceRef", f"requirements[{i}]")

    # All remaining nested typed-reference fields and evidence scope references.
    for i, item in enumerate(_list(document, "properties")):
        path = f"properties[{i}]"
        check_typed_field(item, "subjectRef", path)
        check_typed_field(item, "sourceRef", path)
    for i, item in enumerate(_list(document, "decisions")):
        for j, ref in enumerate(item.get("subjectRefs", [])):
            resolve_ref(ref, f"decisions[{i}].subjectRefs[{j}]")
    for i, item in enumerate(_list(document, "evidence")):
        for j, ref in enumerate(item.get("scopeRefs", [])):
            resolve_ref(ref, f"evidence[{i}].scopeRefs[{j}]")

    # Evidence assessment: an assessment result is not self-authenticating.
    for collection in ("relationships", "invariants", "assertions"):
        for i, item in enumerate(_list(document, collection)):
            result = item.get("assessmentResult")
            refs = item.get("evidenceRefs", [])
            if result in {"pass", "passWithFindings", "fail"} and not refs:
                add("DUSRM-02-E-001", "error", f"{collection}[{i}].assessmentResult",
                    "An assessed result requires at least one linked evidence record.")
            if result in {"pass", "passWithFindings"} and refs:
                linked = [records["evidence"].get(ref) for ref in refs]
                if not any(x and x.get("relation") == "supports" for x in linked):
                    add("DUSRM-02-E-002", "warning", f"{collection}[{i}].evidenceRefs",
                        "A passing assessment has no linked evidence explicitly marked as supporting the claim.")

    # Profile compatibility is never inferred from version similarity.
    if registry is not None:
        profiles_by_id = {
            item.get("profileId"): item
            for item in registry.get("profiles", [])
            if isinstance(item, dict) and isinstance(item.get("profileId"), str)
        }
        for i, ref in enumerate(document.get("profileRefs", [])):
            profile = profiles_by_id.get(ref.get("profileId"))
            path = f"profileRefs[{i}]"
            if profile is None:
                add("DUSRM-02-P-001", "error", path,
                    f"Profile '{ref.get('profileId')}' is not present in the supplied registry.")
                continue
            if profile.get("profileVersion") != ref.get("version"):
                add("DUSRM-02-P-001", "error", path,
                    "Profile version does not match the registry entry.")
            if profile.get("compatibilityStatus") != "compatible":
                add("DUSRM-02-P-001", "warning", path,
                    "Profile compatibility is not explicitly approved by the registry.")

    return sorted(findings, key=lambda item: (item.path, item.code, item.severity, item.message))


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read JSON file {path}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a DUSRM schema 0.2 description.")
    parser.add_argument("description", type=Path, help="Path to a schema 0.2 JSON description.")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--no-registry", action="store_true", help="Skip profile-registry checks.")
    parser.add_argument("--json", action="store_true", help="Emit findings as JSON.")
    args = parser.parse_args()

    try:
        schema = load_json(args.schema)
        document = load_json(args.description)
        Draft202012Validator.check_schema(schema)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    structural = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(document),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if structural:
        for error in structural:
            print(f"SCHEMA ERROR {list(error.absolute_path)}: {error.message}", file=sys.stderr)
        return 1

    registry = None
    if not args.no_registry and args.registry.exists():
        try:
            registry = load_json(args.registry)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2

    findings = validate_semantics(document, registry)
    if args.json:
        print(json.dumps([asdict(item) for item in findings], indent=2))
    else:
        for item in findings:
            print(f"{item.severity.upper()} {item.code} {item.path}: {item.message}")

    errors = [item for item in findings if item.severity == "error"]
    warnings = [item for item in findings if item.severity == "warning"]
    print(f"\nDUSRM 0.2 semantic validation: {len(errors)} error(s), {len(warnings)} warning(s).")
    if errors:
        return 1
    if warnings:
        return 0
    print("No semantic findings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
