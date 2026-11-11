#!/usr/bin/env python3
"""Verify bundled artifacts against their recorded Git blob object IDs."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest.json"


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def verify() -> list[dict[str, str]]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    results: list[dict[str, str]] = []
    for entry in manifest["files"]:
        path = ROOT / entry["path"]
        if not path.is_file():
            results.append({"path": entry["path"], "status": "missing"})
            continue
        actual = git_blob_sha1(path.read_bytes())
        expected = entry["gitBlobSha"]
        results.append({
            "path": entry["path"],
            "status": "ok" if actual == expected else "mismatch",
            "expected": expected,
            "actual": actual,
        })
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify DUSRM SAND OS kit integrity.")
    parser.add_argument("--json", action="store_true", help="Print results as JSON.")
    args = parser.parse_args()
    try:
        results = verify()
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"Bundle verification failed: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for item in results:
            print(f"{item['status'].upper():8} {item['path']}")
    failures = [item for item in results if item["status"] != "ok"]
    print(f"\\nBundle integrity: {len(results) - len(failures)}/{len(results)} files verified.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
