from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATE = ROOT / "validate.py"
VERIFY = ROOT / "verify_bundle.py"
MODEL = ROOT / "sand-os-architecture.json"


class ValidationKitTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATE), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_bundle_integrity(self):
        result = subprocess.run(
            [sys.executable, str(VERIFY)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("4/4 files verified", result.stdout)

    def test_sand_os_model_passes_with_only_expected_compatibility_warning(self):
        with tempfile.TemporaryDirectory() as temp:
            report_path = Path(temp) / "report.json"
            result = self.run_cli("--report", str(report_path))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertTrue(report["summary"]["valid"])
            self.assertEqual(report["summary"]["errors"], 0)
            self.assertEqual(report["summary"]["compatibilityWarnings"], 1)
            self.assertEqual(report["target"]["compatibilityStatus"], "not-assessed")

    def test_strict_compatibility_returns_distinct_exit_code(self):
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_cli(
                "--strict-compatibility",
                "--report",
                str(Path(temp) / "report.json"),
            )
            self.assertEqual(result.returncode, 3, result.stdout + result.stderr)

    def test_dangling_element_reference_fails_semantic_validation(self):
        model = json.loads(MODEL.read_text(encoding="utf-8"))
        model["elements"] = [
            item for item in model["elements"] if item["id"] != "sand-os-memory-manager"
        ]
        with tempfile.TemporaryDirectory() as temp:
            model_path = Path(temp) / "broken.json"
            report_path = Path(temp) / "broken-report.json"
            model_path.write_text(json.dumps(model), encoding="utf-8")
            result = self.run_cli(str(model_path), "--report", str(report_path))
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("does not resolve", result.stderr)

    def test_wrong_schema_version_fails_structural_validation(self):
        model = json.loads(MODEL.read_text(encoding="utf-8"))
        model["schemaVersion"] = "999"
        with tempfile.TemporaryDirectory() as temp:
            model_path = Path(temp) / "wrong-version.json"
            model_path.write_text(json.dumps(model), encoding="utf-8")
            result = self.run_cli(str(model_path), "--report", str(Path(temp) / "report.json"))
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("SCHEMA ERROR", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
