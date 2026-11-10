# DUSRM 1.0 Preparation — WP4 Schema 0.2 Semantic Validator

**Work package:** WP4 — Schema 0.2 Semantic Validator and Migration Tooling  
**Status:** Implemented draft; non-normative  
**Schema:** urn:dusrm:schema:description:0.2-draft

## 1. Purpose

JSON Schema 0.2 checks the structural contract and relationship endpoint kinds. It cannot establish whether typed references resolve across collections or whether records agree with one another.

The WP4 semantic validator adds deterministic cross-record checks after schema validation. It is an engineering consistency aid, not a conformance certifier or proof that the described system behaves as claimed.

## 2. Command line

From the repository root:

```bash
python scripts/validate_semantics_0_2.py schema/fixtures/0.2/valid-minimal.json
python scripts/validate_semantics_0_2.py schema/fixtures/0.2/valid-sand-os-architecture.json
python scripts/validate_semantics_0_2.py path/to/description.json --json
```

Optional arguments:
- `--schema PATH` selects a schema 0.2 JSON Schema file.
- `--registry PATH` selects the profile registry.
- `--no-registry` skips profile checks.
- `--json` emits machine-readable findings.

The CLI performs structural validation first. If the document fails schema 0.2, semantic checking does not proceed.

Exit behavior:
- **0:** no semantic errors; warnings may be present and are printed.
- **1:** structural or semantic errors.
- **2:** input/schema/registry loading or schema-definition failure.

## 3. Semantic check catalogue

| Finding code | Severity | Check |
|---|---|---|
| DUSRM-02-M-000 | Error | Description root must be an object |
| DUSRM-02-M-001 | Error | IDs are unique across modeled object collections, including Realization records |
| DUSRM-02-M-002 | Error | Typed references and evidence references resolve |
| DUSRM-02-M-003 | Error | Typed reference kind is permitted at the use site |
| DUSRM-02-M-010 | Error | Evidence references resolve |
| DUSRM-02-M-012 | Error | Duplicate element-to-responsibility realization pairs are rejected |
| DUSRM-02-M-013 | Warning | In-progress or implemented responsibility has no realizing element |
| DUSRM-02-M-014 | Error | Duplicate layer-applicability declarations and responsibility/applicability conflicts |
| DUSRM-02-M-015 | Error | Relationship scope cannot silently refer to a different SOI |
| DUSRM-02-M-016 | Error | transitionsTo endpoints must belong to the same state variable |
| DUSRM-02-M-017 | Error | Execution timestamps and time ordering are consistent with execution state |
| DUSRM-02-M-018 | Error | State value belongs to its variable's declared finite domain, when defined |
| DUSRM-02-M-019 | Error / Warning | Transition source and destination share a state variable; transition subject is checked against state ownership |
| DUSRM-02-M-020 | Error | Interface and interaction participant-role assignments are consistent |
| DUSRM-02-M-021 | Error | Responsibility parent hierarchy is not self-referential or cyclic |
| DUSRM-02-M-022 | Error / Warning | Allocation validity, units and declared resource capacity are checked |
| DUSRM-02-E-001 | Error | Implemented realization and assessed-claim evidence discipline |
| DUSRM-02-E-002 | Warning | Passing assessment lacks evidence explicitly marked as supporting |
| DUSRM-02-E-003 | Warning | Evidence kind and evidence-producing method appear inconsistent |
| DUSRM-02-P-001 | Error / Warning | Profile exists and version matches; compatibility is not assumed unless explicitly approved |

The implementation intentionally emits warnings where the record may be meaningful but needs engineering judgement. It does not convert uncertainty into an error simply to force a binary result.

## 4. Checks performed

The validator currently checks:
- globally unique identifiers for the indexed object collections;
- typed reference existence and endpoint-kind rules;
- Realization references, duplicate pairs, implementation-state conflicts and unmapped responsibilities;
- responsibility parent references and hierarchy cycles;
- layer applicability uniqueness and conflicts with assigned responsibilities;
- relationship endpoints and selected scope/state semantics;
- operation owners, execution operation/subject references and execution time fields;
- event sources, state-variable subjects, state domains and transition consistency;
- interface contracts, participant roles, operation references and interaction-to-interface role agreement;
- resource owners, allocation participants, allocation time order, capacity and units;
- capability/service providers, operation/capability/interface/consumer references;
- requirement sources, constraint/invariant/assertion/decision subjects;
- evidence references, selected evidence-method consistency, assessment evidence and profile-registry status.

## 5. Deliberate limits

The validator does **not**:
- decide whether the eight-layer architecture is complete or well designed;
- prove a responsibility has been allocated to the correct layer;
- infer relationship symmetry, transitivity, inverse, causality or authority;
- establish that an interface is reachable or that an operation executes;
- assess evidence independence, freshness, sufficiency or truth automatically;
- perform full profile-composition compatibility analysis;
- prove safety, security, reliability, real-time behavior or implementation conformance;
- replace domain review, hazard analysis, testing, formal proof or certification.

A clean result means only that this validator found no errors in the subset of rules it implements.

## 6. Version boundaries

This tool validates schema 0.2 descriptions only. The 0.9 validator and schema 0.1 remain separate and unchanged. New semantic rules must be added with regression tests and a documented change to the 0.2 draft contract.
