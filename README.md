# DUSRM
## DMJ Universal Systems Reference Model

**Status:** Research proposal — working draft  
**Current specification:** 0.9-draft  
**1.0 preparation:** WP1 and WP2 documentation complete; WP3 schema 0.2 structural CI passed; independent review pending  
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

The 1.0 preparation work is tracked separately from the 0.9 draft. WP1 tightens the eight responsibility-layer definitions and boundary tests. WP2 consolidates the ontology, relationship semantics, and evidence/status model. WP3 introduces a separately versioned schema 0.2 draft, typed architecture fixtures including SAND OS, and a dedicated structural validation workflow. Its final CI run #4 passed the schema and all four positive/negative fixture expectations; the legacy 0.1, 0.8 and 0.9 workflows also passed. Independent review and semantic validation remain outstanding. See [WP1 status](specification/DUSRM-1.0/M1-STATUS.md), [WP2 status](specification/DUSRM-1.0/M2-STATUS.md), [WP3 status](specification/DUSRM-1.0/M3-STATUS.md), and the [DUSRM 1.0 preparation index](specification/DUSRM-1.0/README.md).

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
- **DUSRM 1.0 preparation — WP1:** layer definitions and boundaries (documentation complete; independent review pending). [Status](specification/DUSRM-1.0/M1-STATUS.md)
- **DUSRM 1.0 preparation — WP2:** foundational ontology, relationship semantics, and evidence/status model (documentation complete; independent review and schema work pending). [Status](specification/DUSRM-1.0/M2-STATUS.md)
- **DUSRM 1.0 preparation — WP3:** typed metamodel and schema 0.2 draft (automated validation pending). [Status](specification/DUSRM-1.0/M3-STATUS.md)
- **Next work package:** WP4 — schema 0.2 semantic validator and migration tooling.

## Repository map

- `specification/` — versioned reference-model documents
- `schema/` — machine-readable description schema proposal
- `scripts/` — schema and semantic validation tools
- `tests/` — validator regression tests
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
