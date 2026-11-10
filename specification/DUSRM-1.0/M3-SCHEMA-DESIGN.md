# DUSRM 1.0 Preparation — WP3 Typed Metamodel and Schema 0.2 Design

**Work package:** WP3 — Typed Metamodel and Schema 0.2 Design  
**Status:** Draft; non-normative  
**Schema identifier:** urn:dusrm:schema:description:0.2-draft  
**Target conceptual model:** DUSRM 1.0 preparation

## 1. Purpose

WP3 converts the WP2 ontology into a machine-readable description envelope. Schema 0.2 is separately versioned from the DUSRM conceptual version and does not replace schema 0.1.

The schema is designed to reject structurally ambiguous records and invalid relationship endpoint categories. It is not a complete semantic validator or an executable system model.

## 2. Design principles

1. **Typed references:** references declare both object kind and identifier.
2. **Distinct metamodel objects:** Element, Responsibility, Operation, Execution, Event, State, Interface, Resource, Capability, Requirement, Constraint, Evidence and other concepts have separate records.
3. **Responsibility-only layer allocation:** only a Responsibility has a core primary layer.
4. **Orthogonal status dimensions:** design disposition, realization state, applicability and assessment result are independent fields.
5. **Explicit multi-party roles:** interfaces and interactions carry named participant roles.
6. **Reification where required:** resource allocation and complex interactions can be first-class records.
7. **No implicit relationship semantics:** endpoint kinds are specified, while transitivity, symmetry, authority and conformance are not inferred.
8. **Version preservation:** schema 0.1 stays available for historical descriptions; schema 0.2 has its own identifier and fixture suite.

## 3. Typed reference structure

A typed reference has exactly two fields:

`{ "kind": "<metamodel-kind>", "id": "<stable-identifier>" }`

The kind disambiguates references to elements, responsibilities, operations, executions, events, states, interfaces, resources, requirements, evidence and other defined objects.

A participant reference is a restricted typed reference whose kind must be one of:
- system;
- element;
- environmentParticipant.

Typed references prevent a string such as `"OP-1"` from being interpreted as an element in one part of a description and an operation in another.

Schema validation confirms the reference shape and allowed kind. It does **not** confirm that the referenced identifier exists in the corresponding collection. That remains a semantic-validator responsibility.

## 4. Description envelope

A schema 0.2 description includes:
- schema and DUSRM version identifiers;
- description identifier, title and description lifecycle state;
- profile references;
- context with the SOI, purpose, scope, abstraction level, boundary and environment participants;
- all typed model collections;
- namespaced extension data.

All collection envelopes are required, including empty arrays. This makes omissions explicit and yields predictable interchange structure.

## 5. Typed collections

| Collection | Object | Purpose |
|---|---|---|
| elements | Element | Subjects inside the declared SOI boundary |
| responsibilities | Responsibility | Concerns assigned to one primary layer |
| realizations | Realization | Element-to-responsibility allocations |
| layerApplicability | Layer Applicability | Internal/external/not-applicable/not-modeled/unknown layer declarations |
| properties | Property | Typed properties of subjects or relationships |
| specifications | Specification | Referenced designs, contracts, standards and specifications |
| relationships | Relationship | Typed graph assertions with explicit endpoint kinds |
| operations | Operation | Behavior specifications |
| executions | Execution | Individual occurrences or attempts of operations |
| events | Event | Generated, observed, external or derived occurrences |
| stateVariables | State Variable | Named state dimensions and domains |
| states | State | Named valuations of a state variable |
| transitions | Transition | Typed changes between state values |
| interfaces | Interface | Participant boundaries and referenced interaction contracts |
| interactions | Interaction | Exchanges among named participant roles |
| resources | Resource | Capacities, assets and means |
| allocations | Allocation | Allocator/resource/recipient/quantity records |
| capabilities | Capability | Abilities a provider can offer or exercise |
| services | Service | Consumable capabilities exposed through an interface |
| requirements | Requirement | Needs, obligations and acceptance criteria |
| constraints | Constraint | Structural, state, resource, time, authority, safety and other restrictions |
| invariants | Invariant | Properties claimed over a declared scope and assumptions |
| assertions | Assertion | Statements about design, implementation, behavior, assumptions or assessment |
| decisions | Decision | Architecture decisions, disposition, rationale and alternatives |
| evidence | Evidence | Sources, tests, measurements, observations, analyses, simulations and formal results |

