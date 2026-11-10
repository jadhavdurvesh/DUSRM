# DUSRM 1.0 Preparation — Core Layer Charter

**Work package:** WP1 — Layer Definitions and Boundaries  
**Status:** Stabilization draft; non-normative  
**Target:** Proposed DUSRM 1.0 core  
**Decision authority:** Not yet approved; independent review remains required

## 1. Purpose

This charter tightens the eight candidate responsibility layers. Each layer is distinguished by the kind of responsibility being described, not by the technology, product, organization, or component that realizes it.

This is a 1.0-preparation revision. It does not declare DUSRM 1.0 stable and does not retroactively alter the historical DUSRM 0.3 draft.

## 2. Core modeling rules

### 2.1 Responsibilities are classified; components are not assigned wholesale

A responsibility has exactly one primary DUSRM layer. An element may realize multiple responsibilities, including responsibilities in different layers. The same element must not be duplicated merely to fit the layer view.

### 2.2 Layer order is an organizing convention, not an execution pipeline

The L1-to-L8 ordering is a reading convention from realization substrate toward intended outcomes. It does not prescribe call order, data-flow order, deployment order, control authority, dependency direction, or a mandatory interface between adjacent layers.

Actual dependencies, information exchange, control, containment, and feedback are represented by typed relationships. A system may connect any relevant layers directly.

### 2.3 Classify responsibilities, not technology names

Do not classify a product, repository, programming language, protocol, database, robot, or organization by name. State what it does in the system description, then assign each distinct responsibility to its primary layer.

### 2.4 Separate internal responsibilities from external dependencies

An external operating system, user, remote service, network, or physical environment may be necessary to the system of interest without becoming an internal element that realizes one of its responsibilities.

Record external participants in the context and relationship model. Mark a layer as an external dependency where relevant; do not claim the system internally realizes an external provider's responsibility.

### 2.5 Layer applicability states

For each layer in a particular system description, use one of these applicability states:
- **Internal:** a relevant responsibility is within the system boundary.
- **External dependency:** the system depends on a responsibility provided outside its boundary.
- **Planned:** the responsibility is intended but not yet realized.
- **Not applicable:** the responsibility is outside the system's purpose or scope.
- **Not modeled:** the concern may exist, but the description intentionally omits it.
- **Unknown:** available information is insufficient to decide.

These are applicability states, not implementation-maturity statuses. Planned is not the same as not applicable. An external dependency is not an internal realization.

## 3. The eight core layers

### L1 — Physical and Infrastructure Foundation

**Core question:** What physical or hosting substrate and environmental conditions enable or constrain the system?

**Owns**
- physical devices, mechanical structures, sensors, actuators, power sources, physical media, and facilities;
- compute, storage, and network infrastructure as deployed substrate;
- hosting and infrastructure topology at the realization level;
- physical and infrastructure operating limits that constrain system behavior.

**Does not own**
- capacity quotas, allocations, reservations, or policies over resources (L2);
- the lifecycle of an executing operation (L3);
- the meaning of stored information (L4);
- algorithms or mission policy (L5/L8).

**Boundary test:** If the question is "what substrate or environment physically/operationally exists, and what are its inherent limits?", use L1. If it is "how much capacity is available, reserved, shared, or allocated?", use L2.

**Examples**
- Standalone application: host computer, display, storage device, and host platform are usually external L1 dependencies.
- ANANTA: host CPU, memory devices, disks, and filesystem/OS substrate are infrastructure dependencies; ANANTA is not the substrate.
- FireBot: chassis, motors, cameras, LiDAR, batteries, wiring, and compute boards are L1 elements when included in the system boundary; if not yet built, their realization status is planned.

### L2 — Resource and Abstraction

**Core question:** What capacities or resources are represented, bounded, owned, reserved, shared, allocated, consumed, or released?

**Owns**
- resource quantities and capacities such as memory budgets, storage capacity, energy reserves, compute quotas, bandwidth, workspace, and actuator duty budgets;
- abstractions that represent those capacities to system responsibilities;
- allocation, reservation, ownership, sharing, contention, limits, and release rules;
- resource accounting and policies for admission or load shedding.

**Does not own**
- the physical substrate itself (L1);
- the execution lifecycle or scheduler step that uses a resource (L3);
- the algorithm that computes a result (L5);
- mission priorities that determine why an outcome matters (L8), though L2 may consume a priority policy as input.

**Boundary test:** If the statement can be expressed as a capacity, budget, quota, reservation, allocation, contention, or release condition, use L2. If it describes the action being run, use L3; if it describes the algorithm, use L5.

**Examples**
- Standalone application: process memory limits or local storage quotas; no network resource manager is implied.
- ANANTA: bounded result batches and execution row/cell/working-set limits, plus the documented single-writer ownership boundary.
- FireBot: battery reserve, power budget, load priority, compute budget, available communication capacity, and energy-based load shedding. A battery pack itself is L1; its available energy budget is L2.

