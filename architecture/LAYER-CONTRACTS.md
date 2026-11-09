# DUSRM 0.3 — Layer Contract Template and Rules

**Status:** Working draft; non-normative

## 1. Purpose

This document provides a repeatable template for describing each DUSRM responsibility layer. It is intended to make layer definitions comparable and to prevent layer names from becoming vague labels.

## 2. Required layer contract

Each layer specification should include:

1. Identifier and name.
2. One-sentence purpose.
3. Scope and explicit exclusions.
4. Owned responsibilities.
5. Concepts and entity roles used.
6. Provided responsibilities or guarantees.
7. Required responsibilities and dependencies.
8. Inputs, outputs, and observable effects.
9. Interfaces or contracts, where applicable.
10. Constraints and invariants.
11. Failure, degradation, and recovery considerations.
12. Cross-cutting concern mapping.
13. Relationship to layers above and below.
14. Non-adjacent and feedback relationships.
15. Worked examples from at least two domains.
16. Open issues and evidence status.

## 3. Rules for layer boundaries

- A layer is defined by the responsibility it groups, not by the technology commonly used to implement it.
- A layer must not be defined only by saying what another layer does.
- Adjacent layers should have declared responsibility contracts where a support dependency exists.
- Direct non-adjacent relationships are allowed and must be represented in the relationship graph.
- Feedback, control, and bidirectional interactions must not be prohibited merely to preserve a neat stack diagram.
- A layer may be implemented by several components or one component may realize multiple layers.
- A layer may be absent or not applicable in a particular system description.
- If two layer definitions cannot be distinguished in a worked example, their boundaries must be revised.

## 4. Layer-to-technology mapping rule

DUSRM maps technologies to responsibilities, not the other way around.

For example, a database engine may support information/state and computation responsibilities, but DUSRM must not prescribe that database engine. An API or protocol may realize interaction responsibilities, but DUSRM must not redefine the API or protocol.

Technology mappings must state whether they are:
- verified against an existing specification or repository;
- inferred from an incomplete description;
- planned;
- hypothetical.

## 5. Review checklist

A proposed layer is acceptable only when reviewers can identify:
- a distinct responsibility;
- its boundary with neighboring layers;
- what it provides and requires;
- how it relates to the ontology;
- how it applies to both software and cyber-physical examples;
- what it explicitly does not define.

This checklist is preliminary and will be refined during validation.
