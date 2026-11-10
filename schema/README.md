# DUSRM Machine-Readable Description Schemas

**Status:** Proposal; non-normative  
**Schema 0.1 ID:** urn:dusrm:schema:description:0.1-draft  
**Schema 0.2 ID:** urn:dusrm:schema:description:0.2-draft

## Purpose

This directory contains separately versioned JSON Schemas for DUSRM system descriptions. Schema 0.1 remains the historical 0.x format. Schema 0.2 is the typed description proposal for DUSRM 1.0 preparation.

## Schema 0.1

- [Description schema](dusrm-description-0.1.schema.json)
- [Legacy fixtures](../conformance/fixtures/)

Schema 0.1 uses the 0.x status vocabulary and untyped relationship endpoint IDs. Its structural and semantic tooling is preserved for historical descriptions.

## Schema 0.2 — DUSRM 1.0 preparation

- [Schema 0.2 draft](dusrm-description-0.2.schema.json)
- [WP3 schema design](../specification/DUSRM-1.0/M3-SCHEMA-DESIGN.md)
- [WP3 0.1→0.2 migration guidance](../specification/DUSRM-1.0/M3-MIGRATION-0.1-TO-0.2.md)
- [Schema 0.2 fixtures](fixtures/0.2/README.md)
- [Structural fixture validator](../scripts/validate_schema_0_2_fixtures.py)
- [Semantic validator 0.2](../scripts/validate_semantics_0_2.py)
- [Migration utility](../scripts/migrate_schema_0_1_to_0_2.py)
- [WP4 semantic validator design](../specification/DUSRM-1.0/M4-SEMANTIC-VALIDATOR.md)
- [WP4 migration tooling guide](../specification/DUSRM-1.0/M4-MIGRATION-TOOLING.md)
- [Dedicated CI workflow](../.github/workflows/dusrm-1.0-schema-validation.yml)

Schema 0.2 structural, semantic and migration CI [run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42872255944) passed on 2026-11-10. The workflow validated both positive fixtures, rejected both structural negatives, passed 18 regression tests, semantically validated the minimal and SAND OS fixtures without findings, and exercised a 0.1→0.2 review-draft migration.

## Validation boundaries

Structural JSON Schema validation checks document shape and declared endpoint kinds. The semantic validator performs selected cross-reference, uniqueness, allocation, state, interaction, resource, evidence-reference and profile checks. Neither establishes full DUSRM conformance or real-system behavior.

The migration utility preserves the source file and produces a report. Ambiguous conversions are not guessed; incomplete output requires explicit `--allow-incomplete`.

The schema does not define a wire protocol, API, runtime, database format, or mandatory implementation technology.
