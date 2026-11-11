from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from jsonschema import Draft202012Validator, FormatChecker
from validate_semantics_0_2 import validate_semantics

SCHEMA = json.loads((ROOT / "schema/dusrm-description-0.2.schema.json").read_text())
REGISTRY = json.loads((ROOT / "profiles/registry.json").read_text())
DOC = json.loads((ROOT / "schema/fixtures/0.2/profiles/sand-os-operating-system.json").read_text())
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


class SandOSProfileTests(unittest.TestCase):
    def test_profile_passes_schema_02(self):
        errors = list(VALIDATOR.iter_errors(DOC))
        self.assertEqual(
            errors, [],
            msg="; ".join(f"{list(e.absolute_path)}: {e.message}" for e in errors),
        )

    def test_profile_has_no_semantic_errors(self):
        findings = validate_semantics(DOC, REGISTRY)
        errors = [item for item in findings if item.severity == "error"]
        self.assertEqual(errors, [], msg="; ".join(item.message for item in errors))

    def test_profile_compatibility_remains_not_assessed(self):
        profile = next(
            item for item in REGISTRY["profiles"]
            if item["profileId"] == "DUSRM-PROFILE-OPERATING-SYSTEM-0.1"
        )
        self.assertEqual(profile["compatibilityStatus"], "not-assessed")
        findings = validate_semantics(DOC, REGISTRY)
        warnings = [item for item in findings if item.code == "DUSRM-02-P-001"]
        self.assertEqual(len(warnings), 1)
        self.assertEqual(warnings[0].severity, "warning")

    def test_eight_dusrm_layers_and_nine_sand_strata_are_not_conflated(self):
        self.assertEqual(
            {item["layer"] for item in DOC["layerApplicability"]},
            {f"L{i}" for i in range(1, 9)},
        )
        mapping = DOC["extensions"]["org.dmj.dusrm.profile.operating-system"]["implementationStrata"]
        self.assertEqual(len(mapping), 9)
        self.assertEqual({item["stratumId"] for item in mapping}, {f"sand-stratum-{i:02d}" for i in range(1, 10)})
        used = {layer for item in mapping for layer in item["dusrmLayers"]}
        self.assertEqual(used, {f"L{i}" for i in range(1, 9)})

    def test_runtime_independence_is_explicit(self):
        extension = DOC["extensions"]["org.dmj.dusrm.profile.operating-system"]
        self.assertIn("no kernel/runtime dependency", extension["adoptionMode"])
        decision = next(
            item for item in DOC["decisions"]
            if item["id"] == "sand-os-decision-dusrm-boundary"
        )
        self.assertIn("not linked into the boot chain", decision["statement"])

    def test_planned_subsystems_are_not_marked_implemented(self):
        for identifier in ("sand-os-networking", "sand-os-service-ipc", "sand-os-compositor"):
            element = next(item for item in DOC["elements"] if item["id"] == identifier)
            self.assertEqual(element["realizationState"], "planned")

    def test_current_security_and_filesystem_limits_are_preserved(self):
        filesystem = next(item for item in DOC["elements"] if item["id"] == "sand-os-sandfs")
        sdk = next(item for item in DOC["elements"] if item["id"] == "sand-os-sapp-sdk")
        self.assertIn("crash consistency", filesystem["description"])
        self.assertIn("trust store", sdk["description"])
        security = next(item for item in DOC["evidence"] if item["id"] == "SAND-EV-SEC")
        self.assertTrue(security["limitations"])

    def test_profile_evidence_has_exact_qemu_ci_revision(self):
        evidence = next(item for item in DOC["evidence"] if item["id"] == "SAND-EV-CI")
        self.assertEqual(evidence["revision"], "661cdedd38e2e24e202dee22798047fd7311353a")
        self.assertEqual(evidence["context"], "simulation")
        self.assertIn("QEMU", evidence["limitations"][0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
