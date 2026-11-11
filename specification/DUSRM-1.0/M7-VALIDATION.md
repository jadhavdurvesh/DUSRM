# DUSRM 1.0 Preparation — WP7 Portable Kit Validation

**Workflow:** DUSRM SAND OS validation kit  
**Run:** [GitHub Actions run #43026965428](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43026965428)  
**Conclusion:** success  
**Checked commit:** `3b36bd93879ae9a0d757bad9dd5f44d47e58a364)  
**Date:** 2026-11-11

## Results

| Check | Result |
|---|---|
| Pinned bundle integrity | 4/4 files verified |
| Portable validation-kit regression tests | 5 passed |
| Default SAND OS description validation | valid |
| Structural schema errors | 0 |
| Semantic errors | 0 |
| Semantic warnings | 1 |
| Profile compatibility warnings | 1 expected |
| JSON report generation | passed |
| Report artifact upload | passed |

## Regression cases

The five tests exercise:
1. Git blob hash verification for the bundled validator, schema, registry and architecture fixture.
2. Positive SAND OS architecture validation with the expected warning and machine-readable report.
3. Strict compatibility mode returning exit code 3 while profile compatibility is not assessed.
4. Rejection of a semantically invalid description with a dangling element reference.
5. Rejection of an invalid schema version.

## Expected warning

`DUSRM-02-P-001`: the operating-system profile is not explicitly approved as compatible in the profile registry.

The warning is deliberately non-fatal in the default mode. Use `--strict-compatibility` to make it fail with exit code 3 until an explicit compatibility assessment is recorded. Structural or semantic errors fail with a non-zero exit code.

## CI report artifact

The workflow uploaded `dusrm-sand-os-architecture-report` as an artifact. It contains the generated JSON report, including:
- target repository revision and description identity;
- schema, registry, validator and model SHA-256 digests;
- error/warning counts and full semantic findings;
- compatibility state and validation limitations.

The artifact is attached to the [workflow run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43026965428).

## Scope

The result demonstrates that the DUSRM schema and selected semantic rules can be run reproducibly against the SAND OS architecture description. It does not test SAND OS kernel code, create a boot image, execute the OS, verify physical hardware, audit security, or approve profile compatibility.
