# DUSRM 0.2 — Foundational Ontology Status

**Status:** Working draft; non-normative  
**Milestone:** M1 — Ontology  
**Release label:** 0.2-draft  
**Date:** 2026-11-09

## Objective

Establish a stable first vocabulary and relationship model for describing systems, while keeping the system of interest distinct from its DUSRM description.

## Included in this draft

- Three-level separation: reference-model level, subject level, and description level.
- Preliminary system-of-interest definition.
- Core concepts: element, system, component, subsystem, environment, boundary, interface, relationship, property, state, operation, execution, event, transition, resource, capability, constraint, invariant, requirement, assertion, and evidence.
- Static and behavioral aspects.
- Initial typed relationship catalogue.
- Informal explanatory notation.
- Prior-art scope review covering OSI, ISO/IEC/IEEE 15288, ISO/IEC/IEEE 42010, and OMG SysML v2.

## Explicitly not finalized

- The set and names of all core concepts.
- Ontology completeness and domain coverage.
- Layer count or layer ordering.
- Formal mathematical semantics.
- Cardinality, multiplicity, and relationship inference rules.
- Machine-readable serialization or schema.
- Normative conformance requirements.
- Novelty or superiority claims.

## Acceptance questions for review

A reviewer should be able to answer:

1. Can the model distinguish a real/planned system from its written description?
2. Can an element be a subsystem in one context and a component in another without contradiction?
3. Can boundaries change across viewpoints while the scope remains explicit?
4. Are operation definitions distinguishable from execution occurrences?
5. Are capabilities distinguishable from permissions?
6. Are requirements distinguishable from constraints and evidence?
7. Can relationships be interpreted without relying on diagram layout alone?
8. Can the ontology describe software and cyber-physical examples without importing implementation-specific meanings?

## Next milestone

**M2 — Structural Model Research**

Compare layered, multidimensional, graph/ontology, hierarchical, and hybrid forms against explicit criteria. Do not approve a structure until it passes the ontology consistency and cross-domain evaluation.
