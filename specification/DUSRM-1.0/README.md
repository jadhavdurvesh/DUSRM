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

## Proposed next work package

**WP5 — Domain Profile Reconciliation and Independent Review Preparation**

Reconcile the standalone application, ANANTA and FireBot profiles against the 1.0 ontology/schema; identify profile-specific typed concepts and compatibility; build review cases; and prepare an independent reviewer package with objections, expected behaviors, and change-control records.

## Release gate

DUSRM 1.0 must not be declared stable solely because WP1–WP4 artifacts and CI exist. The core ontology, relationship semantics, metamodel, schema, semantic rules, migration behavior, conformance checks, domain profiles, and independent review findings must be reconciled and approved through the repository's governance process.
