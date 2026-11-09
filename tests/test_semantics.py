"""Unit tests for the DUSRM 0.8 semantic validator."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.validate_semantics import validate_semantics

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "conformance" / "fixtures"
REGISTRY = json.loads((ROOT / "profiles" / "registry.json").read_text(encoding="utf-8"))


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class SemanticValidatorTests(unittest.TestCase):
    def codes(self, document: dict) -> set[str]:
        return {finding.code for finding in validate_semantics(document, REGISTRY)}

    def errors(self, document: dict):
        return [f for f in validate_semantics(document, REGISTRY) if f.severity == "error"]

    def test_minimal_fixture_has_no_semantic_errors(self):
        self.assertEqual(self.errors(load_fixture("valid-minimal.json")), [])

    def test_one_element_can_realize_multiple_layers(self):
        document = load_fixture("valid-multilayer-realization.json")
        findings = validate_semantics(document, REGISTRY)
        self.assertNotIn("DUSRM-M-005", {f.code for f in findings})
        self.assertEqual(self.errors(document), [])
        layers = {
            r["primaryLayer"] for r in document["responsibilities"]
            if any(
                x["elementRef"] == "engine-process" and x["responsibilityRef"] == r["id"]
                for x in document["realizations"]
            )
        }
        self.assertEqual(layers, {"L3", "L4", "L5"})

    def test_duplicate_element_identifier_is_rejected(self):
        self.assertIn("DUSRM-M-001", self.codes(load_fixture("invalid-duplicate-element-identifiers.json")))

    def test_dangling_realization_reference_is_rejected(self):
        self.assertIn("DUSRM-M-003", self.codes(load_fixture("invalid-dangling-reference.json")))

    def test_registry_profile_not_assessed_is_not_compatible(self):
        document = load_fixture("valid-minimal.json")
        document["profileRefs"] = [{
            "profileId": "DUSRM-PROFILE-SWAPP-0.1",
            "version": "0.1-draft"
        }]
        self.assertIn("DUSRM-P-001", self.codes(document))

    def test_transition_value_must_belong_to_state_domain(self):
        document = load_fixture("valid-minimal.json")
        document["transitions"][0]["to"] = "paused"
        self.assertIn("DUSRM-M-015", self.codes(document))

    def test_verified_claim_requires_adequate_evidence(self):
        document = load_fixture("valid-minimal.json")
        document["invariants"] = [{
            "id": "INV-1",
            "statement": "A completed task was authorized.",
            "status": "verified",
            "evidenceRefs": [],
            "assumptions": []
        }]
        self.assertIn("DUSRM-E-001", self.codes(document))

    def test_duplicate_realization_pair_is_rejected(self):
        document = load_fixture("valid-minimal.json")
        duplicate = dict(document["realizations"][0])
        duplicate["id"] = "REAL-DUPLICATE"
        document["realizations"].append(duplicate)
        self.assertIn("DUSRM-M-013", self.codes(document))

    def test_extension_keys_must_be_namespaced(self):
        document = load_fixture("valid-minimal.json")
        document["extensions"] = {"unqualified": {"feature": True}}
        self.assertIn("DUSRM-P-002", self.codes(document))

    def test_interacts_with_allows_external_environment_participant(self):
        document = load_fixture("valid-minimal.json")
        document["relationships"].append({
            "id": "REL-USER",
            "type": "interactsWith",
            "sourceRef": "task-ui",
            "targetRef": "user",
            "status": "proposed",
            "rationale": "The interface interacts with an external user."
        })
        self.assertNotIn("DUSRM-M-006", self.codes(document))
        self.assertNotIn("DUSRM-M-002", self.codes(document))

    def test_controls_rejects_environment_as_target(self):
        document = load_fixture("valid-minimal.json")
        document["relationships"].append({
            "id": "REL-INVALID-CONTROL",
            "type": "controls",
            "sourceRef": "task-ui",
            "targetRef": "user",
            "status": "proposed",
            "rationale": "Invalidly models the user as a controlled component."
        })
        self.assertIn("DUSRM-M-006", self.codes(document))

    def test_unsupported_relationship_signature_is_warning(self):
        document = load_fixture("valid-minimal.json")
        document["relationships"].append({
            "id": "REL-UNSPECIFIED",
            "type": "performs",
            "sourceRef": "app-process",
            "targetRef": "task-ui",
            "status": "proposed",
            "rationale": "The current core draft has not assigned a participant signature to performs."
        })
        findings = validate_semantics(document, REGISTRY)
        matching = [f for f in findings if f.code == "DUSRM-M-016"]
        self.assertTrue(matching)
        self.assertTrue(all(f.severity == "warning" for f in matching))

    def test_interacts_with_allows_external_environment_participant(self):
        document = load_fixture("valid-minimal.json")
        document["relationships"].append({
            "id": "REL-USER",
            "type": "interactsWith",
            "sourceRef": "task-ui",
            "targetRef": "user",
            "status": "proposed",
            "rationale": "The task interface interacts with the external user."
        })
        self.assertNotIn("DUSRM-M-006", self.codes(document))
        self.assertNotIn("DUSRM-M-002", self.codes(document))

    def test_controls_rejects_environment_as_target(self):
        document = load_fixture("valid-minimal.json")
        document["relationships"].append({
            "id": "REL-INVALID-CONTROL",
            "type": "controls",
            "sourceRef": "task-ui",
            "targetRef": "user",
            "status": "proposed",
            "rationale": "This invalid example treats the external user as a controlled element."
        })
        self.assertIn("DUSRM-M-006", self.codes(document))

    def test_unsupported_relationship_signature_is_warning(self):
        document = load_fixture("valid-minimal.json")
        document["relationships"].append({
            "id": "REL-UNSPECIFIED",
            "type": "performs",
            "sourceRef": "app-process",
            "targetRef": "task-ui",
            "status": "proposed",
            "rationale": "The current core draft has not assigned a participant signature to performs."
        })
        findings = validate_semantics(document, REGISTRY)
        self.assertIn("DUSRM-M-016", {f.code for f in findings})
        self.assertEqual([f for f in findings if f.code == "DUSRM-M-016"][0].severity, "warning")



if __name__ == "__main__":
    unittest.main(verbosity=2)
