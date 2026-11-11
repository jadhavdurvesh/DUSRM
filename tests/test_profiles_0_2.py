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
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())

PROFILE_FIXTURES = (
    "standalone-application.json",
    "ananta-database-engine.json",
    "firebot-cyber-physical-robotics.json",
)


def load_fixture(name: str) -> dict:
    path = ROOT / "schema/fixtures/0.2/profiles" / name
    return json.loads(path.read_text(encoding="utf-8"))


class ProfileSchema02Tests(unittest.TestCase):
    def test_each_profile_fixture_passes_structural_schema(self):
        for name in PROFILE_FIXTURES:
            with self.subTest(profile=name):
                doc = load_fixture(name)
                errors = list(VALIDATOR.iter_errors(doc))
                self.assertEqual(
                    errors, [],
                    msg="; ".join(f"{list(e.absolute_path)}: {e.message}" for e in errors),
                )

    def test_each_profile_fixture_has_no_semantic_errors(self):
        for name in PROFILE_FIXTURES:
            with self.subTest(profile=name):
                doc = load_fixture(name)
                findings = validate_semantics(doc, REGISTRY)
                errors = [item for item in findings if item.severity == "error"]
                self.assertEqual(errors, [], msg="; ".join(item.message for item in errors))

    def test_profile_compatibility_is_not_silently_approved(self):
        for name in PROFILE_FIXTURES:
            with self.subTest(profile=name):
                doc = load_fixture(name)
                findings = validate_semantics(doc, REGISTRY)
                warnings = [item for item in findings if item.code == "DUSRM-02-P-001"]
                self.assertEqual(len(warnings), 1)
                self.assertEqual(warnings[0].severity, "warning")

    def test_profile_registry_targets_schema_0_2_without_claiming_compatibility(self):
        self.assertEqual(REGISTRY["coreVersion"], "1.0-preparation")
        self.assertEqual(REGISTRY["assessmentTarget"]["schemaVersion"], "0.2-draft")
        for profile in REGISTRY["profiles"]:
            with self.subTest(profile=profile["profileId"]):
                self.assertEqual(profile["candidateCoreVersion"], "1.0-preparation")
                self.assertEqual(profile["candidateSchemaVersion"], "0.2-draft")
                self.assertEqual(profile["compatibilityStatus"], "not-assessed")
                self.assertEqual(profile["reconciliationStatus"], "review-prepared")


if __name__ == "__main__":
    unittest.main(verbosity=2)
