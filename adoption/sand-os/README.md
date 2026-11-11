# DUSRM SAND OS Validation Kit

**Kit:** DUSRM-SAND-OS-VALIDATION-KIT 0.2.3-draft  
**Status:** Experimental, host-side architecture-description validation  
**Canonical source:** [jadhavdurvesh/DUSRM](https://github.com/jadhavdurvesh/DUSRM)  
**Target architecture:** [jadhavdurvesh/sand-os](https://github.com/jadhavdurvesh/sand-os)

**Latest completed validation:** [DUSRM SAND OS kit CI passed](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43032761981) on 2026-11-11. Four bundled files verified, 14 tests passed, all 16 required OS domains covered, all eight DUSRM layers mapped, zero semantic errors and one expected profile compatibility warning.

## What this actually is

This is a portable, executable copy of the DUSRM schema 0.2 draft, semantic validator, profile registry and SAND OS architecture description.

It can:
- check a DUSRM description against JSON Schema Draft 2020-12;
- resolve typed references and run cross-record consistency checks;
- enforce operating-system profile coverage, layer-map completeness and maturity/evidence consistency;
- keep profile compatibility warnings visible;
- produce a JSON validation report with input hashes;
- verify that bundled files still match the exact Git blob objects recorded in `manifest.json`.

It does **not** boot an operating system, modify kernel behavior, provide syscalls, verify machine code, certify security, or replace SAND's build/QEMU tests.

## Run

Requires Python 3.10+ and the pinned dependency in `requirements.txt`.

From this directory:

```bash
python -m pip install -r requirements.txt
python verify_bundle.py
python validate.py
```

The default run validates `sand-os-architecture.json`, prints a summary, and creates `dusrm-validation-report.json` in the current working directory.

Expected initial outcome:
- structural schema: pass;
- semantic errors: 0;
- warnings: 1;
- warning: `DUSRM-02-P-001` because OS profile compatibility is still `not-assessed`;
- exit code: 0.

Use `--strict-compatibility` to return exit code 3 until the profile is formally assessed. Schema/semantic errors return non-zero.

Validate another DUSRM description:

```bash
python validate.py path/to/system-description.json --report out/report.json
```

Run self-tests:

```bash
python -m unittest discover -s tests -v
```

## Machine-readable report

The report records:
- target repository/revision and description identity;
- schema, registry, validator and model SHA-256 digests;
- error/warning counts and complete findings;
- required versus covered OS domains, unmapped layers and coverage completeness;
- explicit profile compatibility status;
- limitations attached to the kit.

Treat the report as architecture-validation evidence only. Preserve it alongside the CI job artifacts if adopted.

## Bundle pinning and updates

`manifest.json` records the canonical DUSRM source commit, original source paths and Git blob object IDs for each bundled artifact.

Before using this kit in another repository, run `python verify_bundle.py`. If an artifact changes, the integrity check fails. Update the copy and manifest together from a reviewed DUSRM commit; do not hand-edit the bundled schema or validator.

This kit is a snapshot, not a self-updating network client. It does not fetch code during validation.

## Proposed use in SAND OS CI — not yet installed there

See the [WP7 SAND CI adoption proposal](../../specification/DUSRM-1.0/M7-SAND-CI-ADOPTION.md) and [independent review checklist](../../specification/DUSRM-1.0/M7-REVIEW-CHECKLIST.md).

After separate approval, a SAND host-side CI job may:
1. install the pinned Python dependency;
2. run bundle integrity verification;
3. run the profile validator;
4. upload the JSON report as a workflow artifact.

It must not run inside QEMU or the guest OS, alter the disk image, add kernel objects, generate headers, or make the SAND boot path depend on DUSRM.

## OS profile coverage

The current fixture represents 16 required operating-system domains and maps nine SAND implementation strata onto all eight DUSRM layers. The validator requires internal domains to reference SAND elements, applicable domains to reference evidence, and test maturity claims to be backed by context-appropriate evidence. A planned user-mode runtime is modeled separately from the current SAPP SDK.

## Compatibility and maturity

The operating-system profile is `DUSRM-PROFILE-OPERATING-SYSTEM-0.1`; its compatibility status is `not-assessed`. Passing the validator is not profile approval.

SAND OS source revision and QEMU evidence are pinned in `manifest.json`. QEMU success remains emulator-scoped, not physical hardware verification.

## Contents

- `validate.py` — one-command validator and JSON report generator.
- `validate_semantics_0_2.py` — bundled DUSRM semantic checker.
- `dusrm-description-0.2.schema.json` — pinned structural schema.
- `profile-registry.json` — pinned profile registry.
- `sand-os-architecture.json` — SAND OS architecture fixture.
- `verify_bundle.py` — Git blob integrity verifier.
- `tests/` — positive, negative, domain-coverage, maturity and policy-behavior tests.
- [Architecture change-review template](CHANGE-REVIEW-TEMPLATE.md) — DUSRM-based SAND architecture review.
- `manifest.json` — source revision and artifact pins.
