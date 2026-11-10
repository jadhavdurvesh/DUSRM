# DUSRM 1.0 Preparation — Schema 0.2 Semantic Validator

**Work package:** WP4 — Schema 0.2 Semantic Validator and Migration Tooling  
**Status:** Implemented draft; non-normative  
**Implementation:** `scripts/validate_semantics_0_2.py`

## 1. Purpose

The schema 0.2 semantic validator checks selected consistency rules across typed records after JSON Schema structural validation. It resolves typed references against declared collections and returns deterministic, ordered findings for a fixed description, schema and profile registry.

It is not a conformance certifier and does not establish that a real system behaves as described or that evidence is sufficient for a safety or security claim.

## 2. Validation sequence

The command performs these stages:

1. Parse the description, schema and optional profile registry.
2. Validate the schema against JSON Schema Draft 2020-12.
3. Validate the description structurally, including declared formats.
4. Build indexes for the SOI, boundary, environment participants and all typed model collections.
5. Check global identifier uniqueness across the SOI, boundary, environment, and all ID-bearing collections, including Realization and Relationship records.
6. Resolve typed references and participant references.
7. Check realization pairs, selected maturity consistency and responsibility hierarchy.
8. Check layer applicability and selected relationship scope rules.
9. Check operations, executions, events, state variables, states and transitions.
10. Check interfaces, interaction roles and service contracts.
11. Check resources and allocations, including units and declared capacities.
12. Check capability, service, requirement, constraint, invariant, assertion and decision references.
13. Check evidence references and selected evidence-method consistency.
14. Check selected profile versions and explicit compatibility status.
15. Emit ordered machine findings.

## 3. Finding catalogue

| Code | Severity | Meaning |
|---|---|---|
| DUSRM-02-M-000 | Error | Description root is not an object |
| DUSRM-02-M-001 | Error | Duplicate identifier across modeled object collections |
| DUSRM-02-M-002 | Error | Typed reference does not resolve |
| DUSRM-02-M-003 | Error | Typed reference kind is not permitted at the use site |
| DUSRM-02-M-010 | Error | Evidence reference does not resolve |
| DUSRM-02-M-012 | Error | Duplicate element-to-responsibility Realization pair |
| DUSRM-02-M-013 | Warning | Responsibility marked in progress/implemented without a realizing element |
| DUSRM-02-M-014 | Error | Duplicate layer-applicability declaration or responsibility assigned to a not-applicable layer |
| DUSRM-02-M-015 | Error | Relationship scope conflicts with the declared system of interest |
| DUSRM-02-M-016 | Error | `transitionsTo` endpoints belong to different state variables |
| DUSRM-02-M-017 | Error | Execution timestamp requirements or ordering are inconsistent |
| DUSRM-02-M-018 | Error | State value is outside its state-variable domain |
| DUSRM-02-M-019 | Error / Warning | Transition source/destination state variables differ (error); transition subject differs from state-variable subject (warning) |
| DUSRM-02-M-020 | Error | Interface/interaction participant-role assignments are duplicated or inconsistent |
| DUSRM-02-M-021 | Error | Responsibility parent hierarchy is self-referential or cyclic |
| DUSRM-02-M-022 | Error / Warning | Allocation interval or capacity is inconsistent (error); allocation unit differs from resource unit (warning) |
| DUSRM-02-E-001 | Error | Implemented Realization conflicts with element maturity, or an assessed relationship/invariant/assertion has no linked evidence |
| DUSRM-02-E-002 | Warning | Passing assessment has no evidence explicitly marked as supporting it |
| DUSRM-02-E-003 | Warning | Evidence kind and evidence-producing method appear inconsistent |
| DUSRM-02-P-001 | Error / Warning | Profile is absent/version-mismatched (error) or compatibility is not explicitly approved (warning) |

Errors cause the CLI to return exit code 1. Warnings remain visible but do not alone change the exit status to failure. A warning-free result is not a conformance certificate.

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
- **2:** input, schema or registry could not be loaded/validated.

## 5. Checks implemented

The current validator checks:
- global identifier uniqueness across all ID-bearing collections;
- typed-reference resolution, including references to Realization records;
- relationship endpoint signatures and participant reference kinds;
- evidence-reference resolution on records, relationships, realizations and layer-applicability declarations;
- duplicate Realization pairs and selected maturity conflicts;
- responsibility parent references, self-parenting and hierarchy cycles;
- layer applicability uniqueness and contradictions;
- relationship scope references and conflicting system-of-interest participants;
- operation owners and typed input/output references;
- execution operation/subject references, lifecycle timestamp requirements and timestamp ordering;
- event source references;
- state-variable ownership, finite state domains and transition consistency;
- interface contract and operation references;
- interface/interaction participant-role uniqueness and agreement;
- resource owners, allocation participants, intervals, capacity and units;
- capability/service providers, operations, interfaces and consumers;
- requirement sources and subject references on constraints, invariants, assertions and decisions;
- evidence references and selected evidence-kind/method consistency;
- profile versions and explicit registry compatibility status.

## 6. Deliberate limits

The validator does **not**:
- decide whether the eight-layer architecture is complete or well designed;
- prove that a responsibility has been assigned to the correct layer;
- prove a relationship's full semantic correctness or cardinality beyond the current signature checks;
- prove that a declared boundary logically contains every referenced participant;
- infer or verify transitivity, symmetry, inverse, causality, authority or control priority;
- establish that an interface is reachable or an operation actually executes;
- assess evidence independence, freshness, uncertainty, sufficiency or truth automatically;
- perform complete profile-composition analysis;
- verify implementation behavior, physical hardware effects, safety or security.

A clean result means only that this validator found no errors in its current check set. Unimplemented checks must not be treated as passed.

## 7. Version isolation

This tool validates schema 0.2 descriptions only. The legacy `scripts/validate_semantics.py` remains the schema 0.1/0.9 validator. Schema 0.1 and its historical fixtures/workflows remain available for reproducibility.
