# DUSRM 1.0 Preparation — Consolidated Core Ontology

**Work package:** WP2 — Foundational Ontology and Relationship Consolidation  
**Status:** Proposed core ontology; non-normative  
**Target:** DUSRM 1.0  
**Predecessors:** DUSRM 0.2 Core Ontology; DUSRM 0.5 Formal Metamodel; DUSRM 1.0 WP1 Layer Charter

## 1. Purpose

This document consolidates the foundational concepts used to describe a system. It clarifies which concepts identify subjects, which describe responsibilities or behavior, and which record claims and evidence.

The ontology is intended to describe software, infrastructure, data engines, distributed systems, organizations, cyber-physical systems, and systems of systems without requiring a particular implementation technology.

This is a proposed 1.0-preparation ontology. It does not make the current JSON schema or validator a complete implementation of these concepts.

## 2. Modeling levels

Every description keeps four levels distinct:

1. **Reference-model level:** DUSRM's concepts, definitions, relationship semantics, rules, and viewpoints.
2. **Subject level:** the real, planned, simulated, or hypothetical system of interest (SOI), including the relevant entities and behavior.
3. **Description level:** the particular model, architecture description, or set of assertions created about the SOI.
4. **Evidence level:** sources, observations, measurements, tests, analyses, reviews, and formal results used to support or challenge description assertions.

A representation is not its subject. A modeled state transition is not proof that the corresponding physical or deployed transition occurred.

Every material statement in a description should be identifiable as a definition, an assertion about the SOI, a design decision, an assumption, or evidence.

## 3. Core subject and participant concepts

### 3.1 System of interest

A **System of Interest** is the real, intended, or hypothetical organized subject selected for analysis, design, operation, or assurance.

A description identifies its purpose, scope, boundary, abstraction level, relevant environment, and version. A system may be treated as a subsystem in a larger description.

### 3.2 Element

An **Element** is a distinguishable subject represented within the declared system description. It may represent a physical object, software construct, person or role, information object, resource, process, subsystem, or other relevant subject.

An element is not required to be a physical or deployable component. The element's category and roles describe what kind of subject it represents; they do not determine its layer.

### 3.3 Environment participant

An **Environment Participant** is an external entity or actor relevant to the SOI under the selected boundary. It may be a person, organization, external system, infrastructure provider, physical environment, or remote service.

An environment participant is not an internal realization of the SOI. A boundary change may cause the same subject to be internal in one description and external in another.

### 3.4 Participant

**Participant** is the role used when a relationship needs to connect an SOI, an Element, or an Environment Participant. It is a reference category, not a new kind of physical entity.

### 3.5 Boundary and context

A **Boundary** declares what is included, excluded, or treated as crossing the selected scope. Boundaries may be physical, logical, organizational, temporal, or analytical.

Context includes purpose, stakeholders, operating conditions, environment participants, assumptions, exclusions, and the selected abstraction level.

## 4. Classification: category, kind, and role

A subject's classification must not be confused with its architectural responsibility.

- **Category** identifies a broad ontological family, such as physical, computational, informational, human/organizational, or environmental.
- **Kind** identifies a more specific form, such as sensor, software service, database engine, battery, requirement, or event.
- **Role** describes the part a subject plays in one particular system or relationship, such as provider, consumer, controller, observer, allocator, or operator.

A subject may have multiple roles and may participate in several responsibilities. Multiple roles do not require duplicate element records.

The category and kind vocabulary may be extended by a domain profile. A profile must preserve the distinction between a subject's kind and the DUSRM layer of its responsibilities.

## 5. Core model objects

### 5.1 Responsibility

A **Responsibility** is a separately describable concern, duty, or function assigned to a primary DUSRM layer. It states what must be accounted for in the architecture, not which component performs it.

Each core responsibility has exactly one primary layer. If a description combines concerns from multiple layers in one statement, it should decompose that statement into distinct responsibilities.

A responsibility is not the same as:
- a requirement, which states an obligation or need;
- an operation, which specifies behavior;
- a capability, which states an ability offered or available;
- an element, which identifies a subject;
- a component, which is a contextual role of an element.

### 5.2 Realization allocation

A **Realization** is a typed allocation record connecting an Element to a Responsibility it realizes in the declared scope.

Realization is many-to-many:
- one element may realize multiple responsibilities;
- one responsibility may be realized by multiple elements;
- an element may have no allocation when it is only a contextual participant or when its role is outside the modeled scope.

A Realization record is distinct from a general relationship assertion. Do not use the relationship type name realizes as a substitute for the dedicated element-to-responsibility allocation record.

### 5.3 Operation and execution

An **Operation** is a specification of behavior that a subject can perform or offer. It may describe purpose, inputs, preconditions, outputs, effects, postconditions, and failure conditions.

An **Execution** is a particular occurrence or attempt to perform an operation. It has a subject, operation reference, execution context, lifecycle, and relevant timing or outcome.

An operation definition does not prove that an execution occurred. An execution record does not, by itself, prove that its intended physical effect occurred.

