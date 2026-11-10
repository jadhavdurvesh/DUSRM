#!/usr/bin/env python3
"""Validate the DUSRM 0.2-draft JSON Schema and its isolated fixture suite.

This is structural validation, including relationship endpoint-kind rules.
It does not resolve IDs across collections or assess semantic conformance.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "dusrm-description-0.2.schema.json"
FIXTURE_DIR = ROOT / "schema" / "fixtures" / "0.2"

POSITIVE_FIXTURES = (
    "valid-minimal.json",
    "valid-sand-os-architecture.json",
)
NEGATIVE_FIXTURES = (
    "invalid-wrong-typed-endpoint.json",
    "invalid-legacy-status-field.json",
)


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot load {path.relative_to(ROOT)}: {exc}") from exc


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    failures: list[str] = []

    for name in POSITIVE_FIXTURES:
        path = FIXTURE_DIR / name
        document = load_json(path)
        errors = sorted(
            validator.iter_errors(document),
            key=lambda error: (list(error.absolute_path), error.message),
        )
        if errors:
            failures.append(f"{name}: expected schema pass, got {len(errors)} error(s)")
            failures.extend(
                f"  {list(error.absolute_path)}: {error.message}"
                for error in errors
            )
        else:
            print(f"PASS schema: {name}")

    for name in NEGATIVE_FIXTURES:
        path = FIXTURE_DIR / name
        document = load_json(path)
        errors = sorted(
            validator.iter_errors(document),
            key=lambda error: (list(error.absolute_path), error.message),
        )
        if not errors:
            failures.append(f"{name}: expected schema rejection but document passed")
        else:
            print(f"PASS rejection: {name}")
            for error in errors:
                print(f"  {list(error.absolute_path)}: {error.message}")

    if failures:
        print("\nDUSRM schema 0.2 fixture validation FAILED:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("\nDUSRM schema 0.2 structural and typed-endpoint fixture checks passed.")
    print("Cross-reference resolution, semantic consistency, profile compatibility,")
    print("evidence adequacy, and overall system conformance were not assessed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
