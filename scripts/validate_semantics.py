#!/usr/bin/env python3
"""DUSRM semantic consistency validator (0.8 draft).

The validator checks selected cross-reference, allocation, transition,
profile-registry, and evidence rules. It is not a safety certifier and does
not establish that a described implementation behaves as claimed.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schema" / "dusrm-description-0.1.schema.json"
DEFAULT_REGISTRY = ROOT / "profiles" / "registry.json"
EVIDENCE_KINDS_FOR_VERIFICATION = {
    "testResult", "toolOutput", "measurement", "observation", "analysis", "review"
}
PROMOTED_STATUSES = {"implemented", "observed", "tested", "verified"}


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    path: str
    message: str


def _items(document: dict[str, Any], name: str) -> list[dict[str, Any]]:
    value = document.get(name, [])
    return value if isinstance(value, list) else []


def _read_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read JSON file {path}: {exc}") from exc


def validate_semantics(
    document: dict[str, Any],
    registry: dict[str, Any],
) -> list[Finding]:
    """Return deterministic semantic findings for a schema-shaped description."""
    findings: list[Finding] = []

    def add(code: str, severity: str, path: str, message: str) -> None:
        findings.append(Finding(code, severity, path, message))

    context = document.get("context") or {}
    soi = context.get("systemOfInterest") or {}
    soi_id = soi.get("id")

    elements = _items(document, "elements")
    responsibilities = _items(document, "responsibilities")
    realizations = _items(document, "realizations")
    relationships = _items(document, "relationships")
    operations = _items(document, "operations")
    state_variables = _items(document, "stateVariables")
    transitions = _items(document, "transitions")
    evidence = _items(document, "evidence")
    claims = _items(document, "constraints") + _items(document, "invariants")
    environment = context.get("environment", [])
    if not isinstance(environment, list):
        environment = []

    # The SOI, in-scope elements, and declared environment participants share
    # one participant namespace because relationship endpoints are untyped IDs.
    participant_ids: dict[str, str] = {}
    for label, identifier in [("systemOfInterest", soi_id)]:
        if isinstance(identifier, str):
            participant_ids[identifier] = label

    for collection_name, records in (("elements", elements), ("environment", environment)):
        for index, record in enumerate(records):
            identifier = record.get("id")
            if not isinstance(identifier, str):
                continue
            location = f"{collection_name}[{index}].id"
            if identifier in participant_ids:
                add(
                    "DUSRM-M-001", "error", location,
                    f"Duplicate participant identifier '{identifier}' also used by {participant_ids[identifier]}.",
                )
            else:
                participant_ids[identifier] = f"{collection_name}[{index}]"

    # Each typed collection has its own identifier namespace.
    collections = {
        "responsibilities": responsibilities,
        "realizations": realizations,
        "relationships": relationships,
        "operations": operations,
        "stateVariables": state_variables,
        "transitions": transitions,
        "evidence": evidence,
        "claims": claims,
    }
    for name, records in collections.items():
        seen: set[str] = set()
        for index, record in enumerate(records):
            identifier = record.get("id")
            if not isinstance(identifier, str):
                continue
            if identifier in seen:
                add(
                    "DUSRM-M-001", "error", f"{name}[{index}].id",
                    f"Duplicate identifier '{identifier}' in the {name} namespace.",
                )
            seen.add(identifier)

    element_by_id = {x.get("id"): x for x in elements if isinstance(x.get("id"), str)}
    responsibility_by_id = {x.get("id"): x for x in responsibilities if isinstance(x.get("id"), str)}
    state_by_id = {x.get("id"): x for x in state_variables if isinstance(x.get("id"), str)}
    evidence_by_id = {x.get("id"): x for x in evidence if isinstance(x.get("id"), str)}

    def require_ref(identifier: Any, allowed: set[str], code: str, path: str, label: str) -> None:
        if not isinstance(identifier, str) or identifier not in allowed:
            add(code, "error", path, f"{label} reference '{identifier}' does not resolve.")

    # Realization is a typed many-to-many relation; element-to-layer exclusivity
    # is intentionally not imposed.
    realization_pairs: set[tuple[str, str]] = set()
    realization_counts: dict[str, int] = {}
    for index, realization in enumerate(realizations):
        element_ref = realization.get("elementRef")
        responsibility_ref = realization.get("responsibilityRef")
        require_ref(element_ref, set(element_by_id), "DUSRM-M-003",
                    f"realizations[{index}].elementRef", "Element")
        require_ref(responsibility_ref, set(responsibility_by_id), "DUSRM-M-003",
                    f"realizations[{index}].responsibilityRef", "Responsibility")
        if isinstance(element_ref, str) and isinstance(responsibility_ref, str):
            pair = (element_ref, responsibility_ref)
            if pair in realization_pairs:
                add(
                    "DUSRM-M-013", "error", f"realizations[{index}]",
                    f"Duplicate realization pair {element_ref!r} -> {responsibility_ref!r}.",
                )
            realization_pairs.add(pair)
            realization_counts[responsibility_ref] = realization_counts.get(responsibility_ref, 0) + 1

        if realization.get("status") in PROMOTED_STATUSES:
            target = element_by_id.get(element_ref, {})
            if target.get("status") in {"planned", "simulated", "unknown"}:
                add(
                    "DUSRM-E-003", "error", f"realizations[{index}].status",
                    "A promoted realization status conflicts with the referenced element's maturity status.",
                )

    for index, responsibility in enumerate(responsibilities):
        identifier = responsibility.get("id")
        if identifier and realization_counts.get(identifier, 0) == 0:
            if responsibility.get("status") not in {"planned", "unknown", "notApplicable"}:
                add(
                    "DUSRM-M-012", "warning", f"responsibilities[{index}]",
                    "Responsibility has no realizing element; record this as planned, not applicable, or an explicit architecture gap.",
                )

    # Relationship endpoints may be model elements, external environment
    # participants, or the SOI itself. No implicit layer-order dependency is inferred.
    for index, relationship in enumerate(relationships):
        require_ref(
            relationship.get("sourceRef"), set(participant_ids),
            "DUSRM-M-002", f"relationships[{index}].sourceRef", "Relationship source",
        )
        require_ref(
            relationship.get("targetRef"), set(participant_ids),
            "DUSRM-M-002", f"relationships[{index}].targetRef", "Relationship target",
        )
        scope_ref = relationship.get("scopeRef")
        if scope_ref is not None:
            require_ref(
                scope_ref, set(participant_ids), "DUSRM-M-007",
                f"relationships[{index}].scopeRef", "Relationship scope",
            )
        if relationship.get("status") in PROMOTED_STATUSES:
            endpoints = [
                element_by_id.get(relationship.get("sourceRef")),
                element_by_id.get(relationship.get("targetRef")),
            ]
            if any(e and e.get("status") in {"planned", "simulated", "unknown"} for e in endpoints):
                add(
                    "DUSRM-E-003", "error", f"relationships[{index}].status",
                    "A promoted relationship status conflicts with a planned, simulated, or unknown endpoint.",
                )

    for index, operation in enumerate(operations):
        require_ref(
            operation.get("ownerRef"), set(element_by_id),
            "DUSRM-M-008", f"operations[{index}].ownerRef", "Operation owner",
        )

    states_by_subject: dict[str, list[dict[str, Any]]] = {}
    for index, state in enumerate(state_variables):
        subject_ref = state.get("subjectRef")
        require_ref(
            subject_ref, set(element_by_id),
            "DUSRM-M-009", f"stateVariables[{index}].subjectRef", "State-variable subject",
        )
        if isinstance(subject_ref, str):
            states_by_subject.setdefault(subject_ref, []).append(state)
        allowed = state.get("allowedValues")
        if isinstance(allowed, list) and len(allowed) != len(set(allowed)):
            add(
                "DUSRM-M-014", "error", f"stateVariables[{index}].allowedValues",
                "State-variable allowedValues contains duplicates.",
            )

    for index, transition in enumerate(transitions):
        subject_ref = transition.get("subjectRef")
        require_ref(
            subject_ref, set(element_by_id),
            "DUSRM-M-010", f"transitions[{index}].subjectRef", "Transition subject",
        )

        state_ref = transition.get("stateVariableRef")
        candidate_states = states_by_subject.get(subject_ref, [])
        selected_state = None
        if state_ref is not None:
            require_ref(
                state_ref, set(state_by_id),
                "DUSRM-M-010", f"transitions[{index}].stateVariableRef", "Transition state variable",
            )
            selected_state = state_by_id.get(state_ref)
            if selected_state and selected_state.get("subjectRef") != subject_ref:
                add(
                    "DUSRM-M-010", "error", f"transitions[{index}].stateVariableRef",
                    "Transition stateVariableRef belongs to a different subject.",
                )
        elif len(candidate_states) == 1:
            selected_state = candidate_states[0]
        elif len(candidate_states) > 1:
            add(
                "DUSRM-M-010", "warning", f"transitions[{index}].stateVariableRef",
                "Multiple state variables exist for this subject; identify stateVariableRef to disambiguate the transition domain.",
            )
        elif subject_ref in element_by_id:
            add(
                "DUSRM-M-010", "warning", f"transitions[{index}]",
                "No state-variable definition exists for this transition subject.",
            )

        if selected_state:
            allowed = selected_state.get("allowedValues")
            if isinstance(allowed, list) and allowed:
                for endpoint in ("from", "to"):
                    if transition.get(endpoint) not in allowed:
                        add(
                            "DUSRM-M-015", "error", f"transitions[{index}].{endpoint}",
                            f"Transition {endpoint} value {transition.get(endpoint)!r} is outside the selected state's allowedValues.",
                        )

    # Every evidence reference must resolve. Verified assertions need stronger
    # evidence than a file/document reference alone.
    evidence_kinds_for_verification = EVIDENCE_KINDS_FOR_VERIFICATION
    evidence_ref_bearing: list[tuple[str, dict[str, Any]]] = []
    for collection_name, records in (
        ("elements", elements),
        ("realizations", realizations),
        ("relationships", relationships),
        ("transitions", transitions),
    ):
        evidence_ref_bearing.extend((f"{collection_name}[{i}]", record) for i, record in enumerate(records))

    for location, record in evidence_ref_bearing:
        refs = record.get("evidenceRefs", [])
        if not isinstance(refs, list):
            continue
        resolved: list[dict[str, Any]] = []
        for ref_index, evidence_ref in enumerate(refs):
            if evidence_ref not in evidence_by_id:
                add(
                    "DUSRM-M-011", "error", f"{location}.evidenceRefs[{ref_index}]",
                    f"Evidence reference '{evidence_ref}' does not resolve.",
                )
            else:
                resolved.append(evidence_by_id[evidence_ref])

        status = record.get("status")
        if status in PROMOTED_STATUSES and not refs:
            severity = "error" if status == "verified" else "warning"
            add(
                "DUSRM-E-002", severity, f"{location}.status",
                f"Status '{status}' has no linked evidence reference.",
            )

        if status == "verified":
            adequate = [
                item for item in resolved
                if item.get("kind") in evidence_kinds_for_verification
                and isinstance(item.get("method"), str) and item["method"].strip()
                and item.get("status") in {"tested", "observed", "verified"}
            ]
            if not adequate:
                add(
                    "DUSRM-E-001", "error", location,
                    "Verified status requires linked test, observation, measurement, analysis, tool, or review evidence with a recorded method and an adequate evidence status.",
                )

    # Claims always have evidenceRefs in the schema, so a verified claim without
    # traceable evidence is an error.
    for collection_name in ("constraints", "invariants"):
        for index, claim in enumerate(_items(document, collection_name)):
            refs = claim.get("evidenceRefs", [])
            for ref_index, evidence_ref in enumerate(refs):
                if evidence_ref not in evidence_by_id:
                    add(
                        "DUSRM-M-011", "error",
                        f"{collection_name}[{index}].evidenceRefs[{ref_index}]",
                        f"Evidence reference '{evidence_ref}' does not resolve.",
                    )
            if claim.get("status") == "verified":
                adequate = [
                    evidence_by_id[ref] for ref in refs if ref in evidence_by_id
                    and evidence_by_id[ref].get("kind") in evidence_kinds_for_verification
                    and isinstance(evidence_by_id[ref].get("method"), str)
                    and evidence_by_id[ref]["method"].strip()
                    and evidence_by_id[ref].get("status") in {"tested", "observed", "verified"}
                ]
                if not adequate:
                    add(
                        "DUSRM-E-001", "error", f"{collection_name}[{index}]",
                        "Verified claim requires linked assessment evidence and a recorded method.",
                    )

    # Profile extensions must use a reverse-domain or profile-qualified namespace.
    extensions = document.get("extensions", {})
    if isinstance(extensions, dict):
        for extension_key in extensions:
            if not isinstance(extension_key, str) or "." not in extension_key:
                add(
                    "DUSRM-P-002", "error", f"extensions.{extension_key}",
                    "Extension keys must be namespaced (for example, org.example.profile.feature).",
                )

    # Profile compatibility is explicit. A candidate version or a draft profile
    # is not treated as compatible until the registry says so.
    registry_profiles = {
        entry.get("profileId"): entry
        for entry in registry.get("profiles", [])
        if isinstance(entry, dict) and isinstance(entry.get("profileId"), str)
    }
    for index, profile_ref in enumerate(_items(document, "profileRefs")):
        profile_id = profile_ref.get("profileId")
        profile_version = profile_ref.get("version")
        registry_entry = registry_profiles.get(profile_id)
        if registry_entry is None:
            add(
                "DUSRM-P-001", "error", f"profileRefs[{index}].profileId",
                f"Profile '{profile_id}' is not present in the supplied profile registry.",
            )
            continue
        if profile_version != registry_entry.get("profileVersion"):
            add(
                "DUSRM-P-001", "error", f"profileRefs[{index}].version",
                f"Profile version '{profile_version}' does not match registry version '{registry_entry.get('profileVersion')}'.",
            )
        if registry_entry.get("candidateCoreVersion") != document.get("dusrmVersion"):
            add(
                "DUSRM-P-001", "error", f"profileRefs[{index}]",
                "Profile registry candidate core version does not match the description's DUSRM version.",
            )
        if registry_entry.get("compatibilityStatus") != "compatible":
            add(
                "DUSRM-P-001", "error", f"profileRefs[{index}]",
                f"Profile compatibility is '{registry_entry.get('compatibilityStatus', 'unspecified')}', not explicitly compatible.",
            )
        if registry_entry.get("status") in {"deprecated", "rejected"}:
            add(
                "DUSRM-P-001", "error", f"profileRefs[{index}]",
                f"Profile registry status '{registry_entry.get('status')}' is not selectable.",
            )

    # Stable ordering keeps reports reproducible.
    severity_order = {"error": 0, "warning": 1}
    return sorted(findings, key=lambda f: (severity_order.get(f.severity, 9), f.code, f.path, f.message))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a DUSRM description's structural and semantic rules.")
    parser.add_argument("description", type=Path, help="Path to a DUSRM JSON description.")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA, help="JSON Schema path.")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY, help="Profile registry path.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable findings.")
    args = parser.parse_args(argv)

    try:
        description = _read_json(args.description)
        schema = _read_json(args.schema)
        registry = _read_json(args.registry)
        Draft202012Validator.check_schema(schema)
        schema_errors = sorted(
            Draft202012Validator(schema).iter_errors(description),
            key=lambda error: (list(error.absolute_path), error.message),
        )
    except (ValueError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if schema_errors:
        if args.json:
            print(json.dumps({
                "result": "schema-failed",
                "findings": [
                    {"code": "DUSRM-S-001", "severity": "error",
                     "path": "/" + "/".join(str(p) for p in error.absolute_path),
                     "message": error.message}
                    for error in schema_errors
                ],
            }, indent=2))
        else:
            print(f"Schema validation failed with {len(schema_errors)} error(s):")
            for error in schema_errors:
                path = "/" + "/".join(str(p) for p in error.absolute_path)
                print(f"ERROR DUSRM-S-001 {path}: {error.message}")
        return 2

    findings = validate_semantics(description, registry)
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    if args.json:
        print(json.dumps({
            "result": "semantic-failed" if errors else ("passed-with-warnings" if warnings else "passed"),
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        for finding in findings:
            print(f"{finding.severity.upper()} {finding.code} {finding.path}: {finding.message}")
        if errors:
            print(f"\nDUSRM semantic validation FAILED: {len(errors)} error(s), {len(warnings)} warning(s).")
        elif warnings:
            print(f"\nDUSRM semantic validation passed with {len(warnings)} warning(s).")
        else:
            print("\nDUSRM semantic validation passed with no findings.")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
