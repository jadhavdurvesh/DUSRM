#!/usr/bin/env python3
"""Loss-aware migrator from DUSRM schema 0.1-draft to 0.2-draft.

The migrator preserves source files, records every uncertain conversion, and
never invents typed endpoints. Use --allow-incomplete only when you want a
structurally valid draft with unresolved legacy records omitted and reported.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_01 = ROOT / "schema" / "dusrm-description-0.1.schema.json"
SCHEMA_02 = ROOT / "schema" / "dusrm-description-0.2.schema.json"

RELATIONSHIP_KINDS = {
    "memberOf": ({"element"}, {"system", "element"}),
    "decomposesInto": ({"system", "element"}, {"element"}),
    "containedWithin": ({"element"}, {"element", "boundary"}),
    "dependsOn": ({"system", "element", "environmentParticipant"}, {"system", "element", "environmentParticipant"}),
    "exposes": ({"system", "element", "environmentParticipant"}, {"interface"}),
    "requires": ({"system", "element", "environmentParticipant"}, {"interface", "capability", "resource"}),
    "interactsWith": ({"system", "element", "environmentParticipant"}, {"system", "element", "environmentParticipant"}),
    "allocates": ({"system", "element", "environmentParticipant"}, {"resource"}),
    "performs": ({"execution"}, {"operation"}),
    "triggers": ({"event"}, {"transition", "operation"}),
    "transitionsTo": ({"state"}, {"state"}),
    "observes": ({"system", "element", "environmentParticipant"}, {"element", "event", "property", "state"}),
    "controls": ({"system", "element", "environmentParticipant"}, {"element", "operation", "execution"}),
    "constrainedBy": ({"element", "operation", "execution"}, {"constraint"}),
    "satisfies": ({"element", "responsibility", "operation", "capability", "service"}, {"requirement"}),
    "derivedFrom": ({"requirement", "decision", "assertion"}, {"evidence", "requirement", "decision", "assertion"}),
    "implements": ({"element"}, {"specification"}),
}

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


class Migration:
    def __init__(self, source: dict[str, Any]) -> None:
        self.source = source
        self.output: dict[str, Any] = {}
        self.warnings: list[dict[str, str]] = []
        self.blockers: list[dict[str, str]] = []
        self.dropped: list[dict[str, str]] = []
        self.id_kind: dict[str, str] = {}
        self.boundary_id = self._stable_id(f"{source.get('descriptionId', 'description')}.boundary")

    @staticmethod
    def _stable_id(value: str) -> str:
        value = re.sub(r"[^A-Za-z0-9._:-]", "-", value)
        if not value or not value[0].isalpha():
            value = "MIG-" + value
        return value[:128]

    def warn(self, path: str, message: str) -> None:
        self.warnings.append({"path": path, "message": message})

    def block(self, path: str, message: str) -> None:
        self.blockers.append({"path": path, "message": message})

    def register(self, identifier: Any, kind: str, path: str) -> None:
        if not isinstance(identifier, str):
            return
        previous = self.id_kind.get(identifier)
        if previous is not None:
            self.block(path, f"Identifier '{identifier}' is ambiguous across kinds '{previous}' and '{kind}'.")
        else:
            self.id_kind[identifier] = kind

    def typed_ref(self, identifier: Any, allowed: set[str], path: str) -> dict[str, str] | None:
        if not isinstance(identifier, str):
            self.block(path, "Legacy endpoint is not a string identifier.")
            return None
        kind = self.id_kind.get(identifier)
        if kind is None:
            self.block(path, f"Legacy reference '{identifier}' cannot be resolved to a declared object.")
            return None
        if kind not in allowed:
            self.block(path, f"Legacy reference '{identifier}' resolves to '{kind}', not an allowed endpoint kind {sorted(allowed)}.")
            return None
        return {"kind": kind, "id": identifier}

    def participant_ref(self, identifier: Any, path: str) -> dict[str, str] | None:
        return self.typed_ref(identifier, {"system", "element", "environmentParticipant"}, path)

    def realization_state(self, legacy: Any, path: str) -> str:
        direct = {
            "planned": "planned",
            "implemented": "implemented",
            "unknown": "unknown",
        }
        if legacy in direct:
            return direct[legacy]
        if legacy == "notApplicable":
            self.warn(path, "Legacy notApplicable is an applicability value, not a realization state; mapped to unknown for review.")
            return "unknown"
        if legacy in {"proposed", "specified", "simulated", "observed", "tested", "verified", "assumed", "rejected"}:
            self.warn(path, f"Legacy status '{legacy}' cannot be safely converted into realizationState; mapped to unknown.")
            return "unknown"
        self.warn(path, f"Unrecognized legacy status '{legacy}'; mapped to unknown.")
        return "unknown"

    def disposition(self, legacy: Any, path: str) -> str:
        if legacy in {"proposed", "rejected"}:
            return legacy
        if legacy in {"specified", "planned", "implemented", "simulated", "observed", "tested", "verified", "assumed", "unknown", "notApplicable"}:
            self.warn(path, f"Legacy status '{legacy}' does not establish a design disposition; mapped to proposed.")
            return "proposed"
        self.warn(path, f"Unrecognized legacy status '{legacy}'; mapped to proposed.")
        return "proposed"

    def base(self) -> dict[str, Any]:
        src = self.source
        context = src.get("context") or {}
        old_soi = context.get("systemOfInterest") or {}
        soi_id = old_soi.get("id", "MIG-SOI")
        self.register(soi_id, "system", "context.systemOfInterest.id")
        old_boundary = self._stable_id(f"{src.get('descriptionId', 'description')}.boundary")
        self.register(old_boundary, "boundary", "context.boundary")

        for i, item in enumerate(context.get("environment", [])):
            if isinstance(item, dict):
                self.register(item.get("id"), "environmentParticipant", f"context.environment[{i}].id")
        for i, item in enumerate(src.get("elements", [])):
            if isinstance(item, dict):
                self.register(item.get("id"), "element", f"elements[{i}].id")
        for kind, collection in (
            ("responsibility", "responsibilities"),
            ("property", "properties"),
            ("specification", "specifications"),
            ("operation", "operations"),
            ("execution", "executions"),
            ("event", "events"),
            ("stateVariable", "stateVariables"),
            ("state", "states"),
            ("transition", "transitions"),
            ("interface", "interfaces"),
            ("interaction", "interactions"),
            ("resource", "resources"),
            ("allocation", "allocations"),
            ("capability", "capabilities"),
            ("service", "services"),
            ("requirement", "requirements"),
            ("constraint", "constraints"),
            ("invariant", "invariants"),
            ("assertion", "assertions"),
            ("decision", "decisions"),
            ("evidence", "evidence"),
        ):
            for i, item in enumerate(src.get(collection, [])):
                if isinstance(item, dict):
                    self.register(item.get("id"), kind, f"{collection}[{i}].id")

        self.output = {
            "schemaVersion": "0.2-draft",
            "dusrmVersion": src.get("dusrmVersion", "1.0-preparation"),
            "descriptionId": src.get("descriptionId", "migrated-description"),
            "title": src.get("title", "Migrated DUSRM Description"),
            "descriptionState": "draft",
            "profileRefs": src.get("profileRefs", []),
            "context": {
                "systemOfInterest": {
                    "id": soi_id,
                    "name": old_soi.get("name", "Migrated system of interest"),
                    "category": "other",
                    "kind": "legacy-system",
                    "description": old_soi.get("purpose", ""),
                    "realizationState": self.realization_state(old_soi.get("status"), "context.systemOfInterest.status"),
                    "evidenceRefs": [],
                },
                "purpose": context.get("purpose", "Migrated from schema 0.1; confirm purpose."),
                "scope": context.get("scope", "Migrated scope; review required."),
                "abstractionLevel": "migration-needs-review",
                "boundary": {
                    "id": old_boundary,
                    "inclusions": (context.get("boundary") or {}).get("inclusions", []),
                    "exclusions": (context.get("boundary") or {}).get("exclusions", []),
                    "notes": "Boundary converted from schema 0.1; confirm generated identifier and abstraction.",
                },
                "environment": [],
                "assumptions": list(context.get("assumptions", [])),
            },
        }
        self.output["summary"] = src.get("summary", "")

        for i, item in enumerate(context.get("environment", [])):
            if not isinstance(item, dict):
                continue
            self.output["context"]["environment"].append({
                "id": item["id"],
                "name": item.get("name", item["id"]),
                "category": "other",
                "kind": "legacy-environment-participant",
                "roles": [item.get("role", "legacy-role")],
                "description": "Category and kind require review; legacy schema did not define them.",
                "evidenceRefs": item.get("evidenceRefs", []),
            })
            self.warn(f"context.environment[{i}]", "Category/kind were not represented in schema 0.1; mapped to 'other' and a generic kind for review.")

        if "extensions" in src:
            self.output["extensions"] = src["extensions"]
            self.warn("extensions", "Legacy extensions were preserved without checking their namespace semantics.")

        for collection in COLLECTIONS.values():
            self.output[collection] = []
        self.output["layerApplicability"] = []
        return self.output

    def migrate_elements_and_responsibilities(self) -> None:
        src = self.source
        for i, item in enumerate(src.get("elements", [])):
            path = f"elements[{i}]"
            self.output["elements"].append({
                "id": item["id"],
                "name": item.get("name", item["id"]),
                "category": "other",
                "kind": item.get("kind", "legacy-element"),
                "roles": [],
                "description": item.get("description", ""),
                "realizationState": self.realization_state(item.get("status"), f"{path}.status"),
                "evidenceRefs": item.get("evidenceRefs", []),
            })
            self.warn(path, "Legacy schema did not separate category and roles; category 'other' and no roles require human review.")

        for i, item in enumerate(src.get("responsibilities", [])):
            path = f"responsibilities[{i}]"
            entry = {
                "id": item["id"],
                "name": item.get("name", item["id"]),
                "description": item.get("description", "Legacy responsibility description missing."),
                "primaryLayer": item.get("primaryLayer"),
                "realizationState": self.realization_state(item.get("status"), f"{path}.status"),
                "evidenceRefs": [],
            }
            if item.get("parentResponsibilityRef"):
                entry["parentResponsibilityRef"] = item["parentResponsibilityRef"]
            self.output["responsibilities"].append(entry)
        for i, item in enumerate(src.get("realizations", [])):
            path = f"realizations[{i}]"
            self.output["realizations"].append({
                "id": item["id"],
                "elementRef": item.get("elementRef"),
                "responsibilityRef": item.get("responsibilityRef"),
                "realizationState": self.realization_state(item.get("status"), f"{path}.status"),
                "rationale": item.get("rationale", "Legacy realization; review rationale."),
                "evidenceRefs": item.get("evidenceRefs", []),
            })
        self._migrate_layer_applicability()

    def _migrate_layer_applicability(self) -> None:
        # The old format did not have layer applicability. Do not invent it.
        for i in range(1, 9):
            self.output["layerApplicability"].append({
                "layer": f"L{i}",
                "applicability": "unknown",
                "rationale": "Schema 0.1 did not record explicit layer applicability; review required.",
            })
        self.warn("layerApplicability", "No layer applicability is inferred from the legacy description; all eight layers are marked unknown.")

    def migrate_evidence(self) -> None:
        kind_map = {
            "sourceDocument": ("sourceDocument", "sourceInspection"),
            "sourceCode": ("sourceCode", "sourceInspection"),
            "testResult": ("testResult", "test"),
            "toolOutput": ("toolOutput", "other"),
            "measurement": ("measurement", "measurement"),
            "observation": ("observation", "observation"),
            "analysis": ("analysis", "other"),
            "review": ("review", "designReview"),
            "assumption": ("assumption", "other"),
        }
        for i, item in enumerate(self.source.get("evidence", [])):
            path = f"evidence[{i}]"
            kind, method = kind_map.get(item.get("kind"), ("assumption", "other"))
            legacy_method = item.get("method")
            if isinstance(legacy_method, str) and legacy_method.strip():
                self.warn(f"{path}.method", "Legacy free-text method was not forced into the 0.2 method enum; inferred method retained only when clearly mapped.")
            entry = {
                "id": item["id"],
                "kind": kind,
                "method": method,
                "context": "other",
                "relation": "inconclusive",
                "description": item.get("description", "Migrated evidence record; review required."),
                "limitations": ["Legacy evidence status and assertion linkage were not sufficient to infer evidential strength."],
            }
            if item.get("sourceUri"):
                entry["sourceUri"] = item["sourceUri"]
            if item.get("revision"):
                entry["revision"] = item["revision"]
            if item.get("method"):
                entry["resultSummary"] = f"Legacy method (unmapped): {item['method']}"
            self.output["evidence"].append(entry)
            self.warn(path, "Evidence status was not carried forward as a strength claim; context and support relation require review.")

        self.output["context"]["systemOfInterest"]["evidenceRefs"] = [
            ref for ref in (self.source.get("context", {}).get("systemOfInterest", {}).get("evidenceRefs", []))
            if isinstance(ref, str)
        ]

    def migrate_operations_and_state(self) -> None:
        src = self.source
        for i, item in enumerate(src.get("operations", [])):
            path = f"operations[{i}]"
            owner = self.participant_ref(item.get("ownerRef"), f"{path}.ownerRef")
            if owner is None:
                self.dropped.append({"path": path, "message": "Operation omitted because owner could not be typed without guessing."})
                continue
            self.output["operations"].append({
                "id": item["id"],
                "name": item.get("name", item["id"]),
                "ownerRef": owner,
                "purpose": item.get("purpose", "Legacy operation; review purpose."),
                "designDisposition": self.disposition(item.get("status"), f"{path}.status"),
                "realizationState": self.realization_state(item.get("status"), f"{path}.status"),
                "preconditions": item.get("preconditions", []),
                "postconditions": item.get("postconditions", []),
                "failureConditions": item.get("failureConditions", []),
                "inputRefs": [],
                "outputRefs": [],
                "evidenceRefs": [],
            })
        for i, item in enumerate(src.get("stateVariables", [])):
            path = f"stateVariables[{i}]"
            subject = self.participant_ref(item.get("subjectRef"), f"{path}.subjectRef")
            if subject is None:
                self.dropped.append({"path": path, "message": "State variable omitted because subject could not be typed."})
                continue
            entry = {
                "id": item["id"],
                "subjectRef": subject,
                "name": item.get("name", item["id"]),
                "meaning": item.get("meaning", "Legacy state meaning; review required."),
                "valueType": item.get("valueType", "legacy-unspecified"),
            }
            if item.get("unit"):
                entry["unit"] = item["unit"]
            if isinstance(item.get("allowedValues"), list):
                entry["allowedValues"] = item["allowedValues"]
            self.output["stateVariables"].append(entry)

        # Explicitly create State records for finite values and for transition endpoints.
        variable_by_subject: dict[str, list[dict[str, Any]]] = {}
        for variable in self.output["stateVariables"]:
            variable_by_subject.setdefault(variable["subjectRef"]["id"], []).append(variable)
        state_ids: dict[tuple[str, str], str] = {}
        for variable in self.output["stateVariables"]:
            values = list(variable.get("allowedValues", []))
            for transition in src.get("transitions", []):
                if transition.get("subjectRef") == variable["subjectRef"]["id"]:
                    values.extend([transition.get("from"), transition.get("to")])
            for value in dict.fromkeys(v for v in values if isinstance(v, (str, int, float, bool))):
                state_id = self._stable_id(f"{variable['id']}.state.{str(value)}")
                state_ids[(variable["id"], str(value))] = state_id
                self.output["states"].append({
                    "id": state_id,
                    "stateVariableRef": {"kind": "stateVariable", "id": variable["id"]},
                    "value": value,
                    "meaning": f"Migrated value '{value}' for legacy state variable '{variable['name']}'; review required.",
                })
                self.register(state_id, "state", f"migrated.states.{state_id}")

        for i, item in enumerate(src.get("transitions", [])):
            path = f"transitions[{i}]"
            subject = self.participant_ref(item.get("subjectRef"), f"{path}.subjectRef")
            variable_ref = item.get("stateVariableRef")
            candidates = [v for v in self.output["stateVariables"] if (
                v["id"] == variable_ref or v["subjectRef"]["id"] == item.get("subjectRef")
            )]
            if variable_ref:
                candidates = [v for v in candidates if v["id"] == variable_ref]
            if len(candidates) != 1 or subject is None:
                self.block(path, "Transition cannot be migrated unambiguously: its subject/state variable mapping is missing or ambiguous.")
                self.dropped.append({"path": path, "message": "Transition omitted pending a human decision about state ownership."})
                continue
            variable = candidates[0]
            from_id = state_ids.get((variable["id"], str(item.get("from"))))
            to_id = state_ids.get((variable["id"], str(item.get("to"))))
            if not from_id or not to_id:
                self.block(path, "Transition source or destination could not be represented as a declared State.")
                continue
            guard = item.get("guard", "")
            if item.get("trigger"):
                guard = (guard + " | " if guard else "") + f"Legacy trigger description (not a typed Event): {item['trigger']}"
                self.warn(f"{path}.trigger", "Legacy trigger string was preserved as descriptive guard text; no Event was invented.")
            entry = {
                "id": item["id"],
                "subjectRef": subject,
                "fromStateRef": {"kind": "state", "id": from_id},
                "toStateRef": {"kind": "state", "id": to_id},
                "designDisposition": self.disposition(item.get("status"), f"{path}.status"),
                "realizationState": self.realization_state(item.get("status"), f"{path}.status"),
                "evidenceRefs": item.get("evidenceRefs", []),
            }
            if guard:
                entry["guard"] = guard
            if item.get("effect"):
                entry["effect"] = item["effect"]
            self.output["transitions"].append(entry)

    def migrate_relationships(self) -> None:
        for i, item in enumerate(self.source.get("relationships", [])):
            path = f"relationships[{i}]"
            old_type = item.get("type")
            source_id, target_id = item.get("sourceRef"), item.get("targetRef")
            if old_type == "realizes":
                if self.id_kind.get(source_id) == "element" and self.id_kind.get(target_id) == "responsibility":
                    self.output["realizations"].append({
                        "id": self._stable_id(item.get("id", f"MIG-REAL-{i}")),
                        "elementRef": source_id,
                        "responsibilityRef": target_id,
                        "realizationState": self.realization_state(item.get("status"), f"{path}.status"),
                        "rationale": item.get("rationale", "Migrated from legacy realizes relationship; review."),
                        "evidenceRefs": item.get("evidenceRefs", []),
                    })
                else:
                    self.block(path, "Legacy realizes relationship is ambiguous; cannot determine whether it represents responsibility allocation or implementation trace.")
                    self.dropped.append({"path": path, "message": "Ambiguous realizes relationship omitted pending manual classification."})
                continue
            if old_type not in RELATIONSHIP_KINDS:
                self.block(f"{path}.type", f"Relationship type '{old_type}' is not in the schema 0.2 core vocabulary.")
                self.dropped.append({"path": path, "message": "Unsupported relationship omitted."})
                continue
            source_kinds, target_kinds = RELATIONSHIP_KINDS[old_type]
            source = self.typed_ref(source_id, source_kinds, f"{path}.sourceRef")
            target = self.typed_ref(target_id, target_kinds, f"{path}.targetRef")
            if source is None or target is None:
                self.dropped.append({"path": path, "message": "Relationship omitted because its typed endpoints could not be resolved without guessing."})
                continue
            entry = {
                "id": item["id"],
                "type": old_type,
                "source": source,
                "target": target,
                "rationale": item.get("rationale", "Legacy relationship; review rationale."),
                "designDisposition": self.disposition(item.get("status"), f"{path}.status"),
                "assessmentResult": "notAssessed",
                "realizationState": self.realization_state(item.get("status"), f"{path}.status"),
                "evidenceRefs": item.get("evidenceRefs", []),
            }
            if item.get("scopeRef"):
                scope = self.typed_ref(item["scopeRef"], {"system", "boundary"}, f"{path}.scopeRef")
                if scope:
                    entry["scopeRef"] = scope
            self.output["relationships"].append(entry)

    def migrate_claims(self) -> None:
        for old_collection, new_collection, category in (
            ("constraints", "constraints", None),
            ("invariants", "invariants", None),
        ):
            for i, item in enumerate(self.source.get(old_collection, [])):
                path = f"{old_collection}[{i}]"
                raw_scope = item.get("scopeRef")
                scope = self.typed_ref(raw_scope, set(COLLECTIONS) | {"system", "environmentParticipant"}, f"{path}.scopeRef") if raw_scope else None
                if scope is None:
                    self.dropped.append({"path": path, "message": "Claim omitted because schema 0.1 did not provide an unambiguous typed subject scope."})
                    self.warn(path, "Provide at least one explicit typed subject reference before migrating this claim.")
                    continue
                if new_collection == "constraints":
                    self.output["constraints"].append({
                        "id": item["id"], "statement": item.get("statement", "Migrated constraint; review."),
                        "category": "other", "subjectRefs": [scope], "applicability": "unknown",
                        "evidenceRefs": item.get("evidenceRefs", []),
                    })
                else:
                    self.output["invariants"].append({
                        "id": item["id"], "statement": item.get("statement", "Migrated invariant; review."),
                        "subjectRefs": [scope], "assumptions": item.get("assumptions", []),
                        "assessmentResult": "notAssessed", "method": "Legacy assessment status was not safely convertible.",
                        "evidenceRefs": item.get("evidenceRefs", []),
                    })
                self.warn(path, "Legacy claim status was not promoted to a schema 0.2 assessment result.")

    def run(self) -> dict[str, Any]:
        self.base()
        self.migrate_elements_and_responsibilities()
        self.migrate_evidence()
        self.migrate_operations_and_state()
        self.migrate_relationships()
        self.migrate_claims()

        report = {
            "migration": "DUSRM schema 0.1-draft to 0.2-draft",
            "sourceDescriptionId": self.source.get("descriptionId"),
            "targetDescriptionId": self.output.get("descriptionId"),
            "complete": not self.blockers and not self.warnings and not self.dropped,
            "warningCount": len(self.warnings),
            "blockerCount": len(self.blockers),
            "droppedCount": len(self.dropped),
            "warnings": self.warnings,
            "blockers": self.blockers,
            "droppedItems": self.dropped,
            "preservation": "The input file is never modified. Review this report before adopting the output.",
        }
        return {"description": self.output, "report": report}


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read {path}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate a DUSRM schema 0.1 description to 0.2 draft.")
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--allow-incomplete", action="store_true",
                        help="Write a draft even when mappings are ambiguous; omitted items are listed in the report.")
    args = parser.parse_args()

    try:
        source = load_json(args.source)
        schema01 = load_json(SCHEMA_01)
        schema02 = load_json(SCHEMA_02)
        Draft202012Validator.check_schema(schema01)
        Draft202012Validator.check_schema(schema02)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    errors = list(Draft202012Validator(schema01, format_checker=FormatChecker()).iter_errors(source))
    if errors:
        for error in errors:
            print(f"SCHEMA 0.1 ERROR {list(error.absolute_path)}: {error.message}", file=sys.stderr)
        return 1

    result = Migration(source).run()
    report = result["report"]
    output = result["description"]

    structural = list(Draft202012Validator(schema02, format_checker=FormatChecker()).iter_errors(output))
    if structural:
        report["schema02StructuralErrors"] = [
            {"path": list(error.absolute_path), "message": error.message}
            for error in structural
        ]

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    if report["blockerCount"] or structural:
        if not args.allow_incomplete:
            print(f"Migration not emitted: {report['blockerCount']} blocker(s), {len(structural)} schema error(s). Report written to {args.report}.", file=sys.stderr)
            return 2
    if report["warningCount"] or report["droppedCount"]:
        if not args.allow_incomplete:
            print(f"Migration requires review: {report['warningCount']} warning(s), {report['droppedCount']} omitted item(s). Use --allow-incomplete to emit a review draft. Report written to {args.report}.", file=sys.stderr)
            return 2
    if structural:
        print("Incomplete migration output is not structurally valid; no description was written.", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    if report["complete"]:
        print(f"Migration complete: {args.output}")
        return 0
    print(f"Incomplete review draft written: {args.output}")
    print(f"Warnings: {report['warningCount']}; blockers: {report['blockerCount']}; dropped: {report['droppedCount']}.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
