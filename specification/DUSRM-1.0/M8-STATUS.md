# DUSRM 1.0 Preparation — WP8 Status

**Work package:** WP8 — DUSRM as the Primary SAND OS Architecture Reference  
**Status:** Governance model and machine-checkable OS profile prepared; SAND-side adoption pending separate authorization  
**Date:** 2026-11-11

## Objective

Make DUSRM the primary project-level reference for SAND OS responsibility allocation, subsystem relationships, cross-layer concerns, maturity and evidence—replacing inconsistent project-wide layer diagrams and informal responsibility maps.

DUSRM does not replace SAND-owned technical contracts, code, tests or hardware architecture specifications. It governs the cross-subsystem architecture view.

## Deliverables

- [SAND OS architecture governance policy](M8-SAND-OS-ARCHITECTURE-GOVERNANCE.md)
- [SAND architecture change-review template](../../adoption/sand-os/CHANGE-REVIEW-TEMPLATE.md)
- [Operating-system profile](../../profiles/operating-system/PROFILE.md)
- [Machine-checkable SAND OS description](../../schema/fixtures/0.2/profiles/sand-os-operating-system.json)
- [Portable validation kit](../../adoption/sand-os/README.md)

## Current profile coverage

The SAND OS fixture now contains:
- **17 modeled elements**, including a separate planned user-mode runtime;
- **8 DUSRM core responsibilities**, one primary responsibility per core layer;
- **16 required OS domains**, each with a coverage declaration;
- **9 SAND implementation strata** mapped many-to-many to all eight DUSRM layers;
- typed relationships, operations, states, interfaces, resources, capabilities, requirements, constraints, invariants and evidence.

The semantic validator enforces:
- unique coverage per required OS domain;
- no missing required domains;
- resolvable internal element references and evidence references;
- rationale for not-applicable domains;
- all eight core DUSRM layers appearing in the OS mapping;
- evidence-context rules for simulation, physical testing, independent review and verification;
- maturity consistency between an OS domain and its realizing elements;
- an explicit boundary preventing DUSRM from becoming a kernel/runtime dependency.

## Executable validation

The portable kit includes:
- pinned DUSRM 0.2-draft schema;
- semantic validator with OS profile rules;
- profile registry and SAND OS architecture description;
- bundle integrity verifier;
- JSON validation report with domain coverage and input hashes;
- positive and negative regression tests.

The latest portable-kit CI run is [run #43031919228](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031919228). It passed 4/4 bundle-integrity checks and 14 portable-kit tests. The canonical schema 0.2 [run #43031844187](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031844187) passed 31 semantic/migration tests, 4 existing profile tests and 8 SAND OS profile tests. The legacy 0.8 and 0.9 suites each passed 55 tests. The canonical schema/semantic workflow [run #43031844187](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031844187) also passed after the final negative-test correction. The 0.8 [run #43031844011](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031844011) and 0.9 [run #43031843986](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031843986) each passed 55 tests.

## Proposed project rule

DUSRM should be the authoritative cross-subsystem responsibility map for SAND. For architecture-affecting changes, update the DUSRM description, run validation, update affected technical specifications, implement, test and then attach evidence. Pure refactors with no architecture impact may be recorded as no-model-change.

The proposed [governance policy](M8-SAND-OS-ARCHITECTURE-GOVERNANCE.md) distinguishes DUSRM's system-wide responsibility reference from SAND-specific technical contracts such as Veyra, SAPP and SANDFS.

## Repository boundary

All WP8 deliverables are in DUSRM. The SAND OS repository remains read-only and unchanged. No SAND branch, pull request, file, workflow or release has been created or modified.

## Next step

Obtain owner approval for the DUSRM-first architecture policy and a separate explicit authorization for a SAND-side adoption change. Only then add the pinned architecture description and host-side CI job to `jadhavdurvesh/sand-os`.

The DUSRM profile compatibility status remains `not-assessed` pending independent review.
