# DUSRM 0.5 — Formalization Status

**Status:** Formalization draft; non-normative  
**Milestone:** M4 — Formalization  
**Release label:** 0.5-draft  
**Date:** 2026-11-09

## Objective

Consolidate the ontology, structure, and operational semantics into a consistent abstract metamodel, with explicit responsibility allocation, well-formedness rules, invariant obligations, traceability, and assessment foundations.

## Included

- Formal metamodel signature and concept mapping.
- Responsibility-based layer allocation rules.
- Structural and semantic well-formedness conditions.
- Invariant and proof-obligation method.
- Traceability chain and draft conformance levels.
- Domain profile template.
- Formal notation refinements.
- Prior-art boundaries for TLA+, SysML v2/KerML, and Alloy.
- Consistency review and identified open gaps.

## Key formalization decision

Core responsibilities are mapped to one primary layer each. Elements realize responsibilities through a many-to-many relation. An element may therefore be associated with several layers without being split into artificial duplicate components.

## Formal kernel

The transition-system model introduced in 0.4 remains the operational foundation. The 0.5 metamodel links its configurations and transitions to elements, responsibilities, operations, and evidence. It does not define a new temporal logic, proof engine, executable modeling language, or serialization format.

## Status limitations

- Rules are not yet machine-checked.
- No DUSRM schema or parser exists.
- No independent peer review has been completed.
- Layer boundaries remain provisional.
- ANANTA and FireBot mappings remain exploratory until inspected against current specifications and implementations.
- Conformance levels are proposed assessment categories, not certifications.
- No novelty or superiority claim is made.

## Next milestone

**M5 — Validation and Domain Profiles**

Develop evidence-based descriptions for a small application, ANANTA, and FireBot; test cross-layer allocations and invariants; use an appropriate established formal tool for selected properties; and record gaps before revising the core model.
