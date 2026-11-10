# DUSRM 1.0 Preparation — WP3 Status

**Work package:** WP3 — Typed Metamodel and Schema 0.2 Design  
**Status:** WP3 internally complete; structural CI passed; independent review and semantic validation pending  
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

The final dedicated workflow [run #4](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42749920371) passed on 2026-11-10 at commit `f4be7c3c8edc6a8bc16e21490a6a0558ea44815a`. The schema meta-validation and fixture job completed successfully: both positive fixtures were accepted and both negative fixtures were rejected as expected. This run includes the final SAND OS fixture refinement. It does not validate cross-collection semantic references.

## Important limits

- Schema 0.2 is a draft, not a stable interchange standard.
- The structural fixture runner does not resolve references between collections.
- No full semantic validator for schema 0.2 has been implemented.
- No general-purpose 0.1 to 0.2 migration utility exists.
- Domain profiles remain not-assessed.
- The SAND OS example is a documentation-level pilot and does not modify the SAND OS repository.
- DUSRM 1.0 has not been declared stable.

## Exit criteria

WP3 is internally complete: the dedicated CI workflow passes all positive and negative fixtures, schema 0.1 and the prior 0.8/0.9 validation workflows remain unaffected, and migration/review limits are documented. Formal acceptance still requires independent review of the ontology, schema and migration behavior.

## Next work package

**WP4 — Schema 0.2 Semantic Validator and Migration Tooling**

Add deterministic cross-reference resolution, global identifier checks, realization and layer applicability consistency, relationship scope checks, evidence-reference checks, profile behavior, and migration reporting. Keep all checks version-aware and preserve schema 0.1 behavior.
