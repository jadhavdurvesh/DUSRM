# DUSRM 1.0 Preparation — WP3 Status

**Work package:** WP3 — Typed Metamodel and Schema 0.2 Design  
**Status:** WP3 internally complete; structural CI passed; independent review pending  
**Date:** 2026-11-10  
**Schema:** 0.2-draft

## Objective

Translate the WP2 ontology into an independently versioned machine-readable schema, test its structural contract, and document a safe migration path from schema 0.1.

## Deliverables

- [WP3 schema design](M3-SCHEMA-DESIGN.md)
- [Schema 0.2 JSON Schema](../../schema/dusrm-description-0.2.schema.json)
- [Schema 0.2 fixture suite](../../schema/fixtures/0.2/manifest.json)
- [SAND OS typed architecture example](../../schema/fixtures/0.2/valid-sand-os-architecture.json)
- [0.1 to 0.2 migration guidance](M3-MIGRATION-0.1-TO-0.2.md)
- [Proposed decisions](M3-DECISIONS.md)
- [Validation report](M3-VALIDATION.md)
- [Dedicated CI workflow](../../.github/workflows/dusrm-1.0-schema-validation.yml)

## Included in schema 0.2

- typed references with explicit object kind;
- system, element, environment participant and responsibility distinctions;
- realization allocations and layer applicability;
- operation and execution records;
- event, state variable, state and transition records;
- interface and multi-party interaction records;
- resource and reified allocation records;
- capability and service records;
- requirement, constraint, invariant, assertion and decision records;
- evidence method, context and relation fields;
- typed relationship endpoint constraints for 17 core relationships;
- separate design disposition, realization state, applicability and assessment result fields.

## Automated validation

The final dedicated schema 0.2 structural workflow [run #4](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42749920371) passed on 2026-11-10. Both positive fixtures were accepted and both negative fixtures were rejected as expected.

WP4 subsequently added the schema 0.2 semantic validator and migration tooling. See [WP4 status](M4-STATUS.md) and its [validation report](M4-VALIDATION.md).

## Important limits

- Schema 0.2 is a draft, not a stable interchange standard.
- Structural validation does not establish semantic correctness or conformance.
- Domain profiles remain not-assessed.
- The SAND OS example is a DUSRM-side documentation pilot and does not modify the SAND OS repository.
- DUSRM 1.0 has not been declared stable.

## Exit criteria

WP3 is internally complete: the dedicated workflow passes all structural fixtures, schema 0.1 remains preserved, and migration/review limits are documented. Formal acceptance still requires independent review of the ontology, schema and migration behavior.

## Next work package

**WP4 — Schema 0.2 Semantic Validator and Migration Tooling: internally complete.** See [WP4 status](M4-STATUS.md).

The next work package is **WP5 — Domain Profile Reconciliation and Independent Review Preparation**.
