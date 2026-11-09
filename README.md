# DUSRM
## DMJ Universal Systems Reference Model

**Status:** Research proposal — working draft  
**Current specification:** 0.4-draft  
**Maturity:** Conceptual; not yet validated or normative

DUSRM is a proposed universal reference framework for describing, analyzing, designing, and evaluating computing and engineering systems. It is intended to provide a common conceptual foundation from which domain-specific reference models may be developed.

DUSRM is a **reference model, not an implementation, API, protocol, runtime, operating system, modeling language, or mandatory software architecture**. It must remain implementation-neutral and useful independently of any particular vendor, programming language, platform, or DMJ technology.

## Current milestone: DUSRM-0.4 — Operational Semantics

The 0.4 working draft defines how a system's behavior can be described over time. It introduces:
- operation specifications and execution occurrences;
- abstract execution lifecycle states;
- configurations and a transition-system kernel;
- safety and progress properties;
- event occurrence, observation, processing time, and clock domains;
- concurrency, causality, synchronization, and partial failure;
- failure, degradation, and recovery semantics;
- cross-layer operational rules and feedback;
- exploratory operational mappings for ANANTA and FireBot.

See [DUSRM 0.4 status](specification/DUSRM-0.4/STATUS.md).

## Previous milestone: DUSRM-0.3 — Structural Architecture

The 0.3 draft compares strict layering, multiple viewpoints, graph/ontology, hierarchy, and hybrid approaches. Its current candidate is a hybrid structure with a context frame, eight responsibility layers, a typed relationship graph, cross-cutting concerns, and viewpoints.

See [DUSRM 0.3 status](specification/DUSRM-0.3/STATUS.md).

## Previous milestone: DUSRM-0.2 — Foundational Ontology

The 0.2 draft introduced a distinction between the reference-model vocabulary, the system of interest, and the description representing that system; a first ontology, relationship catalogue, glossary, and informal notation.

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

## Current conceptual dimensions

The ten dimensions introduced in 0.1 remain research concepts. They are not automatically equivalent to the eight candidate layers. Their mapping must be documented and reviewed before the ontology or architecture is stabilized.

## Relationship to DMJ technologies

DUSRM must be capable of describing systems that use technologies such as ANANTA, CONTRACT, CALLGRAPH, OCTET, DATAGRAM, Telegraph, Relay, and MAINTAIN.ai. It must not depend on any of them.

These technologies remain independently specified. DUSRM may map their roles to its concepts, but must not redefine or duplicate their APIs, protocols, data formats, or engine behavior.

## Development roadmap

- **M0 — Research and prior art:** initial survey recorded; further research remains open.
- **M1 — Ontology:** DUSRM 0.2 working draft.
- **M2 — Structural model:** DUSRM 0.3 candidate hybrid structure; validation ongoing.
- **M3 — Operational semantics:** DUSRM 0.4 working draft.
- **M4 — Formalization:** refine semantics, invariants, constraints, proof obligations, and traceability.
- **M5 — Validation:** apply the model to independent case studies, including ANANTA and FireBot, and revise based on gaps.
- **M6 — Conformance and publication:** publish stable specifications, examples, review records, and conformance guidance.

## Repository map

- `specification/` — versioned normative and informative documents
- `semantics/` — operational, temporal, concurrency, and failure semantics
- `terminology/` — controlled vocabulary and definitions
- `ontology/` — entities and relationships
- `architecture/` — candidate structures and diagrams
- `research/` — prior-art reviews, papers, and rationale
- `validation/` — case studies and model evaluation
- `conformance/` — conformance criteria and tests
- `examples/` — illustrative mappings to real systems

## Document status and contribution

This repository is an open research draft. Proposed dimensions and definitions are not normative. Changes should include rationale, prior-art consideration, affected concepts, and validation implications. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md).

No claim of formal standardization, external adoption, or validation is made.
