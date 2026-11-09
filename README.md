# DUSRM
## DMJ Universal Systems Reference Model

**Status:** Research proposal — working draft  
**Current specification:** 0.7-draft  
**Maturity:** Provisional reference framework; not normative or independently validated

DUSRM is a proposed universal reference framework for describing, analyzing, designing, and evaluating computing and engineering systems. It is intended to provide a common conceptual foundation from which domain-specific reference models may be developed.

DUSRM is a **reference model, not an implementation, API, protocol, runtime, operating system, modeling language, or mandatory software architecture**. It must remain implementation-neutral and useful independently of any particular vendor, programming language, platform, or DMJ technology.

## Current milestone: DUSRM-0.7 — Conformance and Tooling Readiness

The 0.7 draft introduces:
- a provisional JSON Schema Draft 2020-12 shape for system descriptions;
- profile compatibility policy and a provisional profile registry;
- a consistency-check catalogue separating schema, semantic, profile, evidence, and human-review checks;
- positive and negative conformance fixtures;
- a small CI check for schema validity and fixture expectations;
- a tooling-readiness plan and independent engineering review package.

The structural JSON Schema and fixture checks passed in [GitHub Actions run #5](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42648618733). The CI check does not implement semantic reference validation or establish profile compatibility, system conformance, safety, or correctness. The eight-layer model remains provisional.

See [DUSRM 0.7 status](specification/DUSRM-0.7/STATUS.md).

## Previous milestones

- **0.6 — Validation and domain profiles:** standalone application, ANANTA, and FireBot case studies, evidence register and validation method. [Status](specification/DUSRM-0.6/STATUS.md)
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
- **Next:** independent review, semantic-validator prototype, and resolution of core model gaps.

## Repository map

- `specification/` — versioned reference-model documents
- `schema/` — machine-readable description schema proposal
- `scripts/` — schema/fixture validation scripts
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

No claim of formal standardization, external adoption, machine-checked verification, or independent validation is made.
