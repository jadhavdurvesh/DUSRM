# DUSRM
## DMJ Universal Systems Reference Model

**Status:** Research proposal — working draft  
**Current specification:** 0.9-draft  
**1.0 preparation:** WP1–WP5 internally prepared; structural, semantic, profile-fixture and legacy CI passed; independent review pending  
**Maturity:** Provisional reference framework; not normative or independently validated

DUSRM is a proposed universal reference framework for describing, analyzing, designing, and evaluating computing and engineering systems. It is intended to provide a common conceptual foundation from which domain-specific reference models may be developed.

DUSRM is a **reference model, not an implementation, API, protocol, runtime, operating system, modeling language, or mandatory software architecture**. It must remain implementation-neutral and useful independently of any particular vendor, programming language, platform, or DMJ technology.

## Current milestone: DUSRM-0.9 — Advanced System Modeling and Verification

The 0.9 draft adds:
- conservative participant-signature checks for selected relationship types in the semantic validator;
- regression tests for valid and invalid relationship endpoints;
- a distributed arbitration model for local claims, partitions and authoritative assignment;
- a FireBot emergency-stop and manual/autonomous precedence model;
- an ANANTA single-writer and WAL crash-recovery model;
- DUSRM-to-TLA+ mappings, assumptions and limits;
- CI that runs the schema, semantic suite and all four formal models.

