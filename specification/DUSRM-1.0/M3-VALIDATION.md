# DUSRM 1.0 Preparation — WP3 Schema 0.2 Validation Report

**Work package:** WP3 — Typed Metamodel and Schema 0.2 Design  
**Status:** Automated validation pending/recorded by CI; non-normative

## 1. Validation scope

WP3 validates the JSON Schema 0.2 structure and the included fixtures. The validation target is the schema document and fixture files, not the SAND OS implementation.

## 2. Fixture suite

| Fixture | Expected | Purpose |
|---|---|---|
| valid-minimal.json | Pass | Minimal complete schema 0.2 envelope |
| valid-sand-os-architecture.json | Pass | Populated typed architecture example; exercises all 17 relationship endpoint signatures |
| invalid-wrong-typed-endpoint.json | Reject | A performs relation uses an Element instead of an Execution |
| invalid-legacy-status-field.json | Reject | Legacy top-level status field is rejected; descriptionState is required |

## 3. Automated checks

The dedicated script performs:
- JSON parsing;
- JSON Schema Draft 2020-12 meta-schema validation;
- structural validation of positive fixtures;
- expected rejection of negative fixtures;
- format checks for declared date-time fields.

Workflow: [DUSRM 1.0 preparation — Schema 0.2 draft validation](../../.github/workflows/dusrm-1.0-schema-validation.yml).

## 4. Validation limitations

A structural pass does not establish:
- referenced identifier existence or global uniqueness;
- typed reference kind-to-collection resolution;
- relationship scope consistency;
- allocation and responsibility correctness;
- evidence adequacy, recency or independence;
- profile compatibility;
- system behavior, implementation conformance, safety or security.

These are reserved for a future semantic validator and human review.

## 5. Result recording

The CI run URL, run identifier, commit SHA, result and date must be entered here after the workflow completes. Do not record success based on a queued or in-progress run.
