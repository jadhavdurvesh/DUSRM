#!/usr/bin/env python3
"""Validate DUSRM schema structure and 0.7 fixture expectations.

This checks JSON Schema only. It does not implement DUSRM semantic, profile,
evidence, safety, or full conformance assessment.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "dusrm-description-0.1.schema.json"
FIXTURES = ROOT / "conformance" / "fixtures"


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot load {path.relative_to(ROOT)}: {exc}") from exc


def errors_for(validator, instance):
    return sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    positives = [
        "valid-minimal.json",
        "valid-multilayer-realization.json",
    ]
    structural_negatives = [
        "invalid-missing-boundary.json",
        "invalid-layer.json",
        "invalid-status-upgrade.json",
    ]
    semantic_only_negatives = [
        "invalid-duplicate-element-identifiers.json",
        "invalid-dangling-reference.json",
    ]

    failures: list[str] = []

    for name in positives:
        instance = load_json(FIXTURES / name)
        errors = errors_for(validator, instance)
        if errors:
            failures.append(f"{name}: expected schema pass, got {len(errors)} error(s)")
            for error in errors:
                failures.append(f"  {list(error.absolute_path)}: {error.message}")
        else:
            print(f"PASS schema: {name}")

    for name in structural_negatives:
        instance = load_json(FIXTURES / name)
        errors = errors_for(validator, instance)
        if not errors:
            failures.append(f"{name}: expected schema failure but document passed")
        else:
            print(f"PASS rejection: {name}")

    for name in semantic_only_negatives:
        instance = load_json(FIXTURES / name)
        errors = errors_for(validator, instance)
        if errors:
            failures.append(
                f"{name}: expected to pass structural schema so a semantic check can reject it"
            )
            for error in errors:
                failures.append(f"  {list(error.absolute_path)}: {error.message}")
        else:
            print(f"PASS schema-boundary: {name} (semantic validation remains pending)")

    if failures:
        print("\nDUSRM schema fixture validation FAILED:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("\nDUSRM JSON Schema checks passed.")
    print("Semantic validation, profile compatibility, evidence assessment, and system conformance were not evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
