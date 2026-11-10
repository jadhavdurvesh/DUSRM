# DUSRM Machine-Readable Description Schemas

**Status:** Proposal; non-normative  
**Schema ID:** urn:dusrm:schema:description:0.1-draft  
**Target model:** DUSRM 0.7-draft

## Purpose

This directory contains a provisional JSON Schema for the structure of a DUSRM system description.

The schema validates document shape and basic field types. It does not establish that references resolve, identifiers are unique across collections, relationships have valid participant kinds, invariants are true, or a system conforms to DUSRM.

## Files

- [Description schema](dusrm-description-0.1.schema.json)
- [Valid minimal example](../conformance/fixtures/valid-minimal.json)
- [Valid multi-layer realization example](../conformance/fixtures/valid-multilayer-realization.json)

## Compatibility and status

- JSON Schema dialect: Draft 2020-12.
- Schema version: 0.1-draft.
- DUSRM model version: 0.7-draft.
- Breaking schema changes require a new schema version and migration notes.
- Additive fields may still require a schema revision if consumers use strict validation.
- GitHub Actions run [#5](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42648618733) passed the schema and structural fixture checks with `jsonschema` 4.26.0 on 2026-11-09.

## Validation boundary

Structural JSON Schema validation is only the first stage. Cross-reference, uniqueness, profile compatibility, relationship signatures, layer allocation, evidence status, and proof-obligation checks are defined in the conformance catalogue and remain outside the current script.

The schema does not define a wire protocol, API, runtime, database format, or mandatory implementation technology.

## Schema 0.2 — DUSRM 1.0 preparation

- [Schema 0.2 draft](dusrm-description-0.2.schema.json)
- [WP3 design](../specification/DUSRM-1.0/M3-SCHEMA-DESIGN.md)
- [0.1 to 0.2 migration guide](../specification/DUSRM-1.0/M3-MIGRATION-0.1-TO-0.2.md)
- [Schema 0.2 fixtures](fixtures/0.2/README.md)
- [Dedicated validation script](../scripts/validate_schema_0_2_fixtures.py)
- [Dedicated GitHub Actions workflow](../.github/workflows/dusrm-1.0-schema-validation.yml)

Schema 0.2 structural CI [run #3](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42749757789) passed on 2026-11-10: schema meta-validation passed, both positive fixtures were accepted, and both negative fixtures were rejected as expected.

Schema 0.2 is a breaking, separately identified Draft 2020-12 proposal (`urn:dusrm:schema:description:0.2-draft`). It adds typed references, first-class ontology collections, orthogonal status dimensions and relationship endpoint-kind constraints. It does not replace schema 0.1 and is not yet a stable interchange contract.

The schema 0.2 validator checks structure and endpoint kinds. It does not resolve identifiers across collections, assess evidence adequacy, or establish conformance. See the WP3 validation report for the exact boundary.
