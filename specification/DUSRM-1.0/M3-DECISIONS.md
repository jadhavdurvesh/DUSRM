# DUSRM 1.0 Preparation — WP3 Schema and Metamodel Decisions

**Work package:** WP3 — Typed Metamodel and Schema 0.2 Design  
**Status:** Proposed decisions; awaiting review  
**Date:** 2026-11-10

## 1. Proposed decisions

| ID | Decision | Rationale | Status |
|---|---|---|---|
| WP3-D01 | Keep schema 0.1 immutable for legacy 0.7/0.9 descriptions | Preserve reproducibility and historical validation | Proposed |
| WP3-D02 | Create schema 0.2 as a separately identified Draft 2020-12 schema | Typed metamodel is a breaking structural change | Drafted |
| WP3-D03 | Use typed references with kind and identifier | Avoid ambiguous string endpoints | Proposed |
| WP3-D04 | Require explicit top-level collection envelopes | Missing arrays should not be confused with intentionally empty collections | Proposed |
| WP3-D05 | Add first-class Execution, Event, State, Interface, Interaction, Resource, Allocation, Capability, Service, Requirement, Constraint, Invariant, Assertion, Decision and Evidence collections | Make ontology objects independently referable and type-checkable | Proposed |
| WP3-D06 | Encode relationship endpoint-kind constraints in JSON Schema conditionals | Reject structurally invalid endpoint categories before semantic checks | Drafted |
| WP3-D07 | Separate design disposition, realization state, applicability and assessment result | Avoid overloading one status value | Proposed |
| WP3-D08 | Use reified records for allocation and multi-party interaction | Preserve recipient, quantity, roles, context and validity | Proposed |
| WP3-D09 | Reserve Realization for element-to-responsibility allocation and use implements for implementation-to-specification | Remove relationship-name collision | Proposed |
| WP3-D10 | Treat schema 0.2 validation as structural, not full DUSRM conformance | Prevent overstating what JSON Schema can prove | Proposed |
| WP3-D11 | Require a loss-aware migration report and preserve schema 0.1 source files | Prevent ambiguous status and endpoint conversion | Proposed |

## 2. Decisions not made

WP3 does not:
- make schema 0.2 stable;
- approve DUSRM 1.0;
- implement global reference resolution or full semantic validation;
- run a migration utility against every existing description;
- approve any existing domain profile for schema 0.2;
- establish safety, security, regulatory, or implementation conformance.

## 3. Review requirements

Before acceptance:
- verify the schema against a JSON Schema Draft 2020-12 implementation;
- review endpoint signatures and object-kind vocabulary;
- review time and quantity value representation;
- inspect the SAND OS fixture for inaccurate maturity claims;
- test profile extension and unknown-field behavior;
- review migration rules for ambiguous legacy statuses;
- confirm that schema 0.1 and its validation workflow remain unchanged.

## 4. Review record

No independent reviewer findings have yet been received.

| Reviewer | Expertise | Date | Finding | Disposition |
|---|---|---|---|---|
| Pending | JSON Schema/tooling | Pending | Not received | Open |
| Pending | Systems ontology | Pending | Not received | Open |
| Pending | Systems architecture | Pending | Not received | Open |