### 5.4 Event

An **Event** is an occurrence represented as relevant to a system. It may be generated internally, observed externally, derived from other information, or abstracted from a continuing physical phenomenon.

An event's time, source, observation context, and uncertainty should be recorded when they affect causality or interpretation. An event may trigger or enable a transition, but does not guarantee that the resulting behavior completes.

### 5.5 Information, property, and state

An **Information Object** is a represented item whose identity and meaning are relevant to the description. Its type, units, provenance, validity, and source should be explicit where they matter.

A **Property** is a characteristic attributed to a subject or relationship. A property may be qualitative, quantitative, static, or time-varying.

A **State Variable** is a named property or value slot used to represent a selected aspect of a subject's condition. It should identify its subject, meaning, value domain, scope, units, and authority or observation status.

A **State** or **Configuration** is a modeled condition or valuation over the selected state variables and other facts. It is not necessarily a single global mode.

A **Transition** describes a permitted change between declared state values or configurations under conditions, triggers, guards, and effects. Its semantics must identify whether it concerns a state variable, a local state, or a system configuration.

### 5.6 Interface and interaction

An **Interface** is a declared boundary at which participants may exchange information, commands, services, energy, material, or other effects.

An interaction contract may identify participants, roles, direction, exchanged items, preconditions, postconditions, timing, failure behavior, and authority. It may reference a separate technical specification.

An interface is not synonymous with an API, protocol, connector, transport, or encoding. Those technical artifacts remain specified by their own authoritative specifications.

An **Interaction** is an exchange or coordinated activity involving participant roles. A multi-party interaction must preserve all meaningful participant roles; it must not be flattened into misleading pairwise links.

### 5.7 Resource

A **Resource** is a capacity, asset, or means that can be required, allocated, reserved, occupied, consumed, shared, or controlled.

A resource may be physical or non-physical. Its capacity, unit, availability, ownership, contention, allocation, consumption, and release semantics should be modeled where relevant.

The resource's physical substrate belongs to the appropriate subject model; the available capacity and its allocation policy are separate responsibilities.

### 5.8 Capability and service

A **Capability** is an ability that a system or element can provide or exercise under declared conditions.

A **Service** is a coherent capability made available to a consumer through an interaction boundary, with declared conditions or quality where relevant.

A capability is not permission or authority. Technical ability, permission to act, recognized authority, and actual execution are separate concepts.

### 5.9 Requirement, constraint, and invariant

A **Requirement** records a stakeholder need, obligation, or condition expected of a system or element.

A **Constraint** restricts allowable structure, properties, states, operations, transitions, relationships, or behaviors.

An **Invariant** is a constraint claimed to remain true throughout a declared scope and behavior under explicit assumptions. An invariant is not proven merely by being written in mathematical notation.

A requirement is not evidence of satisfaction. A constraint may be violated by an observed system; the description must distinguish the rule from the evidence about the subject.

### 5.10 Assertion, decision, and evidence

An **Assertion** is a statement made in a system description about the SOI, a design, requirement, relationship, or assumption.

A **Decision** records an accepted or rejected choice, its rationale, scope, alternatives, and source basis.

**Evidence** is material used to support, refute, or qualify an assertion. It may be a source document, source revision, test result, tool output, measurement, observation, analysis, simulation, formal result, or review record.

Evidence must identify its provenance and context sufficiently to understand what it does and does not support.

## 6. Layer association

The eight WP1 layers classify Responsibilities only. They do not classify all model objects.

An element, operation, interface, event, state variable, resource, capability, requirement, or piece of evidence does not receive a primary layer merely because it exists. A layer is derived from the responsibilities that the relevant element realizes.

An entity may be relevant to responsibilities in multiple layers without being duplicated. Cross-cutting concerns attach to the specific entities, responsibilities, relationships, operations, transitions, or claims they affect.

## 7. Identity and reference rules

- Identifiers are stable within a declared description version and object namespace.
- A reference must identify both the target object and its metamodel kind when the reference could be ambiguous.
- A description must not rely on a bare string that can refer to an Element, Operation, Event, State, Requirement, or Evidence item interchangeably.
- External participants must be distinguished from internal elements.
- A nested system may be represented as an element with a system role and its own referenced description or boundary.
- Aliases and human-readable names are not substitutes for stable identifiers.

## 8. Extension rules

A domain profile may introduce specialized kinds, roles, properties, relationship subtypes, or constraints. Each extension must:
- declare its owner and version;
- define scope, semantics, and endpoint expectations;
- map to one or more core concepts without redefining them;
- identify whether it is optional or mandatory for that profile;
- describe compatibility and migration behavior.

An extension must not silently change the meaning of a core layer, relationship, status dimension, or evidence category.

## 9. Status

The ontology and terminology in this document are proposed 1.0 core concepts. Their implementation in the JSON schema and semantic validator is a separate staged task. The current 0.9 tooling remains a partial projection and must not be described as implementing the full ontology.
