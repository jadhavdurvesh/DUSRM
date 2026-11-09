# DUSRM
## DMJ Universal Systems Reference Model

**Status:** Research proposal — working draft  
**Current specification:** 0.2-draft  
**Maturity:** Conceptual; not yet validated or normative

DUSRM is a proposed universal reference framework for describing, analyzing, designing, and evaluating computing and engineering systems. It is intended to provide a common conceptual foundation from which domain-specific reference models may be developed.

DUSRM is a **reference model, not an implementation, API, protocol, runtime, operating system, modeling language, or mandatory software architecture**. It must remain implementation-neutral and useful independently of any particular vendor, programming language, platform, or DMJ technology.

## Current milestone: DUSRM-0.2 — Foundational Ontology

The 0.2 working draft introduces:
- A separation between the reference-model vocabulary, the system of interest, and the description representing that system.
- A first system ontology and controlled glossary.
- A proposed catalogue of typed relationships.
- An informal notation for discussion and examples.
- A prior-art scope review covering OSI, ISO/IEC/IEEE 15288, ISO/IEC/IEEE 42010, and OMG SysML v2.

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
- Require every system to use the same number of layers.
- Prescribe a particular implementation technology.
- Claim novelty merely by renaming established concepts.

## Current conceptual dimensions

The following are **research dimensions**, not finalized layers or a normative ordering:

| ID | Dimension | Research scope |
|---|---|---|
| D01 | Existence and Identity | What entities exist, how they are identified, and what makes a system distinguishable |
| D02 | Structure and Composition | How entities are organized, composed, and bounded |
| D03 | State and Change | State representation, ownership, transitions, and observability |
| D04 | Computation | Operations, transformations, dependencies, and computational meaning |
| D05 | Execution | Progress, scheduling, concurrency, interruption, and termination |
| D06 | Resources and Capabilities | Resource requirements, allocation, ownership, contention, and release |
| D07 | Interaction | Interfaces, exchanges, dependencies, and effects across boundaries |
| D08 | Coordination | Cooperation among components and independent systems |
| D09 | Governance and Assurance | Authority, constraints, invariants, policy, verification, and safety obligations |
| D10 | Evolution and Lifecycle | Initialization, configuration, adaptation, recovery, upgrade, and retirement |

These dimensions remain hypotheses. Research must determine whether they are orthogonal, hierarchical, cross-cutting, or best represented through another structure. Do not present them as OSI-like layers until this is justified.

## Relationship to DMJ technologies

DUSRM must be capable of describing systems that use technologies such as ANANTA, CONTRACT, CALLGRAPH, OCTET, DATAGRAM, Telegraph, Relay, and MAINTAIN.ai. It must not depend on any of them.

These technologies remain independently specified. DUSRM may map their roles to its concepts, but must not redefine or duplicate their APIs, protocols, data formats, or engine behavior.

## Development roadmap

- **M0 — Research and prior art:** survey established systems theories, reference models, systems engineering frameworks, formal methods, and domain standards.
- **M1 — Ontology:** refine definitions, entity types, relationships, boundaries, and assumptions. Current work is draft 0.2.
- **M2 — Structural model:** evaluate candidate structures (layered, dimensional, graph, or hybrid) and justify the choice.
- **M3 — Semantics:** define state, operation, transition, interaction, time, and failure semantics.
- **M4 — Formalization:** define invariants, constraints, notation, and traceability.
- **M5 — Validation:** apply the model to independent case studies, including ANANTA and FireBot, and revise based on gaps.
- **M6 — Conformance and publication:** publish stable specifications, examples, review records, and conformance guidance.

## Repository map

- `specification/` — versioned normative and informative documents
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
