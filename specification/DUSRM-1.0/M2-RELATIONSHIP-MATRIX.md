# DUSRM 1.0 Preparation — Relationship Semantics and Signature Matrix

**Work package:** WP2 — Foundational Ontology and Relationship Consolidation  
**Status:** Proposed relationship catalogue; non-normative  
**Target:** DUSRM 1.0

## 1. Purpose

A relationship is a typed assertion connecting model objects in a declared description and scope. Its type determines the meaning of the assertion and the permitted participant roles.

The signature matrix below defines the intended conceptual endpoints. It is deliberately more precise than the two generic participant categories checked by the 0.9 validator.

## 2. General relationship record

A relationship assertion should carry:
- stable identifier;
- relationship type and metamodel version;
- typed source/target or named participant roles;
- description and scope references;
- direction and role meaning;
- validity interval or conditions, where relevant;
- rationale;
- design disposition;
- realization and assessment information where applicable;
- evidence references.

Binary relationships may use source and target. Multi-party relationships must use named participant roles or a reified model object. Do not flatten a genuinely n-ary relation into pairwise links if doing so loses the shared context or allocation semantics.

## 3. Core relationship matrix

| Type | Conceptual source | Conceptual target | Meaning and boundary |
|---|---|---|---|
| memberOf | Element | System or composite Element | Element participates as a member of the named system in the stated scope; does not imply physical containment or ownership |
| decomposesInto | System or composite Element | Element or subsystem | Composite is described through constituent elements; does not imply independent deployment or lifecycle ownership |
| containedWithin | Element | Element, container, or Boundary | Subject is within a declared physical, logical, organizational, or analytical boundary; does not imply membership or ownership |
| dependsOn | Participant | Participant | Source relies on target for a stated property, behavior, or condition; does not imply direct communication |
| exposes | Provider Participant | Interface | Provider makes the named interface available; does not imply reachability, availability, or successful invocation |
| requires | Consumer Participant | Interface, Capability, or Resource | Consumer declares a need for the named interaction point, ability, or resource; does not imply the need is satisfied |
| interactsWith | Participant | Participant | Participants exchange influence, information, commands, energy, or effects within a stated context; direction must be explicit when asymmetric |
| allocates | Allocator Participant | Resource | Allocator assigns or reserves the named resource; recipient, amount, unit, interval, and policy must be represented in a reified Allocation record when material |
| performs | Execution | Operation | Execution is an occurrence or attempt of the referenced operation; does not imply success |
| triggers | Event | Transition or Operation | Event initiates or enables behavior under declared conditions; does not imply completion |
| transitionsTo | State or Configuration | State or Configuration | Declared condition may change to another condition under a transition rule; must preserve the relevant subject and state domain |
| observes | Observer Participant | Observable Element, Event, Property, or State | Observer obtains information about the target; does not imply accuracy, completeness, freshness, or authority |
| controls | Controller Participant | Controlled Element, Operation, or Execution | Controller can influence or constrain target under a declared authority and scope; does not imply unlimited authority or successful physical effect |
| constrainedBy | Subject or Behavior | Constraint | Subject is governed by the referenced constraint; does not imply the constraint is satisfied |
| satisfies | Candidate Element, Responsibility, Operation, or Capability | Requirement | Subject is asserted to meet the requirement under declared conditions; a satisfaction claim needs appropriate criteria and evidence |
| derivedFrom | Requirement, Decision, or Assertion | Source Artifact, Requirement, or Assertion | Source is the declared derivation basis; does not imply that the derivation is correct |
| implements | Implementation Element | Specification or Design Definition | Implementation is intended to realize the referenced specification/design; full conformance requires separate assessment |

## 4. The realizes naming collision

The current drafts use the word realizes in two different senses:
1. an Element realizes a Responsibility, represented by the dedicated Realization allocation record;
2. an implementation realizes a specification or design, represented in the older relationship catalogue.

These meanings must not share one unqualified relationship name in the 1.0 core.

**Proposed 1.0 rule:** reserve **Realization** for the element-to-responsibility allocation object. Use **implements** for an implementation-to-specification/design relationship. The relationship type realizes is retained only as a legacy 0.x term and must not be used in new 1.0 descriptions.

This avoids confusing architectural responsibility allocation with implementation conformance.

## 5. Reified relationships

Some relationships require more than two endpoints or need their own attributes.

### 5.1 Allocation

An Allocation should identify:
- allocator;
- resource;
- recipient or beneficiary;
- quantity and unit, if quantitative;
- validity interval;
- allocation policy or decision;
- status and evidence.

A simple allocates relationship from allocator to resource is not a complete record of who receives how much and when.

### 5.2 Multi-party interaction

A multi-party Interaction should identify all participants with named roles, the shared interaction context, exchanged items, ordering/causality requirements, and relevant failure behavior.

Do not replace one three-party interaction with three pairwise interactsWith links unless the pairwise links faithfully preserve the intended meaning.

### 5.3 Other reification cases

A relationship should be reified as a first-class object when it has independent identity, lifecycle, quantitative properties, temporal validity, more than two participants, or evidence that cannot be accurately attached to a simple binary assertion.

## 6. Default semantic rules

Unless a relationship subtype explicitly states otherwise:
- no transitivity is implied;
- no symmetry or inverse is implied;
- no reflexivity is implied;
- no uniqueness or exclusivity is implied;
- no ordering or causality is implied by diagram placement;
- no implementation or verification status is inferred from the relationship's existence;
- no layer dependency is inferred from the order of the eight layers;
- no control authority or safety guarantee is inferred from a relationship name.

A relationship type may add domain-specific rules only through a reviewed core definition or a namespaced profile extension.

## 7. Legacy 0.9 validator coverage

The 0.9 semantic validator has provisional participant-kind signatures for:
- decomposesInto;
- memberOf;
- containedWithin;
- dependsOn;
- interactsWith;
- observes;
- controls;
- allocates;
- requires;
- exposes.

Those signatures currently use the broad kinds Element, Environment, and System. They are only a conservative validation subset; they are not the full conceptual signatures in this matrix.

The validator reports unsupported types with warning DUSRM-M-016. The types performs, triggers, transitionsTo, constrainedBy, satisfies, realizes, and derivedFrom remain deliberately unguessed because the 0.1 schema does not yet expose all required typed endpoint collections.

## 8. Review status

The conceptual matrix is proposed. Before becoming normative, each relationship requires review of participant cardinality, endpoint typing, scope, temporal validity, status, evidence, and whether reification is mandatory.
