# DUSRM 1.0 Preparation — WP7 Status

**Work package:** WP7 — Portable Validation Kit and SAND OS Adoption Review  
**Status:** Portable kit implemented and CI passed; independent review and SAND-side adoption approval pending  
**Date:** 2026-11-11

## Objective

Demonstrate that DUSRM is an authored, usable reference model with working host-side structural/semantic validation, and prepare a reproducible integration path for SAND OS without modifying the SAND OS repository or adding a kernel/runtime dependency.

## What DUSRM is — and is not

DUSRM is our own research reference model: its eight responsibility layers, ontology, relationship vocabulary, typed description schema, profile rules and semantic validation rules are maintained in this repository.

It is not an operating system, kernel, programming language, syscall ABI, wire protocol or runtime. It does not make SAND OS boot, schedule processes, manage memory or enforce security. Those are responsibilities implemented by SAND.

DUSRM is informed by and should complement existing architecture-description, systems-engineering and modeling practices. It is not an ISO/IEC or OMG standard, and its originality, completeness and compatibility remain subject to independent review.

## WP7 deliverables

- [Portable SAND OS validation kit](../../adoption/sand-os/README.md)
- [Pinned kit manifest](../../adoption/sand-os/manifest.json)
- [One-command validator and report generator](../../adoption/sand-os/validate.py)
- [Git blob integrity verifier](../../adoption/sand-os/verify_bundle.py)
- [Fourteen kit regression tests](../../adoption/sand-os/tests/test_validation_kit.py)
- [WP7 SAND CI adoption proposal](M7-SAND-CI-ADOPTION.md)
- [WP7 review checklist](M7-REVIEW-CHECKLIST.md)
- [WP7 validation record](M7-VALIDATION.md)

## Executable validation result

The dedicated [DUSRM SAND OS validation kit CI run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43032173672) passed on 2026-11-11 at commit `d7af1cc07ac69bf76b2590c8fedd11af059ab7e3`.

- Bundled source integrity: **4/4 files verified** against recorded Git blob object IDs.
- Portable-kit regression tests: **14 passed**.
- SAND OS architecture description: structurally and semantically valid.
- Semantic errors: **0**.
- Warnings: **1**, intentionally retained.
- Profile compatibility warning: **1**, because compatibility remains `not-assessed`.
- JSON validation report: generated and uploaded as a GitHub Actions artifact.

The CI run is executable evidence that the DUSRM schema/validator toolchain works on the pinned SAND OS description. It is not proof of kernel implementation correctness, physical hardware support, safety, security or profile approval.

## How the kit works

The kit is version `0.2.3-draft` and contains a pinned copy of:
- DUSRM schema 0.2-draft;
- DUSRM 0.2 semantic validator;
- profile registry;
- SAND OS architecture description.

The wrapper runs the schema/semantic checks, records SHA-256 hashes of its inputs and emits a JSON report. The integrity verifier confirms that the bundled schema, validator, registry and architecture description match their recorded Git blob IDs.

The kit is host-side and self-contained. It does not fetch code at validation time.

## SAND OS boundary

SAND OS (`jadhavdurvesh/sand-os`) remains unchanged. Its main tree still matches the read-only inspection snapshot `661cdedd38e2e24e202dee22798047fd7311353a`.

No SAND OS branch, file, commit, workflow, build configuration or release was created, modified or deleted. The CI integration is only proposed in [M7-SAND-CI-ADOPTION.md](M7-SAND-CI-ADOPTION.md).

## Compatibility and review status

The operating-system profile remains `not-assessed`. A successful validator run is not a compatibility approval. The OS-profile semantic rules now require complete domain coverage, resolvable element/evidence references, all eight mapped layers, context-appropriate test evidence and consistent implementation maturity. The known SAND documentation questions in [WP6 review findings](M6-REVIEW-FINDINGS.md) remain open.

## Exit criteria

WP7 is not complete until:
1. an independent reviewer assesses DUSRM's core ontology, eight responsibility layers, relationship semantics and schema;
2. the reviewer checks whether the semantic validator's implemented subset is sufficient and accurately scoped;
3. SAND OS ownership reviews the mapping and open documentation questions;
4. the OS profile receives an explicit compatibility disposition;
5. separate explicit authorization is obtained before any SAND OS repository change.

WP8 now proposes DUSRM as SAND's primary project-level responsibility architecture; see [WP8 governance](M8-SAND-OS-ARCHITECTURE-GOVERNANCE.md). Until the owner approves adoption and independent review is complete, the portable kit remains an experimental DUSRM-side tool and no SAND CI changes are made.


## Latest canonical regression runs

The schema 0.2 workflow [run #43031844187](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031844187) passed 31 semantic/migration tests, 4 existing profile tests and 8 SAND OS profile tests. The legacy [0.8 run #43031844011](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031844011) and [0.9 run #43031843986](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031843986) each passed 55 tests.

WP8 proposes using DUSRM as the primary system-wide SAND OS responsibility architecture. See [WP8 status](M8-STATUS.md) and [governance policy](M8-SAND-OS-ARCHITECTURE-GOVERNANCE.md).
