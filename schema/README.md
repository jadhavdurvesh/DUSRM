# DUSRM Machine-Readable Description Schema

**Status:** Proposal; non-normative  
**Schema ID:** urn:dusrm:schema:description:0.1-draft  
**Target model:** DUSRM 0.7-draft

## Purpose

This directory contains a provisional JSON Schema for the structure of a DUSRM system description.

The schema validates document shape and basic field types. It does not establish that references resolve, identifiers are unique across collections, relationships have valid participant kinds, invariants are true, or a system conforms to DUSRM.

## Files

- Description schema: dusrm-description-0.1.schema.json
- Valid minimal example: conformance/fixtures/valid-minimal.json
- Valid multi-layer realization example: conformance/fixtures/valid-multilayer-realization.json

## Compatibility and status

- JSON Schema dialect: Draft 2020-12.
- Schema version: 0.1-draft.
- DUSRM model version: 0.7-draft.
- Breaking schema changes require a new schema version and migration notes.
- Additive fields may still require a schema revision if consumers use strict validation.
- The schema has not yet been run through an independent JSON Schema implementation.

## Validation boundary

Structural JSON Schema validation is only the first stage. Cross-reference, uniqueness, profile compatibility, relationship signatures, layer allocation, evidence status, and proof-obligation checks are defined in the conformance catalogue.

The schema does not define a wire protocol, API, runtime, database format, or mandatory implementation technology.