### L3 — Execution and Control

**Core question:** How is an operation or activity admitted, activated, progressed, scheduled, coordinated during execution, interrupted, or terminated?

**Owns**
- execution occurrences and their lifecycle;
- dispatch, scheduling, sequencing, synchronization, and concurrency of active work;
- runtime control and arbitration over which permitted operation may proceed;
- cancellation, timeout handling, suspension, resumption, termination, and local execution status;
- execution-level feedback and actuator-command progression, when modeled at the operational level.

**Does not own**
- the logical meaning of an algorithm or the result it computes (L5);
- the state/data model itself (L4);
- the contract for exchanging requests or messages across participants (L6);
- the mission objective or acceptance outcome (L8).

**Boundary test:** If the question is "whether, when, and how this operation instance runs or is controlled", use L3. If the question is "what computation or transformation the operation means", use L5.

**Examples**
- Standalone application: dispatching a CompleteTask execution and handling its cancellation or completion.
- ANANTA: query execution lifecycle, pull-based iterator progression, cancellation, and the single-writer execution boundary.
- FireBot: local command arbitration, motion-control execution, emergency-stop state handling, and actuation lifecycle. A command decision rule is distinct from the perception or path-planning algorithm that supplies inputs.

### L4 — Information and State

**Core question:** What information is represented, what does it mean, who or what owns it, and how does its state change or persist?

**Owns**
- information identities, schemas, types, units, meanings, and provenance;
- modeled state, ownership, authority, validity, lifecycle, and consistency requirements;
- distinction between raw observations, estimates, derived information, and authoritative state;
- persistence, retention, versioning, and recovery requirements as information/state properties.

**Does not own**
- physical storage devices or memory hardware (L1);
- capacity quotas and allocation of storage resources (L2);
- query execution or update scheduling (L3);
- the algorithm that transforms information (L5);
- the interaction contract by which information is exchanged (L6).

**Boundary test:** If the question is "what does this datum or state represent, and what makes it valid or authoritative?", use L4. If it is "how is it computed or transformed?", use L5. If it is "how is it exchanged with another participant?", use L6.

**Examples**
- Standalone application: task identity, fields, completion status, and local persistence requirements.
- ANANTA: typed values, schemas, catalog identities, native data artifacts, WAL/checkpoint state, and recovery-visible metadata.
- FireBot: robot pose, mission state, sensor observations, detections, map data, battery measurements, and source/freshness/confidence metadata.

### L5 — Computation and Transformation

**Core question:** What defined computation, algorithm, evaluation, inference, or transformation produces a result from inputs?

**Owns**
- algorithmic and computational semantics;
- parsing, evaluation, planning, optimization, inference, analytics, estimation, and transformation logic;
- decision computations that derive a result from inputs and declared rules;
- computational preconditions, postconditions, and logical effects.

**Does not own**
- the runtime lifecycle or scheduling of the computation (L3);
- the meaning and authority of the input data model (L4);
- the communication mechanism or interaction contract used to request the computation (L6);
- the stakeholder's desired mission outcome or policy objective (L8).

**Boundary test:** If the question is "what transformation or reasoning produces this result from these inputs?", use L5. If it is "when does it run and how is it interrupted?", use L3. If it is "why is this result valuable or acceptable?", use L8.

**Examples**
- Standalone application: task validation, filtering, sorting, and derived counts.
- ANANTA: AQL parsing, planning, name/type resolution, optimization, vectorized query operations, and analytics.
- FireBot: person/fire perception algorithms, sensor fusion, mapping, localization, path planning, and thermal/scene analysis. Their outputs do not by themselves authorize actuation.

### L6 — Interaction and Coordination

**Core question:** What interaction contract or coordination relationship governs an exchange between distinct participants?

**Owns**
- participant-facing interfaces and interaction contracts;
- request/response, event, message, command, and observation exchange semantics;
- participant roles, interaction sequences, acknowledgments, correlation, and coordination obligations;
- cross-component, cross-service, operator/system, device/system, and system-to-system collaboration rules.

**Does not own**
- a specific API syntax, protocol, transport, encoding, or implementation;
- the internal execution lifecycle after an interaction is accepted (L3);
- the algorithm invoked by an interaction (L5);
- the useful capability exposed through one or more interactions (L7);
- the mission goal motivating the exchange (L8).

**Boundary test:** If distinct participants need a defined contract for how they exchange information, requests, commands, or coordination commitments, use L6. If the question is "what useful service can the consumer obtain?", use L7.

**Examples**
- Standalone application: user-interface event contracts and in-process component interaction; networking is not required.
- ANANTA: embedded API request/result/error contract and AQL client interaction; a network server is not implied.
- FireBot: operator/dashboard interaction, subsystem contracts, robot-to-station and fleet coordination semantics. Custom technologies may implement these contracts, but DUSRM does not redefine them.

