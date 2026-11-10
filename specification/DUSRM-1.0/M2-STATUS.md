# DUSRM 1.0 Preparation — WP2 Status

**Work package:** WP2 — Foundational Ontology and Relationship Consolidation  
**Status:** Documentation complete; independent review and schema work pending  
**Target release:** DUSRM 1.0 (not yet declared)  
**Date:** 2026-11-10

## Objective

Consolidate the foundational ontology, disambiguate core relationship semantics, separate status dimensions, and assess compatibility with current schema/validator tooling.

## Deliverables

- [Consolidated core ontology](M2-ONTOLOGY-CORE.md)
- [Relationship semantics and signature matrix](M2-RELATIONSHIP-MATRIX.md)
- [Assertion, applicability, realization, and evidence model](M2-ASSERTION-EVIDENCE.md)
- [Ontology and tooling compatibility analysis](M2-TOOLING-COMPATIBILITY.md)
- [Proposed ontology decisions and review record](M2-DECISIONS.md)
- [Internal ontology and relationship validation](M2-VALIDATION.md)

## Work completed

- Separated reference-model, subject, description, and evidence levels.
- Defined SOI, Element, Environment Participant, Participant, Boundary, category, kind, and role.
- Distinguished Responsibility, Realization allocation, Operation, Execution, Event, Information Object, Property, State Variable, State/Configuration, Transition, Interface, Interaction, Resource, Capability, Service, Requirement, Constraint, Invariant, Assertion, Decision, and Evidence.
- Clarified that only Responsibilities receive a primary core layer.
- Defined conceptual endpoint roles and semantics for the relationship catalogue.
- Identified the legacy realizes naming collision and proposed implements for implementation-to-specification trace.
- Added rules for reified allocations and multi-party interactions.
- Separated design disposition, realization state, applicability, assessment result, and evidence method/context.
- Audited the current schema 0.1, validator 0.9, and profile registry against the proposed model.

## Important limits

- All WP2 decisions remain proposed and non-normative.
- No new JSON Schema or migration tool was created.
- The existing 0.1 schema and 0.9 validator remain unchanged.
- Unsupported relationship signatures remain warnings in the legacy validator.
- The three domain profiles remain not-assessed; no 1.0 compatibility is claimed.
- No independent external review has been recorded.
- DUSRM 1.0 has not been declared stable.

## Exit criteria

WP2 is complete as a conceptual and documentation package. Acceptance requires independent ontology, systems architecture, formal-methods, and tooling review.

## Next work package

**WP3 — Typed Metamodel and Schema 0.2 Design**

Design a versioned typed-reference model, explicit behavioral and contract records, orthogonal status fields, and a loss-aware migration from schema 0.1. Deliver fixtures and conformance rules before enabling new semantic checks.
