# DUSRM 0.3 — Structural Architecture Status

**Status:** Candidate architecture; non-normative  
**Milestone:** M2 — Structural Model  
**Release label:** 0.3-draft  
**Date:** 2026-11-09

## Objective

Select and document a structural form that makes the DUSRM ontology practical for engineering while supporting both layered and non-layered relationships.

## Included

- Comparative evaluation of strict layers, viewpoints, graph ontology, hierarchy, and hybrid structure.
- Prior-art lessons from OSI, RM-ODP, ISO/IEC/IEEE 42010, ISO/IEC/IEEE 15288, and OMG SysML v2.
- A candidate hybrid structure.
- Eight responsibility layers with draft definitions.
- A context frame, typed relationship graph, cross-cutting concerns, and viewpoints.
- Layer contract template and allocation rules.
- Initial validation mappings for ANANTA and FireBot.

## Candidate eight layers

1. L1 — Physical and Infrastructure Foundation
2. L2 — Resource and Abstraction
3. L3 — Execution and Control
4. L4 — Information and State
5. L5 — Computation and Transformation
6. L6 — Interaction and Coordination
7. L7 — Capabilities and Services
8. L8 — Application and Mission Outcomes

The ordering and definitions remain open to revision.

## Key architecture decision

**Current recommendation:** hybrid structure.

The layered responsibility view is combined with:
- a context frame;
- a typed relationship graph;
- cross-cutting concern overlays;
- multiple viewpoints.

The layers are not required to correspond one-to-one with deployed components, programs, or technologies. Non-adjacent dependencies and feedback are permitted when explicitly modeled.

## Validation status

Initial conceptual mappings have been written for:
- ANANTA, with implementation details marked as unknown where they have not been verified against its actual repository.
- FireBot, with planned capabilities distinguished from verified implementation.

These mappings are not evidence that the systems conform to DUSRM. They are exploratory tests used to identify gaps.

## Open issues

- Validate the ordering and boundaries of L3, L4, and L5.
- Review the breadth of L6.
- Review the distinction between L7 and L8.
- Confirm whether the context frame is sufficient for systems-of-systems.
- Determine whether additional cross-cutting concerns are needed.
- Define formal layer allocation and relationship semantics.
- Compare DUSRM descriptions with existing modeling tools, without duplicating them.

## Next milestone

**M3 — Operational Semantics**

Define how operations, executions, events, states, transitions, time, concurrency, failure, and feedback behave across the proposed structure.