## 6. Relationship endpoint constraints

Schema 0.2 defines typed source and target objects for the 17 proposed core relationship types:

| Relationship | Source kinds | Target kinds |
|---|---|---|
| memberOf | element | system, element |
| decomposesInto | system, element | element |
| containedWithin | element | element, boundary |
| dependsOn | system, element, environmentParticipant | system, element, environmentParticipant |
| exposes | system, element, environmentParticipant | interface |
| requires | system, element, environmentParticipant | interface, capability, resource |
| interactsWith | system, element, environmentParticipant | system, element, environmentParticipant |
| allocates | system, element, environmentParticipant | resource |
| performs | execution | operation |
| triggers | event | transition, operation |
| transitionsTo | state | state |
| observes | system, element, environmentParticipant | element, event, property, state |
| controls | system, element, environmentParticipant | element, operation, execution |
| constrainedBy | element, operation, execution | constraint |
| satisfies | element, responsibility, operation, capability, service | requirement |
| derivedFrom | requirement, decision, assertion | evidence, requirement, decision, assertion |
| implements | element | specification |

These are structural endpoint-kind rules. They do not prove identifier resolution, endpoint scope, direction appropriateness, cardinality, realization, authority, correctness or conformance.

The generic `realizes` relationship is not included. Element-to-responsibility allocation uses the dedicated `realizations` collection; implementation-to-specification linkage uses `implements`.

## 7. Status fields

Schema 0.2 separates:
- `designDisposition`: proposed, accepted, rejected, superseded;
- `realizationState`: notStarted, planned, inProgress, implemented, retired, unknown;
- `applicability`: internal, externalDependency, notApplicable, notModeled, unknown;
- `assessmentResult`: notAssessed, pass, passWithFindings, fail, inconclusive;
- evidence `method`, `context`, and `relation`: how evidence was obtained, where, and how it relates to a claim.

The schema intentionally has no single universal top-level `status` property.

## 8. Structural versus semantic validation

Schema 0.2 checks:
- required object shape and collection envelopes;
- allowed field and enumeration values;
- typed-reference structure;
- relationship-specific endpoint kinds;
- required named participant roles for interfaces and interactions;
- basic numeric and temporal formats when a format checker is used.

Schema 0.2 does not check:
- global identifier uniqueness;
- whether any referenced identifier exists;
- whether a reference kind matches the target collection;
- whether relationship scope includes its endpoints;
- whether a responsibility is actually realized;
- whether a layer allocation rationale is correct;
- evidence adequacy, freshness, independence or contradiction resolution;
- profile compatibility;
- safety, security or system conformance.

These checks require the next semantic-validator work package and human/domain review.

## 9. Versioning

Schema 0.2 is identified by `urn:dusrm:schema:description:0.2-draft`. It is not a silent revision of schema 0.1. Consumers must select the schema using the declared schema version or identifier.

Schema versioning is independent of the DUSRM conceptual release. A DUSRM 1.0-preparation description may use schema 0.2-draft without claiming that DUSRM 1.0 is stable.

## 10. Exit conditions

WP3 design is ready for review when:
- the schema is valid Draft 2020-12;
- positive and negative fixtures cover the schema contract;
- the SAND OS pilot exercises typed concepts and all core relationship endpoint categories;
- migration limits from 0.1 are documented;
- CI runs independently of the historical 0.1 validation workflow;
- semantic limitations are clearly stated.