The complete [0.9 CI run #6](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42657987718) passed. Twelve semantic tests passed and all four TLC models completed without errors. This is bounded model checking, not implementation verification or safety certification.

See [DUSRM 0.9 status](specification/DUSRM-0.9/STATUS.md) and [validation results](validation/0.9-VALIDATION-RESULTS.md).

## DUSRM 1.0 preparation

The 1.0 preparation work is tracked separately from the 0.9 draft:

- **WP1 — Layer Definitions and Boundaries:** eight responsibility-layer definitions, boundary tests and external-dependency treatment. [Status](specification/DUSRM-1.0/M1-STATUS.md)
- **WP2 — Foundational Ontology and Relationship Consolidation:** core model objects, relationship semantics and orthogonal evidence/status model. [Status](specification/DUSRM-1.0/M2-STATUS.md)
- **WP3 — Typed Metamodel and Schema 0.2:** separately versioned JSON Schema, typed relationship endpoints, SAND OS architecture fixture and migration guidance. [Status](specification/DUSRM-1.0/M3-STATUS.md)
- **WP4 — Semantic Validator and Migration Tooling:** typed reference resolution, global ID checks, semantic consistency checks and loss-aware 0.1→0.2 migrator. [Status](specification/DUSRM-1.0/M4-STATUS.md)
- **WP5 — Domain Profile Reconciliation:** standalone application, ANANTA and FireBot schema 0.2 profile pilots, compatibility matrix, evidence snapshot and independent-review cases. [Status](specification/DUSRM-1.0/M5-STATUS.md)

The final [WP5 profile validation run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43019955491) passed on 2026-11-11. Twenty-two schema 0.2 semantic/migration tests and four profile tests passed. All three profile fixtures had zero semantic errors and the expected one-warning not-assessed compatibility result. The [schema 0.1](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43019955486), [0.8](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43019955487) and [0.9](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43019955712) workflows also passed on the tested commit.

**Important:** none of the three profiles has been approved as compatible. ANANTA's inspected sources contain a Windows checkpoint-rotation wording conflict, and FireBot's inspected current-state snapshot is dated 2026-10-11. See the [WP5 reconciliation report](specification/DUSRM-1.0/M5-RECONCILIATION.md) and [review package](specification/DUSRM-1.0/M5-REVIEW-PACKAGE.md).

The next phase is **WP6 — Independent Review Findings and Release Candidate Gate**. CI results are internal engineering evidence, not peer approval or a stable 1.0 release.

## Previous milestones

- **0.8 — Semantic validation and formal-methods integration:** semantic validator, CLI, unit tests and a TLA+ task-completion pilot. [Status](specification/DUSRM-0.8/STATUS.md)
- **0.7 — Conformance and tooling readiness:** description JSON Schema, profile compatibility policy, consistency checks, fixtures and review package. [Status](specification/DUSRM-0.7/STATUS.md)
- **0.6 — Validation and domain profiles:** standalone application, ANANTA and FireBot case studies, evidence register and validation method. [Status](specification/DUSRM-0.6/STATUS.md)
- **0.5 — Formalization:** formal metamodel, responsibility allocation, consistency rules, invariants and traceability. [Status](specification/DUSRM-0.5/STATUS.md)
- **0.4 — Operational semantics:** operations, executions, states, transitions, events, time, concurrency, failure and recovery. [Status](specification/DUSRM-0.4/STATUS.md)
- **0.3 — Structural architecture:** candidate hybrid structure, eight responsibility layers, relationship graph, cross-cutting concerns and viewpoints. [Status](specification/DUSRM-0.3/STATUS.md)
- **0.2 — Foundational ontology:** system-of-interest, system description, ontology, relationships, glossary and notation. [Status](specification/DUSRM-0.2/STATUS.md)

## Core architecture principles

- Responsibilities, not whole components, are assigned to the eight candidate layers.
- Elements may realize responsibilities in multiple layers.
- Cross-layer relationships are explicit and do not imply a fixed execution pipeline.
- Cross-cutting concerns apply across relevant layers, elements, and relationships.
- Operations are distinct from execution occurrences.
- A system description is distinct from the system of interest.
- Formal claims require assumptions, scope, method, and evidence.
- Validation maturity distinguishes planned, simulated, implemented, tested, observed, and verified claims.

## Relationship to DMJ technologies

DUSRM must be capable of describing systems that use technologies such as ANANTA, CONTRACT, CALLGRAPH, OCTET, DATAGRAM, Telegraph, Relay, and MAINTAIN.ai. It must not depend on any of them.

These technologies remain independently specified. DUSRM may map their roles to its concepts, but must not redefine or duplicate their APIs, protocols, data formats, or engine behavior.

## Development roadmap

- **M0 — Research and prior art:** initial scope survey; further research remains open.
- **M1 — Ontology:** 0.2 working draft.
- **M2 — Structural model:** 0.3 candidate hybrid structure.
- **M3 — Operational semantics:** 0.4 working draft.
- **M4 — Formalization:** 0.5 working draft.
- **M5 — Validation and profiles:** 0.6 working draft.
- **M6 — Conformance and tooling readiness:** 0.7 proposal.
- **M7 — Semantic validation and formal-methods pilot:** 0.8 draft.
- **M8 — Advanced system modeling and verification:** 0.9 draft.
- **DUSRM 1.0 preparation — WP1:** layer definitions and boundaries. [Status](specification/DUSRM-1.0/M1-STATUS.md)
- **DUSRM 1.0 preparation — WP2:** ontology and relationship consolidation. [Status](specification/DUSRM-1.0/M2-STATUS.md)
- **DUSRM 1.0 preparation — WP3:** typed metamodel and schema 0.2. [Status](specification/DUSRM-1.0/M3-STATUS.md)
- **DUSRM 1.0 preparation — WP4:** semantic validator and migration tooling. [Status](specification/DUSRM-1.0/M4-STATUS.md)
- **DUSRM 1.0 preparation — WP5:** domain profile reconciliation and independent-review preparation. [Status](specification/DUSRM-1.0/M5-STATUS.md)
- **Next work package:** WP6 — independent review findings and release candidate gate.

## Repository map

- `specification/` — versioned reference-model documents
- `schema/` — machine-readable description schemas and fixtures
- `scripts/` — schema, semantic validation and migration tools
- `tests/` — validator, profile and migration regression tests
- `formal/` — external formal-methods pilots and mappings
- `formalization/` — metamodel, allocation rules, invariants, proof obligations
- `semantics/` — operational, temporal, concurrency, and failure semantics
- `profiles/` — domain profiles and compatibility policy
- `ontology/` — entities and relationships
- `architecture/` — candidate structures and layer definitions
- `research/` — prior-art reviews and rationale
- `validation/` — case studies, evidence and gap tracking
- `conformance/` — checks, fixtures and assessment procedures
- `review/` — independent review package and responses
- `examples/` — illustrative system descriptions

## Document status and contribution

This repository is an open research draft. Proposed dimensions, layer definitions, schema, and formal rules are not normative. Changes should include rationale, prior-art consideration, affected concepts, and validation implications. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md).

No claim of formal standardization, external adoption, complete semantic validation, or independent validation is made.
