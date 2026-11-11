#!/usr/bin/env python3
"""Run the bundled DUSRM 0.2 structural and semantic validation."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SCHEMA = ROOT / "dusrm-description-0.2.schema.json"
REGISTRY = ROOT / "profile-registry.json"
VALIDATOR = ROOT / "validate_semantics_0_2.py"
DEFAULT_MODEL = ROOT / "sand-os-architecture.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a SAND OS DUSRM architecture description."
    )
    parser.add_argument("model", nargs="?", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--report", type=Path, default=Path("dusrm-validation-report.json"))
    parser.add_argument(
        "--strict-compatibility",
        action="store_true",
        help="Return exit code 3 while any profile-compatibility warning remains.",
    )
    args = parser.parse_args()

    for required in (SCHEMA, REGISTRY, VALIDATOR, args.model):
        if not required.is_file():
            print(f"Required file not found: {required}", file=sys.stderr)
            return 2

    command = [
        sys.executable, str(VALIDATOR), str(args.model),
        "--schema", str(SCHEMA), "--registry", str(REGISTRY), "--json",
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        if completed.stdout:
            print(completed.stdout, end="", file=sys.stderr)
        if completed.stderr:
            print(completed.stderr, end="", file=sys.stderr)
        return completed.returncode

    try:
        payload = completed.stdout.lstrip()
        findings, _ = json.JSONDecoder().raw_decode(payload)
        model: dict[str, Any] = json.loads(args.model.read_text(encoding="utf-8"))
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot assemble validation report: {exc}", file=sys.stderr)
        return 2

    counts = Counter(item.get("severity", "unknown") for item in findings)
    compatibility_findings = [
        item for item in findings if item.get("code") == "DUSRM-02-P-001"
    ]
    errors = counts.get("error", 0)
    warnings = counts.get("warning", 0)
    report = {
        "reportVersion": "1.0",
        "tool": manifest["kitId"],
        "toolVersion": manifest["kitVersion"],
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "target": {
            "repository": manifest["targetRepository"],
            "revision": manifest["targetRevision"],
            "descriptionId": model.get("descriptionId"),
            "title": model.get("title"),
            "schemaVersion": model.get("schemaVersion"),
            "dusrmVersion": model.get("dusrmVersion"),
            "profileRefs": model.get("profileRefs", []),
            "compatibilityStatus": manifest["compatibilityStatus"],
        },
        "inputs": {
            "modelSha256": sha256(args.model),
            "schemaSha256": sha256(SCHEMA),
            "registrySha256": sha256(REGISTRY),
            "validatorSha256": sha256(VALIDATOR),
        },
        "summary": {
            "valid": errors == 0,
            "errors": errors,
            "warnings": warnings,
            "compatibilityWarnings": len(compatibility_findings),
            "findingCount": len(findings),
        },
        "findings": findings,
        "limitations": manifest["limitations"],
    }

    try:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"Cannot write report {args.report}: {exc}", file=sys.stderr)
        return 2

    print(f"DUSRM description: {model.get('descriptionId', '<unknown>')}")
    print(f"Schema: {model.get('schemaVersion', '<unknown>')}")
    print(f"Result: {'VALID' if errors == 0 else 'INVALID'}")
    print(f"Semantic errors: {errors}")
    print(f"Warnings: {warnings}")
    print(f"Profile compatibility warnings: {len(compatibility_findings)}")
    print(f"Report: {args.report}")
    if compatibility_findings:
        print("NOTE: profile compatibility is not approved; warning intentionally retained.")
    if errors:
        return 1
    if args.strict_compatibility and compatibility_findings:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
