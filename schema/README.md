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

Schema 0.2 structural, semantic, migration and WP5/WP6 profile CI [run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813575) passed on 2026-11-11. The workflow passed 22 semantic/migration tests, 4 existing profile tests and 8 SAND OS profile tests; validated the SAND OS profile with zero semantic errors and the expected not-assessed warning; and exercised a 0.1→0.2 review-draft migration. The schema 0.1, 0.8 and 0.9 compatibility workflows also passed on the tested code commit.

The four profile fixtures are [standalone application](fixtures/0.2/profiles/standalone-application.json), [ANANTA](fixtures/0.2/profiles/ananta-database-engine.json), [FireBot](fixtures/0.2/profiles/firebot-cyber-physical-robotics.json), and [SAND OS](fixtures/0.2/profiles/sand-os-operating-system.json). Their registry compatibility states remain not-assessed; profile fixture success is not an approval.

See the [WP6 adoption plan](../specification/DUSRM-1.0/M6-SAND-OS-ADOPTION.md), [SAND OS architecture mapping](../specification/DUSRM-1.0/M6-SAND-OS-ARCHITECTURE-MAP.md), and [WP6 review findings](../specification/DUSRM-1.0/M6-REVIEW-FINDINGS.md).

## Validation boundaries

Structural JSON Schema validation checks document shape and declared endpoint kinds. The semantic validator performs selected cross-reference, uniqueness, allocation, state, interaction, resource, evidence-reference and profile checks. Neither establishes full DUSRM conformance or real-system behavior.

The migration utility preserves the source file and produces a report. Ambiguous conversions are not guessed; incomplete output requires explicit `--allow-incomplete`.

The schema does not define a wire protocol, API, runtime, database format, or mandatory implementation technology.