### L7 — Capabilities and Services

**Core question:** What coherent, consumable capability does the system provide, and under what service conditions?

**Owns**
- externally meaningful capabilities and service offerings;
- capability boundaries, composition, availability, and declared service quality;
- service-level constraints and capability-level success/failure conditions;
- mapping from lower-level responsibilities to a capability a user, operator, application, or peer can consume.

**Does not own**
- the interaction contract or protocol used to access the capability (L6);
- the internal algorithm or execution mechanism (L3/L5);
- the stakeholder's broader objective, mission strategy, or desired operational outcome (L8).

**Boundary test:** If the statement can be phrased as "the system provides the ability to…", use L7. If it says "the system is intended to achieve…", use L8.

**Examples**
- Standalone application: create, edit, complete, delete, search, and organize tasks.
- ANANTA: schema management, ingestion, query execution, analytics, backup/restore, and other documented database capabilities, with their actual limitations.
- FireBot: detection, mapping, navigation assistance, operator alerting, firefighting support, diagnostics, and fleet coordination capabilities. Planned capabilities must remain labelled planned.

### L8 — Application and Mission Outcomes

**Core question:** What stakeholder, organizational, operational, or mission outcome is the system intended to achieve, and how is success judged?

**Owns**
- stakeholder needs, application purpose, mission objectives, and desired outcomes;
- operational goals, mission policy, priorities, and outcome-level constraints;
- end-to-end use cases and workflows from the stakeholder's perspective;
- outcome measures, acceptance conditions, and mission-level trade-offs.

**Does not own**
- the detailed algorithm that computes a result (L5);
- the runtime sequencing of individual execution occurrences (L3);
- the capability contract exposed to a consumer (L7);
- physical resource allocation or low-level interaction mechanisms (L1/L2/L6).

**Boundary test:** If the statement explains why the system exists, what the user/organization/mission seeks to accomplish, or what counts as end-to-end success, use L8.

**Examples**
- Standalone application: help one user reliably organize and track tasks.
- ANANTA: provide an independent native database/data platform for storage, querying, and analytical workloads.
- FireBot: support people-first search/rescue and firefighting operations while maintaining declared safety and operator-authority constraints. Real-world mission success remains unverified.

## 4. Boundary rules for commonly confused layers

| Distinction | First layer | Second layer | Decision question |
|---|---|---|---|
| Substrate vs resource capacity | L1 | L2 | Is it the device/platform, or the amount/ownership of capacity? |
| Resource allocation vs execution | L2 | L3 | Is it a budget/reservation, or the running/controlled activity? |
| Execution vs computation | L3 | L5 | Is it the lifecycle of running work, or the logic/result of the work? |
| Information vs computation | L4 | L5 | Is it the meaning/authority of information, or the transformation applied to it? |
| State vs interaction | L4 | L6 | Is it the state representation, or the contract for exchanging it? |
| Interaction vs capability | L6 | L7 | Is it how participants interact, or what useful ability is offered? |
| Capability vs outcome | L7 | L8 | Is it what the system can provide, or what the stakeholder wants to achieve? |
| Mission workflow vs execution sequence | L8 | L3 | Is it the operational goal/plan, or the runtime progression of operations? |

## 5. Cross-cutting concerns

Safety, security, identity, trust, governance, observability, evidence, lifecycle, time, uncertainty, and resilience are not additional layers. Each application of a cross-cutting concern must identify the affected element, responsibility, relationship, operation, transition, viewpoint, or system boundary; the constraint or assurance question; its owner and evidence status; and the relevant layer or layers it constrains.

A cross-cutting concern may affect all eight layers, but that does not create an additional layer or permit one layer to claim ownership of the entire concern.

## 6. Required allocation record

For each responsibility, record:
- stable responsibility identifier;
- concise verb-object statement;
- primary layer (exactly one);
- scope: internal responsibility or external dependency/context;
- realizing elements, if internal and known;
- applicability and maturity status;
- rationale using the boundary tests;
- relevant relationships and evidence.

An element may realize multiple responsibilities. A responsibility may be realized by multiple elements. An external participant is represented as an external context element and relationship, not falsely as an internal realization.

## 7. Interpretation and ordering

The authoritative architecture is the combination of the system context and boundary; responsibility-to-layer allocations; element-to-responsibility realizations; typed relationships; operational semantics; and cross-cutting concerns and viewpoints.

No dependency is inferred solely because two layers are adjacent.

## 8. Status

The eight definitions and boundaries are a proposed DUSRM 1.0 core charter. They require the review and acceptance process defined by the WP1 decision record. This charter does not freeze layer names or establish a stable 1.0 release.
