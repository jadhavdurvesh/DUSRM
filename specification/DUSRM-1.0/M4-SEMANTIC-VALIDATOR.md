# DUSRM 1.0 Preparation — Schema 0.2 Semantic Validator

**Work package:** WP4 — Schema 0.2 Semantic Validator and Migration Tooling  
**Status:** Implemented draft; non-normative  
**Implementation:** `scripts/validate_semantics_0_2.py`

## 1. Purpose

The schema 0.2 semantic validator checks selected relationships between typed records after JSON Schema structural validation. It is deterministic for a fixed description, schema and profile registry.

It does not establish that the real system behaves as described, that evidence is adequate for a safety claim, or that a description is fully conformant with DUSRM.

## 2. Validation sequence

The command performs these stages:

1. Parse the description and selected schema.
2. Validate the schema against JSON Schema Draft 2020-12.
3. Validate the description structurally, including declared formats.
4. Build typed object indexes for the SOI, boundary, environment participants and all model collections, including Realization allocations.
5. Check global identifier uniqueness.
6. Resolve typed references and participant references.
7. Check responsibility realizations and layer applicability.
8. Check relationship signatures and declared scope.
9. Check operation, execution, event, state and transition links.
10. Check interface/interaction participant-role consistency.
11. Check resource allocations against declared capacity and units.
12. Check capability, service, requirement, constraint, invariant and evidence links.
13. Check selected profile versions and compatibility status.
14. Return ordered machine findings.

## 3. Findings

| Code | Severity | Meaning |
|---|---|---|
| DUSRM-02-M-000 | Error | Description root is not an object |
| DUSRM-02-M-001 | Error | Duplicate identifier across system, boundary, environment, or model-record collections, including Realization records |
| DUSRM-02-M-002 | Error | Typed reference does not resolve |
| DUSRM-02-M-003 | Error | Typed reference kind is not permitted at the relationship or field endpoint |
| DUSRM-02-M-003 | Error | Typed reference kind is not permitted at this location |
| DUSRM-02-M-010 | Error | Evidence reference does not resolve |
| DUSRM-02-M-012 | Error | Duplicate element-to-responsibility realization pair |
| DUSRM-02-M-013 | Warning | Responsibility marked in progress/implemented without a realizing element |
| DUSRM-02-M-014 | Error | Duplicate layer applicability or responsibility assigned to a not-applicable layer |
| DUSRM-02-M-015 | Error | Relationship scope conflicts with the declared system of interest |
| DUSRM-02-M-016 | Error | transitionsTo endpoints belong to different state variables |
| DUSRM-02-M-017 | Error | Execution timestamp requirements or ordering are inconsistent |
| DUSRM-02-M-018 | Error | State value is outside the declared state-variable domain |
| DUSRM-02-M-019 | Error/Warning | Transition source/destination state variables differ; subject mismatch is a warning |
| DUSRM-02-M-020 | Error | Interface/interaction participant roles are duplicated or inconsistent |
| DUSRM-02-M-021 | Error | Responsibility parent hierarchy is self-referential or cyclic |
| DUSRM-02-M-022 | Error/Warning | Allocation interval, quantity, or resource unit is inconsistent |
| DUSRM-02-E-001 | Error | Assessed relationship/invariant/assertion has no linked evidence |
| DUSRM-02-E-002 | Warning | Passing assessment has no evidence explicitly marked as supporting it |
| DUSRM-02-E-003 | Warning | Evidence kind and declared producing method appear inconsistent |
| DUSRM-02-P-001 | Error/Warning | Profile is absent/version-mismatched or compatibility is not explicitly approved |

An error blocks a clean semantic result. Warnings remain visible and do not alone change the CLI exit status to failure. The report is not a conformance certificate.

## 4. Usage

From the repository root:

```bash
python scripts/validate_semantics_0_2.py schema/fixtures/0.2/valid-minimal.json
python scripts/validate_semantics_0_2.py schema/fixtures/0.2/valid-sand-os-architecture.json
```

Useful options:

```bash
python scripts/validate_semantics_0_2.py path/to/description.json --json
python scripts/validate_semantics_0_2.py path/to/description.json --no-registry
python scripts/validate_semantics_0_2.py path/to/description.json --schema path/to/schema.json
python scripts/validate_semantics_0_2.py path/to/description.json --registry path/to/registry.json
```

Exit codes:
- **0:** schema valid and no semantic errors; warnings may be present.
- **1:** schema or semantic validation errors.
- **2:** input, schema, or registry could not be loaded/validated.

## 5. Current checks and limitations

The validator currently checks:
- global identifier uniqueness across all records, including Realization allocations;
- typed references to Realization records where the target kind is explicitly declared;
- typed-reference resolution against declared collections;
- relationship endpoint kinds and participant references;
- duplicate realization pairs and selected maturity conflicts;
- responsibility-parent cycles;
- layer applicability uniqueness and contradictions;
- relationship system scope where explicitly declared;
- operation owners and typed input/output references;
- execution operation/subject references and timestamp ordering;
- event source references;
- state-variable ownership, state domains and transition endpoints;
- interface contracts, operations, interaction participant roles and interface consistency;
- resource owners, allocation participants, units, capacity and validity intervals;
- capability/service providers, operations, interfaces and consumers;
- subject references on constraints, invariants, assertions and decisions;
- evidence links on all record collections, including realizations and relationships;
- profile versions and explicit compatibility status.

The validator does not yet:
- prove layer allocation is architecturally correct;
- prove relationship semantics or cardinality beyond the defined signature checks;
- prove that a declared scope logically contains every endpoint;
- infer or verify transitivity, causality, symmetry, authority or control priority;
- assess evidence independence, freshness, uncertainty or fitness for a particular assurance claim;
- perform complete profile composition analysis;
- verify implementation behavior, hardware effects, safety or security.

Unimplemented checks must not be described as passed. A warning-free result means only that this implementation found no issue in its current check set.

## 6. Version isolation

This is a schema 0.2 validator. It is separate from `scripts/validate_semantics.py`, which remains the historical schema 0.1/0.9 validator.

The old validator and fixtures remain available for reproducibility.
