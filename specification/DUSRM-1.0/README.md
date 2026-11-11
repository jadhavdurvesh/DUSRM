# DUSRM 1.0 Preparation

**Status:** Working research draft; non-normative  
**Target:** Candidate DUSRM 1.0 core  
**Stable release:** Not declared

This directory contains versioned work packages for preparing a proposed 1.0 core. It does not supersede the historical 0.x documents or imply that independent review has been completed.

## WP1 — Layer Definitions and Boundaries

**Status:** Documentation complete; independent review pending.

- [Status](M1-STATUS.md)
- [Core layer charter](M1-LAYER-CHARTER.md)
- [Boundary decision matrix](M1-LAYER-BOUNDARIES.md)
- [Proposed decisions](M1-DECISIONS.md)
- [Internal validation](M1-VALIDATION.md)

## WP2 — Foundational Ontology and Relationship Consolidation

**Status:** Documentation complete; independent review pending.

- [Status](M2-STATUS.md)
- [Consolidated core ontology](M2-ONTOLOGY-CORE.md)
- [Relationship semantics and signature matrix](M2-RELATIONSHIP-MATRIX.md)
- [Assertion, applicability, realization, and evidence model](M2-ASSERTION-EVIDENCE.md)
- [Ontology and tooling compatibility](M2-TOOLING-COMPATIBILITY.md)
- [Proposed decisions](M2-DECISIONS.md)
- [Internal validation](M2-VALIDATION.md)

## WP3 — Typed Metamodel and Schema 0.2 Design

**Status:** Internally complete; structural CI passed; independent review pending.

- [Status](M3-STATUS.md)
- [Schema design](M3-SCHEMA-DESIGN.md)
- [Migration guidance](M3-MIGRATION-0.1-TO-0.2.md)
- [Proposed decisions](M3-DECISIONS.md)
- [Validation report](M3-VALIDATION.md)
- [Schema 0.2](../../schema/dusrm-description-0.2.schema.json)
- [SAND OS architecture fixture](../../schema/fixtures/0.2/valid-sand-os-architecture.json)

## WP4 — Schema 0.2 Semantic Validator and Migration Tooling

**Status:** Implemented draft; CI passed; independent review pending.

- [Status](M4-STATUS.md)
- [Semantic validator design and usage](M4-SEMANTIC-VALIDATOR.md)
- [Migration tooling and CLI](M4-MIGRATION-TOOLING.md)
- [Proposed decisions](M4-DECISIONS.md)
- [Automated validation report](M4-VALIDATION.md)
- [Semantic validator implementation](../../scripts/validate_semantics_0_2.py)
- [Migration utility](../../scripts/migrate_schema_0_1_to_0_2.py)
- [Regression tests](../../tests/test_semantics_0_2.py)
- [WP4 CI workflow](../../.github/workflows/dusrm-1.0-schema-validation.yml)

## WP5 — Domain Profile Reconciliation and Independent Review Preparation

**Status:** Internal reconciliation complete; CI passed; independent review pending.

- [Status](M5-STATUS.md)
- [Profile reconciliation report](M5-RECONCILIATION.md)
- [Compatibility matrix](M5-COMPATIBILITY-MATRIX.md)
- [Independent reviewer cases](M5-REVIEW-CASES.md)
- [Read-only evidence snapshot](M5-EVIDENCE-SNAPSHOT.md)
- [Proposed decisions](M5-DECISIONS.md)
- [Independent reviewer package](M5-REVIEW-PACKAGE.md)
- [Validation report](M5-VALIDATION.md)
- [Profile fixtures](../../schema/fixtures/0.2/profiles/)
- [Profile regression tests](../../tests/test_profiles_0_2.py)

All three profiles remain `not-assessed`. A clean fixture result is not a profile compatibility approval.

## WP6 — SAND OS Adoption Pilot and Release Gate Review

**Status:** DUSRM-side OS profile and adoption package prepared; CI passed; SAND-side approval and independent review pending.

- [WP6 status](M6-STATUS.md)
- [SAND OS adoption plan](M6-SAND-OS-ADOPTION.md)
- [SAND OS architecture mapping](M6-SAND-OS-ARCHITECTURE-MAP.md)
- [Desk review findings](M6-REVIEW-FINDINGS.md)
- [SAND OS implementation plan](M6-IMPLEMENTATION-PLAN.md)
- [Standards crosswalk](M6-STANDARDS-CROSSWALK.md)
- [WP6 validation report](M6-VALIDATION.md)
- [Operating-system profile](../../profiles/operating-system/PROFILE.md)
- [SAND OS schema 0.2 fixture](../../schema/fixtures/0.2/profiles/sand-os-operating-system.json)

The SAND OS profile remains `not-assessed`. The [WP6 CI run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813575) passed 22 semantic/migration tests, 4 existing profile tests and 8 SAND OS profile tests. The SAND OS repository was inspected read-only and was not modified.

## Release gate

DUSRM 1.0 must not be declared stable solely because WP1–WP8 artifacts and CI exist. The core ontology, layer definitions, relationship semantics, schema, semantic rules, migration behavior, conformance checks, domain profiles, evidence and independent review findings must be reconciled and approved through the repository's governance process.

## WP7 — Portable Validation Kit and SAND OS Adoption Review

**Status:** Portable kit implemented and CI passed; independent review and SAND-side adoption approval pending.

- [WP7 status](M7-STATUS.md)
- [WP7 validation record](M7-VALIDATION.md)
- [Portable SAND OS validation kit](../../adoption/sand-os/README.md)
- [Proposed SAND CI adoption](M7-SAND-CI-ADOPTION.md)
- [Independent review checklist](M7-REVIEW-CHECKLIST.md)

The [portable-kit CI run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031919228) passed 4/4 bundle-integrity checks and all 14 kit tests. Its report artifact is [available here](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43031919228/artifacts/13860938644). The SAND OS model covered 16/16 required OS domains, mapped all eight DUSRM layers, produced zero semantic errors and retained one expected not-assessed compatibility warning.

The SAND OS repository remains unchanged. Its proposed host-side CI adoption requires separate explicit approval.


## WP8 — DUSRM as the Primary SAND OS Architecture Reference

**Status:** Governance and change-review policy prepared; SAND-side adoption pending.

- [WP8 status](M8-STATUS.md)
- [SAND OS architecture governance](M8-SAND-OS-ARCHITECTURE-GOVERNANCE.md)
- [SAND OS DUSRM change-review template](../../adoption/sand-os/CHANGE-REVIEW-TEMPLATE.md)

WP8 proposes DUSRM as SAND's primary project-level responsibility architecture, replacing inconsistent top-level layer diagrams. SAND-specific technical contracts such as Veyra, SAPP and SANDFS remain authoritative for their implementation details. No SAND OS repository changes have been made.
