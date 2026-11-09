# DUSRM
## DMJ Universal Systems Reference Model

**Status:** Research proposal — working draft  
**Current specification:** 0.5-draft  
**Maturity:** Conceptual; not yet validated or normative

DUSRM is a proposed universal reference framework for describing, analyzing, designing, and evaluating computing and engineering systems. It is intended to provide a common conceptual foundation from which domain-specific reference models may be developed.

DUSRM is a **reference model, not an implementation, API, protocol, runtime, operating system, modeling language, or mandatory software architecture**. It must remain implementation-neutral and useful independently of any particular vendor, programming language, platform, or DMJ technology.

## Current milestone: DUSRM-0.5 — Formalization

The 0.5 working draft introduces:
- a compact formal metamodel linking elements, responsibilities, layers, relationships, states, operations, executions, configurations, transitions, and claims;
- responsibility-based layer allocation, allowing one element to realize responsibilities across multiple layers;
- structural well-formedness and consistency rules;
- invariant and proof-obligation templates;
- traceability and staged conformance foundations;
- a reusable domain-profile template;
- a consistency review of ambiguities found in previous drafts.

See [DUSRM 0.5 status](specification/DUSRM-0.5/STATUS.md).

## Previous milestone: DUSRM-0.4 — Operational Semantics

The 0.4 working draft defines how a system's behavior can be described over time, including operation specifications, execution occurrences, state transitions, time, concurrency, failure, recovery, and cross-layer behavior.

See [DUSRM 0.4 status](specification/DUSRM-0.4/STATUS.md).

## Previous milestone: DUSRM-0.3 — Structural Architecture

The 0.3 draft proposes a hybrid structure with a context frame, eight responsibility layers, a typed relationship graph, cross-cutting concerns, and multiple viewpoints.

See [DUSRM 0.3 status](specification/DUSRM-0.3/STATUS.md).

## Previous milestone: DUSRM-0.2 — Foundational Ontology

The 0.2 draft introduced the separation between reference-model vocabulary, system of interest, and system description, plus a first ontology, relationship catalogue, glossary, and informal notation.

See [DUSRM 0.2 status](specification/DUSRM-0.2/STATUS.md).

## Goals

- Establish a precise, reusable vocabulary for describing systems.
- Describe systems through entities, boundaries, states, operations, resources, relationships, constraints, and environments.
- Provide a consistent basis for domain-specific reference models.
- Help engineers reason about system structure, behavior, responsibilities, and assurance.
- Support practical application to software, databases, distributed platforms, robotics, and cyber-physical systems.
- Permit implementations to use existing standards or custom technologies without making either a prerequisite.

## Non-goals

DUSRM does not:
- Replace OSI, TCP/IP, programming language runtimes, operating-system architectures, or domain-specific standards.
- Specify a new API, wire protocol, serialization format, database engine, or transport.
- Replace system life-cycle process standards, architecture-description standards, or general-purpose systems modeling languages.
- Require every implementation to contain eight deployed modules or eight physical components.
- Prescribe a particular implementation technology.
- Claim novelty merely by renaming established concepts.

## Core architecture principles

- Responsibilities, not whole components, are assigned to the eight core layers.
- Elements may realize responsibilities in multiple layers.
- Cross-layer relationships are explicit and do not imply a fixed execution pipeline.
- Cross-cutting concerns apply across relevant layers, elements, and relationships.
- Operations are distinct from execution occurrences.
- A system description is distinct from the system of interest.
- Formal claims require assumptions, scope, method, and evidence.

## Relationship to DMJ technologies

DUSRM must be capable of describing systems that use technologies such as ANANTA, CONTRACT, CALLGRAPH, OCTET, DATAGRAM, Telegraph, Relay, and MAINTAIN.ai. It must not depend on any of them.

These technologies remain independently specified. DUSRM may map their roles to its concepts, but must not redefine or duplicate their APIs, protocols, data formats, or engine behavior.

## Development roadmap

- **M0 — Research and prior art:** initial scope survey recorded; further research remains open.
- **M1 — Ontology:** DUSRM 0.2 working draft.
- **M2 — Structural model:** DUSRM 0.3 candidate hybrid structure.
- **M3 — Operational semantics:** DUSRM 0.4 working draft.
- **M4 — Formalization:** DUSRM 0.5 working draft.
- **M5 — Validation and profiles:** apply DUSRM to independently evidenced systems, including ANANTA and FireBot, and revise based on gaps.
- **M6 — Conformance and publication:** publish stable specifications, examples, review records, and conformance guidance.

## Repository map

- `specification/` — versioned reference-model documents
- `formalization/` — metamodel, allocation rules, invariants, and proof obligations
- `semantics/` — operational, temporal, concurrency, and failure semantics
- `ontology/` — entities and relationships
- `architecture/` — structural candidates and layer definitions
- `research/` — prior-art reviews and rationale
- `validation/` — case studies and model evaluation
- `conformance/` — conformance criteria and assessments
- `examples/` — illustrative system descriptions and profiles

## Document status and contribution

This repository is an open research draft. Proposed dimensions, layer definitions, and formal rules are not normative. Changes should include rationale, prior-art consideration, affected concepts, and validation implications. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md).

No claim of formal standardization, external adoption, machine-checked verification, or independent validation is made.
