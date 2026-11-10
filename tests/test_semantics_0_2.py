from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from jsonschema import Draft202012Validator, FormatChecker
from validate_semantics_0_2 import validate_semantics
from migrate_schema_0_1_to_0_2 import Migration

SCHEMA_02 = json.loads((ROOT / "schema/dusrm-description-0.2.schema.json").read_text())
REGISTRY = json.loads((ROOT / "profiles/registry.json").read_text())


def fixture(name: str) -> dict:
    return json.loads((ROOT / "schema/fixtures/0.2" / name).read_text())


def codes(findings):
    return {item.code for item in findings}


class SemanticValidator02Tests(unittest.TestCase):
    def setUp(self):
        self.validator = Draft202012Validator(SCHEMA_02, format_checker=FormatChecker())

    def test_minimal_fixture_has_no_semantic_findings(self):
        doc = fixture("valid-minimal.json")
        self.assertEqual(list(self.validator.iter_errors(doc)), [])
        self.assertEqual(validate_semantics(doc, REGISTRY), [])

    def test_sand_os_fixture_has_no_semantic_errors(self):
        doc = fixture("valid-sand-os-architecture.json")
        self.assertEqual(list(self.validator.iter_errors(doc)), [])
        findings = validate_semantics(doc, REGISTRY)
        self.assertEqual([f for f in findings if f.severity == "error"], [])

    def test_dangling_typed_relationship_reference_is_rejected(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["relationships"][0]["target"]["id"] = "missing-system"
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-002", codes(findings))

    def test_duplicate_identifier_across_object_kinds_is_rejected(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["resources"][0]["id"] = "kernel"
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-001", codes(findings))

    def test_wrong_relationship_endpoint_kind_is_rejected(self):
        doc = fixture("valid-sand-os-architecture.json")
        relation = next(x for x in doc["relationships"] if x["type"] == "performs")
        relation["source"] = {"kind": "element", "id": "scheduler"}
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-003", codes(findings))

    def test_duplicate_relationship_identifier_is_rejected(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["relationships"][0]["id"] = "kernel"
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-001", codes(findings))

    def test_dangling_realization_evidence_reference_is_rejected(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["realizations"][0]["evidenceRefs"] = ["EV-MISSING"]
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-010", codes(findings))

    def test_dangling_layer_applicability_evidence_reference_is_rejected(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["layerApplicability"][0]["evidenceRefs"] = ["EV-MISSING"]
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-010", codes(findings))

    def test_duplicate_realization_pair_is_rejected(self):
        doc = fixture("valid-sand-os-architecture.json")
        duplicate = copy.deepcopy(doc["realizations"][0])
        duplicate["id"] = "REAL-DUPLICATE"
        doc["realizations"].append(duplicate)
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-012", codes(findings))

    def test_responsibility_cannot_be_allocated_to_not_applicable_layer(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["layerApplicability"][2]["applicability"] = "notApplicable"
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-014", codes(findings))

    def test_state_value_must_be_in_variable_domain(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["states"][0]["value"] = "impossible"
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-018", codes(findings))

    def test_transition_states_must_share_state_variable(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["states"].append({
            "id": "STATE-OTHER",
            "stateVariableRef": {"kind": "stateVariable", "id": "SV-OTHER"},
            "value": "other",
            "meaning": "Test state."
        })
        doc["stateVariables"].append({
            "id": "SV-OTHER",
            "subjectRef": {"kind": "element", "id": "process-manager"},
            "name": "otherState",
            "meaning": "A second independent state variable.",
            "valueType": "string"
        })
        transition = doc["transitions"][0]
        transition["toStateRef"] = {"kind": "state", "id": "STATE-OTHER"}
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-019", codes(findings))

    def test_allocation_cannot_exceed_declared_capacity(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["allocations"][0]["quantity"] = 5000
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-022", codes(findings))

    def test_interaction_roles_must_match_declared_interface(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["interactions"][0]["participantRoles"][0]["role"] = "unlisted-role"
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-M-020", codes(findings))

    def test_passing_assessment_requires_supporting_evidence(self):
        doc = fixture("valid-sand-os-architecture.json")
        doc["invariants"][0]["assessmentResult"] = "pass"
        doc["evidence"].append({
            "id": "EV-NON-SUPPORTING",
            "kind": "assumption",
            "method": "other",
            "context": "other",
            "relation": "inconclusive",
            "description": "An intentionally non-supporting evidence record for regression testing.",
            "limitations": ["Does not support the invariant."]
        })
        doc["invariants"][0]["evidenceRefs"] = ["EV-NON-SUPPORTING"]
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-E-002", codes(findings))

    def test_unassessed_profile_is_not_silently_accepted(self):
        doc = fixture("valid-minimal.json")
        doc["profileRefs"] = [{"profileId": "DUSRM-PROFILE-DBMS-0.1", "version": "0.1-draft"}]
        findings = validate_semantics(doc, REGISTRY)
        self.assertIn("DUSRM-02-P-001", codes(findings))


class Migration02Tests(unittest.TestCase):
    def test_minimal_01_description_becomes_review_draft(self):
        source = json.loads((ROOT / "conformance/fixtures/valid-minimal.json").read_text())
        result = Migration(source).run()
        output = result["description"]
        self.assertEqual(output["schemaVersion"], "0.2-draft")
        self.assertTrue(result["report"]["warningCount"] > 0)
        self.assertEqual(list(Draft202012Validator(SCHEMA_02, format_checker=FormatChecker()).iter_errors(output)), [])

    def test_external_legacy_element_moves_to_environment(self):
        source = json.loads((ROOT / "conformance/fixtures/valid-minimal.json").read_text())
        source["elements"].append({
            "id": "external-clock",
            "name": "External Clock",
            "kind": "service",
            "status": "proposed",
            "external": True,
        })
        source["relationships"].append({
            "id": "REL-EXTERNAL-CLOCK",
            "type": "dependsOn",
            "sourceRef": "app-process",
            "targetRef": "external-clock",
            "status": "proposed",
            "rationale": "The application depends on an external clock service.",
        })
        result = Migration(source).run()
        output = result["description"]
        self.assertNotIn("external-clock", {item["id"] for item in output["elements"]})
        self.assertIn("external-clock", {item["id"] for item in output["context"]["environment"]})
        relation = next(x for x in output["relationships"] if x["id"] == "REL-EXTERNAL-CLOCK")
        self.assertEqual(relation["target"], {
            "kind": "environmentParticipant", "id": "external-clock"
        })
        self.assertEqual(list(Draft202012Validator(
            SCHEMA_02, format_checker=FormatChecker()
        ).iter_errors(output)), [])

    def test_legacy_verified_status_is_not_promoted(self):
        source = json.loads((ROOT / "conformance/fixtures/valid-minimal.json").read_text())
        source["elements"][0]["status"] = "verified"
        result = Migration(source).run()
        migrated = next(x for x in result["description"]["elements"] if x["id"] == "app-process")
        self.assertEqual(migrated["realizationState"], "unknown")
        self.assertTrue(any("verified" in item["message"] for item in result["report"]["warnings"]))

    def test_ambiguous_performs_endpoint_is_reported_not_guessed(self):
        source = json.loads((ROOT / "conformance/fixtures/valid-minimal.json").read_text())
        source["relationships"].append({
            "id": "REL-OLD-PERFORMS",
            "type": "performs",
            "sourceRef": "app-process",
            "targetRef": "app-process",
            "status": "proposed",
            "rationale": "Deliberately ambiguous legacy example."
        })
        result = Migration(source).run()
        self.assertGreater(result["report"]["blockerCount"], 0)
        self.assertTrue(any("REL-OLD-PERFORMS" in item["path"] or "relationships[" in item["path"]
                            for item in result["report"]["blockers"]))
        self.assertFalse(any(x.get("type") == "performs" for x in result["description"]["relationships"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
