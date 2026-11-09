# DUSRM
## DMJ Universal Systems Reference Model

**Status:** Research proposal — working draft  
**Current specification:** 0.6-draft  
**Maturity:** Conceptual; not yet validated or normative

DUSRM is a proposed universal reference framework for describing, analyzing, designing, and evaluating computing and engineering systems. It is intended to provide a common conceptual foundation from which domain-specific reference models may be developed.

DUSRM is a **reference model, not an implementation, API, protocol, runtime, operating system, modeling language, or mandatory software architecture**. It must remain implementation-neutral and useful independently of any particular vendor, programming language, platform, or DMJ technology.

## Current milestone: DUSRM-0.6 — Validation and Domain Profiles

The 0.6 working draft evaluates DUSRM using three system scopes:
- a small standalone software application;
- ANANTA, a native Rust database and data platform;
- FireBot, a software-first firefighting/rescue robot project with planned cyber-physical realization.

It introduces:
- an evidence-based validation procedure;
- standalone software, database-engine, and cyber-physical robotics profiles;
- repository-informed ANANTA and FireBot mappings;
- a source evidence register;
- case-study results, gap tracking, and reproducibility checklists;
- a draft description-assessment procedure.

The validation work is preliminary. ANANTA code/tests and FireBot simulation/tests were not executed as part of this DUSRM exercise. FireBot physical hardware and live network integration are not claimed as implemented.

See [DUSRM 0.6 status](specification/DUSRM-0.6/STATUS.md).

## Previous milestone: DUSRM-0.5 — Formalization

The 0.5 working draft introduced a compact formal metamodel, responsibility-based layer allocation, consistency rules, invariant and proof-obligation templates, and traceability foundations.

See [DUSRM 0.5 status](specification/DUSRM-0.5/STATUS.md).

## Previous milestone: DUSRM-0.4 — Operational Semantics

The 0.4 draft defines how behavior can be described over time, including operations, executions, state transitions, events, time, concurrency, failure, and recovery.

See [DUSRM 0.4 status](specification/DUSRM-0.4/STATUS.md).

## Previous milestone: DUSRM-0.3 — Structural Architecture

The 0.3 draft proposes a hybrid structure with a context frame, eight responsibility layers, a typed relationship graph, cross-cutting concerns, and multiple viewpoints.

See [DUSRM 0.3 status](specification/DUSRM-0.3/STATUS.md).

## Previous milestone: DUSRM-0.2 — Foundational Ontology

The 0.2 draft introduced the separation between reference-model vocabulary, system of interest, and system description, plus a first ontology, relationship catalogue, glossary, and informal notation.

See [DUSRM 0.2 status](specification/DUSRM-0.2/STATUS.md).

## Core architecture principles

- Responsibilities, not whole components, are assigned to the eight candidate layers.
- Elements may realize responsibilities in multiple layers.
- Cross-layer relationships are explicit and do not imply a fixed execution pipeline.
- Cross-cutting concerns apply across relevant layers, elements, and relationships.
- Operations are distinct from execution occurrences.
- A system description is distinct from the system of interest.
- Formal claims require assumptions, scope, method, and evidence.
- Validation maturity must distinguish documented, planned, simulated, implemented, tested, observed, and verified claims.

## Relationship to DMJ technologies

DUSRM must be capable of describing systems that use technologies such as ANANTA, CONTRACT, CALLGRAPH, OCTET, DATAGRAM, Telegraph, Relay, and MAINTAIN.ai. It must not depend on any of them.

These technologies remain independently specified. DUSRM may map their roles to its concepts, but must not redefine or duplicate their APIs, protocols, data formats, or engine behavior.

## Development roadmap

- **M0 — Research and prior art:** initial scope survey recorded; further research remains open.
- **M1 — Ontology:** DUSRM 0.2 working draft.
- **M2 — Structural model:** DUSRM 0.3 candidate hybrid structure.
- **M3 — Operational semantics:** DUSRM 0.4 working draft.
- **M4 — Formalization:** DUSRM 0.5 working draft.
- **M5 — Validation and profiles:** DUSRM 0.6 working draft.
- **M6 — Conformance and publication preparation:** refine assessment criteria, review profiles, and prepare stable documentation only after evidence and independent review.

## Repository map

- `specification/` — versioned reference-model documents
- `formalization/` — metamodel, allocation rules, invariants, and proof obligations
- `semantics/` — operational, temporal, concurrency, and failure semantics
- `profiles/` — domain-specific DUSRM profiles
- `ontology/` — entities and relationships
- `architecture/` — structural candidates and layer definitions
- `research/` — prior-art reviews and rationale
- `validation/` — case studies and model evaluation
- `conformance/` — assessment criteria and reports
- `examples/` — illustrative system descriptions

## Document status and contribution

This repository is an open research draft. Proposed dimensions, layer definitions, and formal rules are not normative. Changes should include rationale, prior-art consideration, affected concepts, and validation implications. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md).

No claim of formal standardization, external adoption, machine-checked verification, or independent validation is made.
