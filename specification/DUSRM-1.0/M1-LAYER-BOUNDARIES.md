# DUSRM 1.0 Preparation — Layer Boundary Decision Matrix

**Work package:** WP1 — Layer Definitions and Boundaries  
**Status:** Draft decision record; non-normative

## 1. Purpose

The 0.3 candidate structure identified several unresolved overlaps. This matrix converts them into explicit allocation tests so authors can assign responsibilities consistently.

## 2. Boundary decisions

### BD-01 — L1 substrate versus L2 resource

- L1 describes the physical or hosting substrate and its inherent conditions.
- L2 describes the capacity abstracted from that substrate and its allocation/ownership policy.
- Example: battery pack and wiring are L1; available watt-hours, reserve threshold, and load budget are L2.
- Example: disk device and host filesystem are L1; storage quota or space reservation is L2.

### BD-02 — L2 resource versus L3 execution

- L2 controls budgets, limits, reservations, contention, and release.
- L3 controls whether and how an operation executes.
- Example: maximum result-batch memory budget is L2; advancing the query iterator is L3.

### BD-03 — L3 execution versus L5 computation

- L3 determines when an operation instance runs, pauses, resumes, is cancelled, or terminates.
- L5 defines the computation the operation performs and the result it derives.
- Example: scheduling an AQL query is L3; parsing, planning, and evaluating AQL is L5.
- Example: starting a navigation task is L3; computing a route is L5.

### BD-04 — L4 information/state versus L5 computation

- L4 defines data meaning, identity, type, provenance, authority, and state.
- L5 defines transformations and reasoning over that information.
- Example: robot pose and its coordinate frame are L4; localization that estimates the pose is L5.
- Example: a database schema is L4; query optimization is L5.

### BD-05 — L4 information/state versus L6 interaction

- L4 defines what information means and how it is classified or trusted.
- L6 defines the contract by which participants exchange or request it.
- Example: telemetry field definitions and units are L4; the telemetry publishing/subscription contract is L6.

### BD-06 — L6 interaction versus L7 capability

- L6 specifies how participants interact, invoke, exchange, acknowledge, or coordinate.
- L7 names the coherent ability or service that a consumer receives.
- Example: the embedded request/result/error contract is L6; bounded query execution is a database capability at L7.
- Example: a fleet message contract is L6; fleet task coordination is a capability at L7.

### BD-07 — L7 capability versus L8 outcome

- L7 expresses what the system can provide.
- L8 expresses the stakeholder or mission outcome and the condition by which the outcome is judged.
- Example: "detect a person" is a capability at L7; "locate and support rescue of people" is an outcome at L8.
- Example: "execute analytical queries" is a capability at L7; "provide an independent data platform for analytical workloads" is a product/application outcome at L8.

### BD-08 — L8 mission workflow versus L3 execution

- L8 expresses end-to-end operational intent, objective, priority, and success conditions.
- L3 expresses the runtime progression and control of individual operation instances.
- Example: "search sector A before suppressing fire in sector B" is a mission policy/workflow at L8; dispatching the robot's next motion-control operation is L3.

## 3. Cross-layer activities

A phrase such as "perform a query", "navigate to a person", or "recover a database" may describe several distinct responsibilities. Do not assign the entire phrase to one layer.

Decompose it into the smallest useful responsibilities:
- information/state required (L4);
- computation or transformation (L5);
- execution lifecycle (L3);
- participant interaction contract (L6);
- capability exposed (L7);
- intended outcome (L8);
- substrate and resources required (L1/L2).

Do not decompose a real component into fictitious components. The responsibility descriptions are separate; the same component can realize several of them.

## 4. External dependencies and layer applicability

The host platform of a standalone application is not automatically an internal L1 component. Describe it as an external environment element and record the application's dependency on it. The layer can be marked **external dependency** for that system of interest.

Similarly:
- an external identity provider is an L6/L7 dependency depending on whether the statement concerns the interaction contract or capability consumed;
- an external network is an L1 infrastructure and/or L2 capacity dependency, depending on whether the statement concerns the substrate or available bandwidth;
- an external human operator is an actor in context and may participate in L6 interactions; the operator is not thereby an internal software component.

## 5. Allocation anti-patterns

Do not:
- assign a database wholly to L4 because it stores data;
- assign an API wholly to L6 without separating the capability exposed at L7;
- assign an AI model wholly to L5 if its deployment, execution, service capability, and mission role are also in scope;
- assign the entire robot to L1 because it is physical;
- assign all coordination to L6 when L3 controls local execution and L8 defines mission priorities;
- equate an implementation component with a layer;
- infer an adjacent-layer dependency from the order of the diagram.

## 6. Acceptance test

A layer boundary is usable when:
1. an author can state the responsibility as a concise verb-object phrase;
2. the primary layer can be selected using the decision question;
3. adjacent-layer confusion can be resolved without changing the responsibility's meaning;
4. cross-layer realization can be represented without duplicating the element;
5. the mapping can be explained in at least one software and one cyber-physical example.
