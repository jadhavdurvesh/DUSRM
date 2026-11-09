# DUSRM 0.2 — Core Ontology

**Document ID:** DUSRM-ONT-001  
**Status:** Working draft; non-normative  
**Version:** 0.2-draft

## 1. Purpose

This document defines the first proposed ontology for DUSRM: the concepts used to describe a system, the relationships among those concepts, and the separation between a system and its description.

The ontology is intended to support software, computing platforms, databases, distributed systems, robotics, and other engineered or cyber-physical systems. It is a conceptual reference, not an implementation schema or programming language.

## 2. Three distinct levels

DUSRM distinguishes three levels. Mixing them produces category errors.

### 2.1 Reference-model level

This is DUSRM itself: the vocabulary, definitions, relationship types, rules, and viewpoints used to describe systems.

Examples: the concepts `System`, `Element`, `Boundary`, `State`, and `Operation`.

### 2.2 Subject level

This is the real, planned, or hypothetical system being examined, called the **system of interest (SOI)**. It includes the entities and behavior that exist or are intended to exist in the subject domain.

Examples: an ANANTA database engine, a FireBot robot, a standalone application, or a sensor controller.

### 2.3 Description level

This is a particular description or model of the SOI, created using DUSRM concepts. It contains statements about the subject, selected viewpoints, assumptions, diagrams, traceability links, and supporting evidence.

A description is not the system itself. A diagram of a robot is not the robot; an architectural description of a database is not the database.

### 2.4 Separation rule

Every statement in a DUSRM description should be understood as one of:
- a definition in the reference model;
- an assertion about the SOI;
- an assumption or hypothesis about the SOI;
- a design decision or intended property;
- evidence supporting or challenging an assertion.

Descriptions should identify which category applies. Planned, implemented, observed, and hypothesized properties must not be silently mixed.

## 3. Scope and system of interest

A **system of interest (SOI)** is the entity, organized set of entities, or engineered arrangement selected for a particular analysis, design, operation, or assurance activity.

A system description must declare, at minimum:
- the subject being considered;
- the reason or purpose for considering it;
- the scope of the description;
- the system boundary at the chosen level of detail;
- the relevant environment and external dependencies;
- the status of its claims (for example, planned, implemented, observed, or assumed).

The boundary may be physical, logical, organizational, temporal, or analytical. It is a modeling decision, not necessarily a physical wall.

A system may itself be treated as a component of a larger system. A subsystem is a system considered as part of another system. This recursion is permitted; it does not require every system to be decomposed into the same number of levels.

## 4. Core ontology concepts

### 4.1 Element

An **element** is anything distinguishable and referable in a description of the SOI. An element may represent a physical thing, software construct, person or role, information item, process, capability, condition, or abstract concept.

An element in a description is a representation of a subject, not the subject itself.

### 4.2 System

A **system** is an SOI considered as an organized whole within a declared scope and boundary. A system has elements and relationships relevant to the reason it is being modeled.

A system is not required to be a software system, network, machine, or product. The model should remain useful for mixed hardware/software systems.

### 4.3 Component and subsystem

A **component** is an element considered in its role as a constituent of a particular system. Component-ness is contextual: the same subject may be a system in one description and a component in a larger system description.

A **subsystem** is a system that is included within a larger system's scope. Subsystems may have their own boundaries, environments, states, and descriptions.

Membership or decomposition does not automatically imply physical containment, ownership, or lifecycle control.

### 4.4 Environment

The **environment** is the set of external entities, conditions, events, and influences relevant to the SOI for the declared scope.

The environment is relative to the selected boundary. An element can be internal in one description and external in another.

### 4.5 Boundary

A **boundary** identifies what is inside, outside, or treated as crossing the scope of a system description. A boundary may be physical, logical, organizational, temporal, or analytical.

A boundary must be described at a useful level of precision. It should identify relevant inclusions, exclusions, and crossings. Boundary changes between descriptions must be explicit.

### 4.6 Interface

An **interface** is a specified point or boundary of interaction between participants. It describes the kinds of interactions that are permitted, expected, observable, or required.

An interface may be software-facing, hardware-facing, mechanical, electrical, informational, human, spatial, or organizational. An interface is not synonymous with an API or network protocol.

An interface description may refer to:
- participants or endpoints;
- interaction direction and roles;
- offered or required interactions;
- inputs, outputs, or exchanged items;
- preconditions, postconditions, constraints, and failure behavior;
- timing or quality properties when relevant.

DUSRM does not prescribe the syntax or wire-level behavior of an interface.

### 4.7 Relationship

A **relationship** is a typed assertion connecting two or more elements. It must have defined semantics; a line in a diagram without a declared meaning is not sufficient.

Relationships may be structural, behavioral, dependency-related, causal, temporal, allocation-related, or descriptive.

### 4.8 Property

