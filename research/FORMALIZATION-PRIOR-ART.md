# DUSRM 0.5 — Formalization Prior-Art Notes

**Status:** Initial research note; non-normative  
**Date:** 2026-11-09

## 1. Purpose

DUSRM formalization must use established mathematical and engineering foundations without claiming those foundations as original. This note identifies relevant neighboring methods and defines the boundary of DUSRM's contribution.

## 2. TLA+ and transition-system reasoning

Leslie Lamport's overview of TLA+ presents state-machine specifications using initial-state and next-state descriptions, with temporal logic for reasoning about behaviors, safety, liveness, and fairness.

**DUSRM use:** The transition-system kernel and invariant proof obligations use related established concepts.

**Boundary:** DUSRM is not TLA+, does not define a substitute temporal logic, and does not claim new transition-system mathematics.

Source: https://lamport.azurewebsites.net/tla/high-level-view.html

## 3. OMG SysML v2 and KerML

OMG describes SysML v2 as a systems modeling language supporting requirements, behavior, structure, analysis, and verification. The official OMG specification page lists the formal SysML 2.0 specification and normative machine-readable artifacts. OMG describes SysML v2 as based on KerML, which provides its semantic foundation.

**DUSRM use:** This demonstrates why DUSRM should remain a reference model and not casually expand into a new general-purpose systems modeling language. DUSRM concepts may be represented in SysML v2 or other modeling tools.

**Boundary:** DUSRM does not redefine SysML, KerML, their syntax, semantics, API, or interchange formats.

Sources:
- https://www.omg.org/sysml/sysmlv2/
- https://www.omg.org/spec/SysML

## 4. Alloy and relational constraint modeling

Alloy documentation describes a language based on signatures, sets, relations, constraints, predicates, and analysis commands. This is relevant to expressing and checking structural relationships and constraints.

**DUSRM use:** Alloy may be evaluated as an external analysis technique for finite structural consistency examples.

**Boundary:** DUSRM does not define an Alloy dialect or its own constraint solver. Any Alloy model would be an optional analysis artifact mapping DUSRM concepts.

Sources:
- https://alloy.readthedocs.io/en/latest/language/
- https://alloy.readthedocs.io/en/latest/language/commands.html

## 5. Architecture and systems engineering references

DUSRM's prior-art register also identifies:
- ISO/IEC/IEEE 42010: architecture descriptions and viewpoints: https://www.iso.org/standard/74393.html
- ISO/IEC/IEEE 15288: system life-cycle processes: https://www.iso.org/standard/81702.html
- ISO/IEC 7498-1: OSI Basic Reference Model: https://www.iso.org/standard/20269.html

These works occupy neighboring but distinct scopes. DUSRM must keep its core conceptual reference model distinct from architecture-description requirements, life-cycle process frameworks, and a communication-focused reference model.

## 6. Originality boundary

The following are not claimed as novel:
- sets, relations, functions, predicates, transition systems;
- state machines, safety, liveness, invariants, or refinement;
- layer diagrams or viewpoints;
- system decomposition and architecture description.

Potential research contribution remains the proposed combination of:
- a cross-domain system ontology;
- responsibility-based allocation to a hybrid layered reference structure;
- explicit cross-layer relationship semantics;
- operational semantics organized across that structure;
- a reusable method for describing and assessing heterogeneous software and cyber-physical systems.

This combination is still a hypothesis requiring literature review, comparison, and external technical review. No novelty or superiority claim is made.
