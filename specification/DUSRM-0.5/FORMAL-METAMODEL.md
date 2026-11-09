# DUSRM 0.5 — Formal Metamodel

**Document ID:** DUSRM-FRM-001  
**Status:** Formalization draft; non-normative  
**Version:** 0.5-draft  
**Date:** 2026-11-09

## 1. Purpose

This document consolidates the ontology, structural model, and operational semantics into a compact abstract metamodel. It defines the principal sets, mappings, and well-formedness conditions used by DUSRM descriptions.

The metamodel is conceptual and mathematical. It is not a programming language, serialization format, executable schema, or implementation requirement.

## 2. Modeling levels

Every DUSRM description must keep these distinct:

1. **Reference model:** DUSRM concepts and rules.
2. **System of interest (SOI):** the real, planned, or hypothetical subject being described.
3. **System description:** a particular representation of the SOI using DUSRM concepts.
4. **Evidence:** observations, tests, analyses, records, or sources used to support assertions in the description.

A description is not the SOI. A modeled transition is not evidence that the physical transition occurred.

## 3. Core signature

For a description at a stated scope and version, define:

`D = (E, K, type, R, P, L, primaryLayer, realizes, V, O, X, C, A, Next, C₀, Q)`

where:

| Symbol | Meaning |
|---|---|
| `E` | Set of element identifiers in the description |
| `K` | Set of element kinds or roles |
| `type : E → K` | Element classification, allowing declared role specialization |
| `R` | Set of typed relationship instances |
| `P` | Set of responsibility definitions |
| `L` | Set of reference layers |
| `primaryLayer : P → L` | Primary layer assigned to each core responsibility |
| `realizes ⊆ E × P` | Relation stating that an element realizes a responsibility |
| `V` | Set of state-variable identifiers |
| `O` | Set of operation specifications |
| `X` | Set of execution occurrences |
| `C` | Set of modeled configurations |
| `A` | Set of action labels |
| `Next ⊆ C × A × C` | Labeled transition relation |
| `C₀ ⊆ C` | Set of admissible initial configurations |
| `Q` | Set of claims, constraints, invariants, assumptions, and evidence references |

The signature is a conceptual index of the information a description may contain. It does not require every project to enumerate these as software objects.

## 4. System scope and boundaries

A description must identify:
- one SOI or an explicitly defined collection of SOIs;
- the purpose of the description;
- the chosen scope and level of abstraction;
- the boundary or boundaries used;
- relevant external environment elements;
- assumptions and operating conditions;
- description version and status.

Membership is relative to a declared SOI and boundary. An element may be internal in one description and external in another without contradiction.

An element may represent a physical object, software construct, role, information item, event, process, resource, capability, or abstract concept.

## 5. Responsibility-based layer allocation

### 5.1 Why responsibilities are allocated

A component can realize responsibilities in more than one layer. Therefore, DUSRM does not define a single-valued function from elements to layers.

Instead:
- `P` is the set of responsibility definitions.
- Each core responsibility `p ∈ P` has one primary layer `primaryLayer(p) ∈ L`.
- `realizes(e,p)` means element `e` realizes responsibility `p` in the stated system description.

The layer set is the eight-layer candidate defined in DUSRM-0.3:
- L1 Physical and Infrastructure Foundation
- L2 Resource and Abstraction
- L3 Execution and Control
- L4 Information and State
- L5 Computation and Transformation
- L6 Interaction and Coordination
- L7 Capabilities and Services
- L8 Application and Mission Outcomes

### 5.2 Consequences

- One responsibility has one primary layer in the core model.
- One element may realize multiple responsibilities.
- An element may therefore be associated with multiple layers.
- A responsibility may be realized by multiple elements.
- A layer is not a software module, process, device, team, or deployment unit.
- Cross-cutting concerns are associated with affected elements, responsibilities, relationships, or claims; they are not forced into a ninth layer.
- Contextual elements may have no layer allocation if they do not realize a responsibility within the SOI. Their role and reason for non-allocation should be recorded.

### 5.3 Domain profiles

A domain profile may refine a core responsibility into more specific responsibilities. Each refinement must map back to exactly one core responsibility or declare that it is an additional profile-specific responsibility outside the core allocation.

A profile must not silently redefine the meaning of a core layer.

## 6. Typed relationship instances

