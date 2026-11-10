# DUSRM 1.0 Preparation

**Status:** Working research draft; non-normative  
**Target:** Candidate DUSRM 1.0 core  
**Stable release:** Not declared

This directory contains versioned work packages for preparing a proposed 1.0 core. It does not supersede the historical 0.x documents or imply that independent review has been completed.

## Work packages

### WP1 — Layer Definitions and Boundaries

**Status:** Documentation complete; independent review pending.

- [Status](M1-STATUS.md)
- [Core layer charter](M1-LAYER-CHARTER.md)
- [Boundary decision matrix](M1-LAYER-BOUNDARIES.md)
- [Proposed decisions](M1-DECISIONS.md)
- [Internal validation](M1-VALIDATION.md)

### WP2 — Foundational Ontology and Relationship Consolidation

**Status:** Documentation complete; independent review and schema work pending.

- [Status](M2-STATUS.md)
- [Consolidated core ontology](M2-ONTOLOGY-CORE.md)
- [Relationship semantics and signature matrix](M2-RELATIONSHIP-MATRIX.md)
- [Assertion, applicability, realization, and evidence model](M2-ASSERTION-EVIDENCE.md)
- [Ontology and tooling compatibility](M2-TOOLING-COMPATIBILITY.md)
- [Proposed decisions](M2-DECISIONS.md)
- [Internal validation](M2-VALIDATION.md)

## Proposed next work package

**WP3 — Typed Metamodel and Schema 0.2 Design**

WP3 is expected to design typed references, first-class behavioral and contract records, orthogonal status fields, schema fixtures, and a loss-aware migration from schema 0.1. It must be separately versioned and validated before new 1.0 conformance claims are made.

## Release gate

DUSRM 1.0 must not be declared stable solely because WP1 and WP2 documentation exists. The core ontology, relationship semantics, metamodel, schema, conformance checks, domain profiles, and independent review findings must be reconciled and approved through the repository's governance process.
