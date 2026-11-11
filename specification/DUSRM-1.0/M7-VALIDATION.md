# DUSRM 1.0 Preparation — WP7 Portable Kit Validation

**Workflow:** DUSRM SAND OS validation kit  
**Run:** [GitHub Actions run #43031919228](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031919228)  
**Conclusion:** success  
**Checked commit:** `a83bb0107c29939d85246f69566600a857b8c36a`  
**Date:** 2026-11-11

## Results

| Check | Result |
|---|---|
| Pinned bundle integrity | 4/4 files verified |
| Portable validation-kit regression tests | 14 passed |
| Default SAND OS description validation | valid |
| Structural schema errors | 0 |
| Semantic errors | 0 |
| Semantic warnings | 1 |
| Profile compatibility warnings | 1 expected |
| Required OS domain coverage | 16/16 |\n| DUSRM layers represented in OS mapping | 8/8 |\n| JSON report generation | passed |
| Report artifact upload | passed |

## Regression cases

The fourteen tests exercise:
1. Git blob hash verification for the bundled validator, schema, registry and architecture fixture.
2. Positive SAND OS architecture validation with a complete 16-domain coverage report.
3. Strict compatibility mode returning exit code 3 while profile compatibility is not assessed.
4. Rejection of dangling element/evidence references and missing required domain coverage.
5. Rejection of an invalid schema version and invalid layer mapping.
6. Rejection of QEMU evidence relabeled as physical hardware testing.
7. Rejection of DUSRM being marked as a required SAND runtime dependency.
8. Rejection of implemented maturity claims that point to in-progress elements.
9. Verification that all eight DUSRM layers remain present in the many-to-many OS mapping.
10. Malformed extension values are reported as validation findings rather than crashing the validator.

## Expected warning

`DUSRM-02-P-001`: the operating-system profile is not explicitly approved as compatible in the profile registry.

The warning is deliberately non-fatal in the default mode. Use `--strict-compatibility` to make it fail with exit code 3 until an explicit compatibility assessment is recorded. Structural or semantic errors fail with a non-zero exit code.

## CI report artifact

The workflow uploaded `dusrm-sand-os-architecture-report` as an artifact. It contains the generated JSON report, including:
- target repository revision and description identity;
- schema, registry, validator and model SHA-256 digests;
- error/warning counts and full semantic findings;
- compatibility state and validation limitations.

The artifact [dusrm-sand-os-architecture-report](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031919228/artifacts/13860938644) is attached to the successful workflow run.

## Scope

The result demonstrates that the DUSRM schema and OS-profile rules can be run reproducibly against the SAND OS architecture description. It includes machine-checked 16/16 OS-domain coverage and all-eight-layer mapping. It does not test SAND OS kernel code, create a boot image, execute the OS, verify physical hardware, audit security, or approve profile compatibility.


## Canonical DUSRM regression suite

The canonical schema 0.2 [CI run #43031844187](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031844187) passed 31 semantic/migration tests, 4 existing domain-profile tests and 8 SAND OS profile tests. The legacy [0.8](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031844011) and [0.9](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031843986) workflows each passed 55 tests.
