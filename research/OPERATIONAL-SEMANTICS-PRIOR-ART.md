# DUSRM 0.4 — Operational Semantics Prior-Art Notes

**Status:** Initial research note; non-normative  
**Purpose:** Identify established formalisms relevant to DUSRM operational semantics.

## 1. Summary

DUSRM 0.4 uses established concepts from transition systems, state machines, temporal reasoning, concurrency models, and systems engineering. DUSRM must not claim these mathematical ideas as original.

The research contribution being explored is the way these concepts are organized and traced across a cross-domain, hybrid responsibility reference structure.

## 2. TLA+

Leslie Lamport's "A High-Level View of TLA+" explains state-machine specifications through an initial condition and a next-state relation. It also discusses behaviors, concurrency, fairness, and temporal properties.

**DUSRM relevance:**
- Initial configurations and permitted transitions;
- state-based descriptions;
- safety and progress properties;
- fairness assumptions for liveness;
- reasoning about concurrent and distributed systems.

**Boundary:** DUSRM's draft tuple M = (C, A, →, C0) is an introductory transition-system notation. It is not TLA+, does not define TLA+ syntax, and is not a replacement for a model checker.

Source: https://lamport.azurewebsites.net/tla/high-level-view.html

## 3. UML and SysML state machines

OMG's UML specification provides an established modeling approach for state machines. State-machine concepts include states, transitions, events, guards, and associated behavior. SysML also includes state-machine modeling for discrete behavior.

**DUSRM relevance:**
- State and transition vocabulary;
- event-triggered behavior;
- guard conditions;
- nested and concurrent state concepts;
- mapping to an established modeling language.

**Boundary:** DUSRM does not define another general-purpose state-machine notation. Its informal notation is explanatory only.

Sources:
- https://www.omg.org/spec/UML
- https://www.omg.org/spec/SysML
- https://www.omg.org/spec

## 4. Systems engineering lifecycle and behavior

NASA's Systems Engineering Handbook discusses system design, product realization, technical management, and lifecycle activities. It is a practical reference for the broader engineering context in which system behavior must be specified, integrated, and validated.

**DUSRM relevance:** operational semantics should support requirements, design, integration, verification, and operation, but should not be confused with a lifecycle process standard.

Source: https://www.nasa.gov/reference/systems-engineering-handbook/

## 5. Design boundaries for DUSRM

| Concern | Established research area | DUSRM position |
|---|---|---|
| States and transitions | State machines, transition systems | Reuse and map |
| Safety and liveness | Temporal logic, formal verification | Use as property categories; no new logic claimed |
| Concurrency | Process algebras, transition systems, distributed systems theory | Describe assumptions and relations; no scheduler prescribed |
| Event timing | Real-time systems, temporal models | Record clock domains and temporal constraints |
| Fault behavior | Dependability and safety engineering | Provide cross-layer vocabulary; no certification claim |
| Recovery | Fault-tolerant and distributed systems | Describe recovery semantics without mandating algorithms |
| Feedback | Control theory and cyber-physical systems | Describe reference/measurement/control relationships; no stability guarantee |

## 6. Research warning

The list above is an initial reference register, not a systematic literature review. Before a stable DUSRM release, the project should review relevant primary specifications and publications in sufficient depth, record edition/version details, and identify exact conceptual overlap.

No claim of novelty, completeness, or superiority is made in this document.
