# DUSRM 0.4 — Concurrency, Causality, and Coordination

**Document ID:** DUSRM-SEM-004  
**Status:** Working draft; non-normative  
**Version:** 0.4-draft

## 1. Purpose

This document defines how a DUSRM description records multiple concurrently progressing activities and the causal relationships between them.

DUSRM must not assume that a whole system performs one operation at a time or that every event has a single global order.

## 2. Concurrency

Two or more execution occurrences are concurrent when their progress may overlap within the chosen model and neither is defined as wholly dependent on completion of the other.

Concurrency may exist:
- within one processor or runtime;
- across processors or devices;
- across independent services;
- across networked systems;
- between physical activities and software processing.

Concurrency is a property of the modeled behavior at a declared abstraction level. It is not inferred merely from the fact that components are separate.

## 3. Interleaving and true parallelism

A model may represent concurrent behavior through an interleaving of individual steps. Interleaving is a modeling technique that serializes steps for analysis while preserving relevant possible orderings.

A model using interleaving does not claim the implementation is single-threaded or that physical events happen one at a time.

True parallel execution may also be modeled when simultaneous or overlapping actions matter to the system's semantics.

The chosen abstraction must be stated.

## 4. Causal order

DUSRM uses a candidate causal relation written as:

`e₁ ≺ e₂`

meaning event e₁ causally precedes event e₂ within the described system.

The relation should satisfy:
- **Irreflexivity:** no event causally precedes itself.
- **Transitivity:** if e₁ ≺ e₂ and e₂ ≺ e₃, then e₁ ≺ e₃.
- **Evidence or rule basis:** every asserted causal edge should arise from a declared rule, dependency, message relation, or observed mechanism.

If neither `e₁ ≺ e₂` nor `e₂ ≺ e₁` is known, the events are causally unordered in the description. This does not prove physical simultaneity.

## 5. Race and conflict

A potential race exists when concurrent executions access shared state or resources and at least one access can change that state or resource, such that the result may depend on ordering.

A DUSRM description should identify:
- shared subject or resource;
- relevant read, write, allocation, release, or control actions;
- permitted ordering or synchronization assumptions;
- required consistency or exclusivity property;
- detection, prevention, or resolution approach.

A race is a property of the modeled interaction, not simply a bug label. Whether a race is harmful depends on the declared requirements.

## 6. Synchronization

Synchronization establishes a relationship that constrains the ordering or coordination of activities.

Possible mechanisms (described abstractly) include:
- precedence dependencies;
- mutual exclusion;
- shared-state coordination;
- barriers or rendezvous;
- acknowledgment dependencies;
- clock synchronization;
- quorum or agreement conditions;
- resource reservations.

DUSRM does not prescribe concrete algorithms or protocols for these mechanisms. Their guarantees and failure behavior must be specified by the implementation or domain standard.

## 7. Consistency and atomicity

A description should state the consistency expectation for shared information or operations.

Examples of possible expectations include:
- atomic visibility at the modeled abstraction;
- sequentially ordered updates;
- eventual convergence under stated assumptions;
- monotonic observation;
- application-specific consistency invariants.

DUSRM does not impose a universal consistency model. "Atomic" must always be qualified by the operation and abstraction level at which atomicity is claimed.

## 8. Distributed coordination

A distributed system may have:
- independent local states;
- partial knowledge of remote state;
- delayed, duplicated, lost, or reordered messages;
- partitions or periods without connectivity;
- independent failures and recovery;
- no perfectly synchronized global clock.

Descriptions should identify:
- participants and membership assumptions;
- authority and coordination roles;
- information each participant can observe;
- required agreement or convergence properties;
- behavior during partial failure;
- rejoin, reconciliation, and recovery expectations.

Do not assume that one global state is directly observable by all participants.

## 9. Deadlock, livelock, starvation, and contention

- **Deadlock:** a set of activities cannot progress because each is waiting on conditions that cannot be satisfied under the current configuration.
- **Livelock:** activities continue changing state but do not make the required progress.
- **Starvation:** an eligible activity is indefinitely denied necessary progress or resources.
- **Contention:** multiple activities compete for a limited resource or shared capability.

These phenomena should be described with scope, assumptions, and progress requirements. A model should not claim freedom from them without analysis.

## 10. Fairness and progress assumptions

A progress property often depends on a scheduler, controller, network, resource manager, or environment eventually taking an enabled action.

The description should state any fairness or progress assumptions. For example:
- an enabled operation is eventually scheduled;
- a continuously available communication path eventually delivers a message;
- a resource is eventually released;
- a controller continues to run.

These are assumptions or guarantees to be justified, not default DUSRM behavior.

TLA+ provides an established way to express transition systems and fairness assumptions. DUSRM should use established formal tools where they fit.

Reference: https://lamport.azurewebsites.net/tla/high-level-view.html

## 11. Open questions

- What is the minimal universal coordination vocabulary?
- Should distributed membership and failure-detector assumptions have a separate reference profile?
- How should the model represent partial knowledge and conflicting observations?
- How should resource conflict and state conflict be distinguished?
- Which causality rules can be standardized without assuming a particular communication protocol?

## 12. Status

This is a draft description framework, not a consensus algorithm, distributed transaction protocol, scheduler, or concurrency-control implementation.
