# DUSRM 0.4 — Operational Semantics Status

**Status:** Working draft; non-normative  
**Milestone:** M3 — Operational Semantics  
**Release label:** 0.4-draft  
**Date:** 2026-11-09

## Objective

Define a common vocabulary and an initial abstract basis for describing how systems operate over time, including operations, executions, states, events, transitions, concurrency, temporal constraints, failure, recovery, and feedback.

## Included

- Operation specification versus execution occurrence.
- An abstract execution lifecycle.
- Enabling, admission, effects, and completion concepts.
- Configuration and transition-system notation.
- Safety and progress property distinction.
- Event occurrence, observation, and processing times.
- Clock-domain and temporal-constraint vocabulary.
- Concurrency, causality, ordering, and synchronization concepts.
- Failure, degradation, diagnosis, containment, and recovery vocabulary.
- Cross-layer operational rules.
- Generic worked trace.
- Exploratory operational questions for ANANTA and FireBot.
- Initial prior-art notes for TLA+, UML/SysML state machines, and systems engineering references.

## Abstract formal kernel

The draft uses an introductory transition-system tuple:

`M = (C, A, →, C₀)`

where C is the set of configurations, A the set of step labels, → the transition relation, and C₀ the admissible initial configurations.

This is a conceptual kernel only. Time, concurrency, fairness, uncertainty, and refinement require additional semantics. No executable language or model checker is defined.

## Important boundaries

- DUSRM is not TLA+, UML, SysML, a process algebra, a scheduler, a control system, or a distributed protocol.
- A valid abstract trace does not prove that an implementation produced the trace.
- A timeout does not necessarily prove a remote operation failed.
- A command acknowledgment does not prove a physical effect.
- A planned behavior is not an implemented or verified behavior.
- DUSRM does not replace safety engineering or domain-specific assurance.

## Next work

**M4 — Formalization and consistency**

- Define precise relationship and state semantics.
- Refine time, causality, concurrency, and failure assumptions.
- Define layer allocation and cross-layer traceability constraints.
- Prepare candidate invariants and proof obligations.
- Review the ontology and structure for contradictions.
- Establish a validation plan before claiming conformance.
