# DUSRM 0.2 — Relationship Catalogue

**Document ID:** DUSRM-REL-001  
**Status:** Working draft; non-normative  
**Version:** 0.2-draft

## 1. Purpose

This document proposes a controlled set of relationship types for connecting DUSRM elements. The purpose is to prevent diagrams and descriptions from using ambiguous lines or overloaded verbs.

A relationship is a typed assertion. It is not enough to draw a connection; the meaning, direction, scope, and relevant conditions should be understood.

## 2. General relationship record

A relationship description should capture the following fields when relevant:

| Field | Meaning |
|---|---|
| Identifier | Stable identifier for the relationship assertion |
| Type | Defined relationship type |
| Source | Element or participant from which the relationship is stated |
| Target | Element or participant to which it is stated |
| Scope | System or description in which the relationship applies |
| Direction | Directed, undirected, or explicitly bidirectional |
| Validity | Time or conditions for which the relationship holds |
| Rationale | Why the relationship is asserted |
| Status | Planned, implemented, observed, assumed, verified, or rejected |
| Evidence | Supporting source, analysis, test, or observation |

A relationship may connect more than two participants. Such relationships should be represented as n-ary relationships rather than forced into misleading pairs.

## 3. Core relationship types

| Relationship | Source → target | Meaning | Does not imply |
|---|---|---|---|
| `memberOf` | Element → System | Element participates as a member of the system in the stated scope | Physical containment or ownership |
| `decomposesInto` | System → Element/System | System is described through constituent elements or subsystems | That every part is independently deployable |
| `dependsOn` | Element → Element | Source relies on target for a stated property or behavior | A direct API or network connection |
| `exposes` | Participant → Interface | Participant makes an interface available | That the interface is reachable or currently operational |
| `requires` | Participant → Interface/Capability/Resource | Participant needs the target to fulfill a stated behavior | That the requirement is satisfied |
| `interactsWith` | Participant ↔ Participant | Participants exchange influence or information within a stated interaction context | A specific protocol or transport |
| `allocates` | Allocator → Resource/Consumer | An allocator assigns or reserves a resource for a consumer | Successful execution or sufficient capacity |
| `performs` | Execution → Operation | Execution is an occurrence of the specified operation | That the operation completed successfully |
| `triggers` | Event → Transition/Operation | Event initiates or enables behavior under stated conditions | That the behavior necessarily completes |
| `transitionsTo` | State → State | A modeled state can change to another state under declared conditions | That all transitions are reachable |
| `observes` | Observer → Subject/Property/Event | Observer obtains information about the target | That the information is accurate or complete |
| `controls` | Controller → Operation/Element | Controller can influence or govern the target within stated authority | Unlimited authority or safety |
| `constrainedBy` | Element/Behavior → Constraint | Target is subject to a stated constraint | That the constraint is satisfied |
| `satisfies` | Element/Evidence → Requirement | Target is asserted to meet a requirement | Verification unless supported by evidence and method |
| `realizes` | Implementation → Specification/Design | Implementation is intended to implement the target definition | Full conformance without assessment |
| `derivedFrom` | Requirement/Decision → Source | Source is the derivation basis | That the derivation is correct |
| `containedWithin` | Element → Boundary/Container | Target lies within a stated containment or scope relationship | Ownership or lifecycle authority |

The table is a proposed controlled vocabulary. It must be reviewed before becoming normative.

## 4. Relationship rules

1. **No silent implication:** A relationship must not imply another relationship unless that implication is explicitly defined.
2. **Scope matters:** `memberOf` and `containedWithin` are always relative to a declared description and boundary.
3. **Direction matters:** Direction must be explicit where reversing source and target changes meaning.
4. **Time matters:** A relationship that changes over time should have validity conditions or temporal context.
5. **Status matters:** Planned, observed, and verified relationships must be distinguishable.
6. **Evidence matters:** High-impact assertions should link to evidence or explicitly state that they are assumptions.
7. **Composition is not ownership:** Decomposition does not automatically imply control, lifecycle responsibility, or physical containment.
8. **Interaction is not transport:** An interaction can be physical, human, logical, informational, mechanical, or software-mediated. It is not itself a protocol.

## 5. Relationship classes

For analysis, relationships may be grouped into broad classes:

- **Structural:** memberOf, decomposesInto, containedWithin.
- **Dependency and provision:** dependsOn, exposes, requires, allocates.
- **Behavioral:** interactsWith, performs, triggers, transitionsTo, observes, controls.
- **Assurance and traceability:** constrainedBy, satisfies, realizes, derivedFrom.

These classes are organizational aids, not additional relationship semantics.

## 6. Relationship composition example

Illustrative example of a generic monitoring system:

- `SensorAssembly memberOf MonitoringSystem`
- `Controller memberOf MonitoringSystem`
- `Controller dependsOn SensorAssembly`
- `SensorAssembly exposes MeasurementInterface`
- `Controller requires MeasurementInterface`
- `Controller performs EvaluateMeasurement` (through a particular execution occurrence)
- `OverLimitEvent triggers AlertTransition`
- `AlertTransition transitionsTo AlertActiveState`

This example does not specify a physical interface, protocol, threshold, timing guarantee, or safety behavior.

## 7. Unresolved topics

- Formal inverse properties and transitivity.
- Whether some relationships should be reified as first-class entities in every case.
- Cardinality constraints and multiplicity.
- Temporal, causal, probabilistic, and uncertain relationships.
- Relationship inheritance and specialization.
- Machine-readable serialization and validation rules.

No general transitivity or inverse rule should be assumed unless defined for a specific relationship type.