A **property** is a characteristic attributed to an element or relationship. A property may be qualitative or quantitative, static or time-varying, measured or assumed.

Quantitative properties should identify units, reference conditions, uncertainty, and provenance where those matter.

### 4.9 State

A **state** is a modeled condition of a subject over a stated scope and time or interval. A state may summarize values of properties, modes, status, or other relevant conditions.

A state description should identify:
- the subject whose state is described;
- the properties or conditions included;
- the time, interval, or observation context;
- whether the state is observed, computed, expected, or assumed.

A state is not necessarily a single global mode. Different parts of a system may have simultaneous local states.

### 4.10 Operation and execution

An **operation** is a specified unit of behavior that a subject can perform or offer. An operation description may define its purpose, inputs, preconditions, outputs, effects, postconditions, and failure conditions.

An **execution** is an occurrence of behavior: an operation being performed, an activity taking place, or a process progressing over time.

The specification of an operation and a particular execution of it are different concepts. A method definition is not a method call; a motor-control capability is not a particular motor movement.

### 4.11 Event

An **event** is an occurrence represented as relevant to the system. Events may be internal or external, generated or observed, discrete or derived.

An event may trigger, enable, inhibit, or provide evidence for a transition. DUSRM does not assume that all events are instantaneous in the physical world; event granularity must be declared by the description.

### 4.12 Transition

A **transition** is a defined change from one modeled state or condition to another. A transition description may identify:
- the subject;
- source and destination states;
- triggering or enabling events;
- guard conditions;
- actions or effects;
- timing assumptions;
- failure or cancellation behavior.

A transition model is an abstraction. It need not imply that the entire system has one finite-state machine.

### 4.13 Resource

A **resource** is an entity, capacity, or means that can be required, allocated, occupied, consumed, shared, or controlled by an operation or system.

Examples include processor time, memory capacity, stored energy, network capacity, sensors, workspace, and human attention. Resources may be finite, replenishable, shared, exclusive, or non-physical.

Descriptions should identify relevant capacity, availability, ownership or control, allocation, contention, and release semantics.

### 4.14 Capability

A **capability** is a defined ability to perform an operation, provide a service, interact, or access a resource under stated conditions.

Capability is not the same as permission. A system may technically be capable of an action but not authorized to perform it. Where relevant, technical capability and granted authority must be modeled separately.

### 4.15 Constraint and invariant

A **constraint** is a condition restricting allowable structure, properties, states, operations, transitions, or relationships.

An **invariant** is a constraint that is required to remain true throughout a declared scope or set of conditions. An invariant must state its scope and assumptions.

A constraint may be violated in an observed system; the description should distinguish the rule from evidence that it is satisfied.

### 4.16 Requirement

A **requirement** is a documented obligation, need, or condition that a system or element is expected to satisfy. Requirements may originate from stakeholders, regulation, hazards, interfaces, contracts, or derived engineering decisions.

A requirement is not itself proof of implementation or satisfaction. It may be mapped to one or more constraints, elements, operations, tests, or evidence items.

### 4.17 Evidence and assertion

An **assertion** is a statement made in a system description about the SOI, a requirement, or a design decision.

**Evidence** is information used to support, refute, qualify, or trace an assertion. Evidence may be a test result, measurement, analysis, inspection, source document, or observation.

Each significant assertion should record its status and provenance. A diagram alone is not evidence that a planned behavior has been implemented or verified.

## 5. Static and behavioral aspects

DUSRM separates two complementary aspects of a system description.

**Static aspect** describes what is present and how it is organized: elements, systems, boundaries, interfaces, properties, and structural relationships.

**Behavioral aspect** describes what happens or can happen: operations, executions, events, states, transitions, and interactions.

A description may include both. Neither aspect should be mistaken for the full system on its own.

## 6. Incomplete knowledge and uncertainty

A description may be incomplete. Unknown, unspecified, not applicable, and intentionally omitted are different conditions and should not be conflated.

Where information is uncertain, the description should record the uncertainty, its source, and its impact when material. Do not invent values to fill gaps.

## 7. Relationship to structure and layers

This ontology does not impose a layered architecture. Layers may be introduced in a later structural model only when each layer has a coherent responsibility and well-defined relationships or interfaces with other layers.

The ontology must also be able to describe non-layered, graph-shaped, hierarchical, federated, and hybrid systems.

## 8. Open questions

- Do the element categories need a stronger type system, or should most categories be roles?
- How should time, causality, concurrency, and distributed state be formalized?
- How should uncertainty and conflicting observations be represented?
- Which relations require first-class relationship objects?
- How should requirements, hazards, controls, and assurance cases map into the ontology?
- What is the smallest complete core that remains useful across software and cyber-physical systems?

## 9. Status

This is a working ontology draft. It is not a complete formal metamodel, a machine-readable schema, or a conformance standard. The next revision must be informed by relationship modeling, prior-art review, and validation against independent case studies.
