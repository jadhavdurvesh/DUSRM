# DUSRM 1.0 Preparation — WP3 Schema 0.2 Validation Report

**Work package:** WP3 — Typed Metamodel and Schema 0.2 Design  
**Status:** Automated structural validation passed; non-normative

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

## 5. Legacy-version compatibility check

The existing schema 0.1 and the 0.8/0.9 validation workflows were re-run on 2026-11-10 after the WP3 schema 0.2 additions:

- [Schema 0.1 workflow](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42749841293) — success, commit `8fbe438b03316e3951bc36d733aab928b95ccd80`.
- [DUSRM 0.8 semantic/formal workflow](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42749841332) — success, same commit.
- [DUSRM 0.9 advanced validation workflow](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42749841354) — success, same commit.

The historical schema 0.1 file remains at blob SHA `0d9ed1b7224a20bb3d4d771c247210de9411a4ee`. The schema 0.1 fixture validator remains at `e6f0a098d90d9e75ff22d2a1298532fa298981ff`, and the 0.9 semantic validator remains at `6a1bd2849232d131a4be8726e523574dec29e834`. These file hashes confirm that the existing implementation files were not rewritten by WP3.

## 6. Recorded result

**Review status:** Not independently reviewed.

- Workflow: DUSRM 1.0 preparation — Schema 0.2 draft validation
- Run: [#3](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42749757789)
- Run ID: `42749757789`
- Commit checked: `13c01c22bba38ac989e893671fdc9187585ce2f2`
- Date: 2026-11-10
- Job: Validate typed schema and fixtures
- Conclusion: **success**
- Result: Draft 2020-12 schema accepted; both positive fixtures passed; both negative fixtures were rejected as expected.

The current `main` branch subsequently received documentation-only updates to WP2 handoff status; the schema, fixtures, validator script and workflow were unchanged after the successful run.
