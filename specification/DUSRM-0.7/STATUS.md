# DUSRM 0.7 — Conformance and Tooling Readiness

**Status:** Proposal; non-normative  
**Milestone:** M6 — Conformance and Publication Preparation  
**Release label:** 0.7-draft  
**Date:** 2026-11-09

## Objective

Prepare DUSRM for independent technical review and future tooling by defining a provisional description schema, profile compatibility rules, consistency checks, reusable fixtures, and a review package.

## Included

- JSON Schema Draft 2020-12 description-shape proposal, schema version 0.1-draft.
- Profile compatibility policy.
- Consistency-check catalogue separating structural and semantic checks from evidence and human review.
- Positive and negative conformance fixtures with declared expected outcomes.
- Review package for independent systems-engineering and formal-methods feedback.
- Tooling-readiness and deferred-implementation guidance.

## Important status limitations

- A GitHub Actions check has been added to run the JSON Schema and fixture script using the Python `jsonschema` implementation; the workflow result must be inspected before claiming a pass.
- The semantic checker does not exist; cross-reference and profile-compatibility checks remain future work.
- The schema fixture suite is configured in CI; semantic-only negative fixtures remain pending a semantic validator.
- Profile compatibility has not been externally reviewed.
- No independent reviewer has yet assessed the model.
- No system is certified or declared formally conformant.
- The eight-layer structure remains provisional.

## Key design decisions

1. Keep schema versioning independent from DUSRM conceptual versioning.
2. Use JSON Schema only for structural validation; semantic checks remain separate.
3. Keep profile refinements traceable to core responsibilities.
4. Preserve the many-to-many element-to-responsibility realization model.
5. Never infer implementation, safety, or correctness from a schema-valid description.

## Next work

- Run the schema and fixtures through an independent JSON Schema 2020-12 validator.
- Implement or prototype only semantic checks with stable test cases.
- Obtain independent technical review and record responses.
- Resolve major model gaps before proposing a stable 1.0 release.
