# Architecture Research

This directory develops and evaluates the structural form of DUSRM.

## Current milestone

**DUSRM 0.3 — Structural Architecture (candidate, non-normative)**

Current recommendation: a **hybrid reference structure** consisting of:
1. A system context frame.
2. Eight responsibility layers.
3. A typed relationship graph.
4. Cross-cutting concern overlays.
5. Multiple viewpoints.

## Documents

- [Structural candidate evaluation](STRUCTURE-CANDIDATES.md) — compares strict layering, viewpoints, graph ontology, hierarchy, and hybrid structure.
- [Proposed reference structure](DUSRM-REFERENCE-STRUCTURE-0.3.md) — defines the candidate eight-layer structure and cross-cutting concerns.
- [Layer contract rules](LAYER-CONTRACTS.md) — reusable template and boundary rules.

## Design rule

Do not select a structure merely because it resembles OSI. Layering must make responsibilities clearer, and non-adjacent relationships, feedback, and cross-cutting concerns must remain representable.

The candidate architecture is not frozen. Revisions should be supported by cross-domain examples and documented rationale.