A relationship instance should contain:
- identifier;
- relationship type;
- source and target or participant set;
- scope;
- validity conditions or time interval, if applicable;
- status (planned, specified, implemented, observed, assumed, verified, rejected, or another defined value);
- rationale;
- evidence references.

Each relationship type declares its participant signature and any domain-specific cardinality rules.

The model must not infer transitivity, symmetry, reflexivity, exclusivity, or inverse relationships unless that rule is explicitly defined for the relationship type.

## 7. State and behavior

A state variable is an identified property used to distinguish configurations. Each state variable should declare:
- owner or subject;
- value domain or referenced type;
- scope;
- whether it is observed, computed, assumed, or authoritative;
- relevant units and temporal meaning, where applicable.

An operation specification describes behavior. An execution occurrence identifies a particular performance or attempt of that operation.

A configuration represents the values and conditions selected as relevant at a declared abstraction. A description may omit details not relevant to its purpose, but omissions must not be presented as known values.

## 8. Operational kernel

The operational part of a description includes:
- `C`: modeled configurations;
- `A`: action labels;
- `Next ⊆ C × A × C`: permitted labeled steps;
- `C₀ ⊆ C`: admissible initial configurations.

A behavior trace is a finite or infinite sequence of configurations and actions such that:
- the first configuration belongs to `C₀`;
- every adjacent configuration/action pair satisfies `Next`.

The relation describes permitted behavior. It does not by itself guarantee progress or choose a deterministic outcome.

## 9. Claims and evidence

A claim should identify:
- the statement being asserted;
- the subject and scope;
- claim status;
- assumptions;
- evidence references;
- assessment method, if verified;
- limitations or uncertainty.

The words planned, specified, implemented, observed, tested, verified, assumed, and unknown have distinct meanings. In particular:
- implemented does not imply tested;
- tested does not imply verified against every requirement;
- specified does not imply implemented;
- a model-consistent trace does not prove that a deployed system produced that trace.

## 10. Well-formedness conditions

A DUSRM description is structurally well-formed only if, at minimum:

**WF-01 — Identity:** Element, relationship, responsibility, operation, state-variable, and evidence identifiers are unique within their declared namespace and version.

**WF-02 — Scope:** The SOI, purpose, abstraction level, and boundary are declared.

**WF-03 — Membership:** Every asserted membership or containment relationship references elements that exist in the description and has a declared scope.

**WF-04 — Relationship typing:** Every relationship instance uses a declared type and satisfies that type's participant signature.

**WF-05 — Relationship status:** Important relationship assertions have a status. Assumptions are not silently presented as observations.

**WF-06 — Responsibility identity:** Every responsibility used in an allocation exists in the description or its referenced profile.

**WF-07 — Layer totality for core responsibilities:** Every core responsibility has exactly one primary layer.

**WF-08 — Element allocation:** Elements realizing architectural responsibilities are linked to those responsibilities. Elements intentionally not allocated have a declared contextual role or reason.

**WF-09 — Cross-layer allocation:** An element realizing responsibilities in multiple layers records each responsibility separately; it must not be forced into one exclusive layer.

**WF-10 — Operation/execution distinction:** An execution occurrence references an operation specification; an operation specification is not itself an execution occurrence.

**WF-11 — State ownership:** Every state variable identifies the subject or scope whose state it represents.

**WF-12 — Transition endpoints:** Every transition references configurations and action labels declared in the description.

**WF-13 — Initial configurations:** The initial configuration set is declared. If a model has no reachable initial configuration, the description must flag that condition rather than implying behavior is possible.

**WF-14 — Constraint scope:** Every invariant and constraint declares the subject, scope, and assumptions under which it applies.

**WF-15 — Evidence discipline:** A verified claim references a criterion, method, and evidence; a model assertion alone is insufficient.

**WF-16 — Version traceability:** Every description identifies the DUSRM draft or stable version and any domain profile used.

These are proposed structural rules. They do not yet constitute a machine-checked validator.

## 11. Out of scope for this metamodel

The current metamodel does not prescribe:
- physical implementation architecture;
- one fixed internal decomposition;
- executable semantics for a programming language;
- API, protocol, transport, or serialization definitions;
- a universal resource allocator or scheduler;
- a specific consistency or transaction model;
- a safety certification process;
- a canonical machine-readable file format.

## 12. Status

This metamodel is a formalization draft. The definitions and well-formedness rules require peer review, consistency testing, and case-study validation before becoming normative.
