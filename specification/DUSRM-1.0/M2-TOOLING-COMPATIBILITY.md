# DUSRM 1.0 Preparation — Ontology and Tooling Compatibility

**Work package:** WP2 — Foundational Ontology and Relationship Consolidation  
**Status:** Compatibility analysis and migration proposal; non-normative  
**Target:** DUSRM 1.0

## 1. Scope

This document compares the WP2 proposed ontology with the existing JSON Schema 0.1, semantic validator 0.9, relationship-signature rules, and profile registry.

No existing schema or validator behavior is silently reclassified as 1.0 conformance.

## 2. Current tooling baseline

The repository currently has:
- JSON Schema Draft 2020-12 description schema identified as 0.1-draft;
- schema fields for context, elements, responsibilities, realizations, binary relationships, operations, state variables, transitions, evidence, constraints, invariants, and extensions;
- a semantic validator that checks selected identifier, reference, realization, relationship-signature, profile, extension, transition, and evidence rules;
- machine-checkable participant signatures for a subset of ten relationship types;
- twelve semantic regression tests in the 0.9 validation baseline.

This is a useful partial projection of the ontology, not a complete metamodel implementation.

## 3. Compatibility gaps

| WP2 concept or rule | Current schema/tooling | Gap and required treatment |
|---|---|---|
| Element category and multiple roles | Element has one free-text kind and optional external boolean | No controlled category/role model; add typed or namespaced roles in a future schema |
| Typed relationship endpoints | Relationships use untyped sourceRef and targetRef | Validator can classify only Element, Environment Participant, and SOI endpoints |
| Operations and executions | Operation definitions exist; no Execution collection | performs cannot receive a complete typed check |
| Events | No Event collection; trigger is a string | triggers cannot be checked against a typed Event |
| State definitions and values | StateVariable exists; transition from/to are strings | transitionsTo cannot safely treat values as first-class State objects |
| Interface | No first-class Interface collection | exposes/requires signatures cannot distinguish an interface from a generic Element |
| Resource and allocation | No typed Resource or Allocation collection | allocates cannot record allocator, resource, recipient, amount, unit and interval |
| Capabilities and services | No first-class Capability or Service collection | requires cannot distinguish a service from another participant |
| Requirements and constraints | Constraints reuse a generic claim object; no separate Requirement collection | satisfies and constrainedBy need typed target records |
| Implementation-to-specification trace | realizes is present in legacy relationship catalogue | Name conflicts with the dedicated element-to-responsibility Realization record; use implements in the proposed 1.0 vocabulary |
| Evidence and assertions | One legacy status field and limited evidence metadata | Need orthogonal disposition, realization, applicability, assessment, and evidence context |
| External layer applicability | Element has external boolean; layer applicability is not represented | Need explicit applicability records or references |
| N-ary relationships | Relationship schema is binary source/target | Use reified entities or named participant roles where shared multi-party context matters |
| Profile compatibility | Registry coreVersion is 0.7-draft; all three profiles are not-assessed | No profile may claim 1.0 compatibility until separately reviewed |

## 4. What the current validator can and cannot claim

The 0.9 validator can report selected structural-semantic findings. It cannot:
- validate the full conceptual relationship matrix in WP2;
- prove that a layer assignment is architecturally correct;
- type-check operations, events, states, interfaces, resources, capabilities, or requirements as relationship endpoints;
- assess all evidence for relevance, freshness, independence, or sufficiency;
- establish implementation conformance, system safety, or fitness for purpose.

Unsupported relationship signatures produce warning DUSRM-M-016. This is intentional and safer than assuming an endpoint signature based on a relationship name.

## 5. Proposed schema evolution

A future schema revision should be independently versioned from the DUSRM conceptual version. The current 0.1 schema must remain available for historical 0.7/0.9 descriptions.

The next schema design should consider:
1. typed reference objects that include both metamodel kind and identifier;
2. explicit role/category declarations for elements;
3. explicit Execution and Event records;
4. explicit State/StateValue semantics and typed transition endpoints;
5. first-class Interface, Resource, Allocation, Capability, Service, Requirement, Constraint, and Specification records where required;
6. reified n-ary relationships with named participant roles;
7. orthogonal status fields rather than one overloaded status;
8. explicit layer applicability;
9. evidence records with method, revision, scope, context, result, and limitations;
10. migration rules from schema 0.1, including contextual mapping of legacy status values.

This document does not create schema 0.2 or authorize a breaking change. That work needs its own schema design, fixtures, migration utility, validator updates, and CI.

## 6. Profile compatibility

The current registry declares core version 0.7-draft and marks the standalone application, ANANTA DBMS, and FireBot cyber-physical profiles not-assessed.

They remain not-assessed. WP2 does not approve profile compatibility with DUSRM 1.0. Each profile must be reviewed against the consolidated ontology, layer charter, relationship semantics, and status model.

## 7. Migration principles

- Preserve the original source description and schema version.
- Convert into a new schema version without overwriting the original.
- Record every lossy or ambiguous mapping.
- Do not automatically promote evidence or realization states.
- Keep external participants distinct from internal elements.
- Preserve stable IDs where object identity is unchanged; create explicit mapping records where object kinds split or merge.
- Run both old and new validators during the migration window.
- Publish fixtures for both successful and rejected migrations.

## 8. Status

The compatibility analysis is complete as a documentation deliverable. The existing schema, validator, fixtures, and profiles are unchanged by this work package.
