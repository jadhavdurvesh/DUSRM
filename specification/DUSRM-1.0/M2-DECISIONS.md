# DUSRM 1.0 Preparation — WP2 Ontology Decisions and Review Record

**Work package:** WP2 — Foundational Ontology and Relationship Consolidation  
**Status:** Proposed decisions; awaiting independent review  
**Date:** 2026-11-10

## 1. Proposed core decisions

| ID | Proposed decision | Rationale | Status |
|---|---|---|---|
| WP2-D01 | Keep SOI, Element, Environment Participant, and Description distinct | Avoids scope and representation category errors | Proposed |
| WP2-D02 | Distinguish subject category, kind, and contextual role | A subject may have multiple roles without duplication | Proposed |
| WP2-D03 | Keep Responsibility separate from Requirement, Operation, Capability, and Element | These concepts answer different modeling questions | Proposed |
| WP2-D04 | Reserve Realization for Element-to-Responsibility allocation records | Prevents collision with implementation-to-specification trace | Proposed |
| WP2-D05 | Distinguish Operation specification from Execution occurrence | A defined operation is not evidence of an execution | Proposed |
| WP2-D06 | Treat Event, State/Configuration, Interface, Resource, Capability, Requirement, Constraint, and Evidence as typed ontology concepts | Generic string references are insufficient for reliable relationship checks | Proposed |
| WP2-D07 | Use implements for implementation-to-specification/design trace; deprecate realizes as a general relationship name | Removes ambiguity with the Realization allocation record | Proposed |
| WP2-D08 | Require explicit conceptual signatures for core relationships | Relationship names alone do not determine endpoint types or authority | Proposed |
| WP2-D09 | Reify n-ary or independently characterized relationships | Preserves participant roles, quantities, validity, and evidence | Proposed |
| WP2-D10 | Separate design disposition, realization state, applicability, assessment result, and evidence method/context | These dimensions are not interchangeable | Proposed |
| WP2-D11 | Keep schema and validator versioning independent of the DUSRM conceptual version | Allows tool evolution and compatibility declarations | Proposed |
| WP2-D12 | Do not declare current profiles compatible with 1.0 without review | Registry entries remain not-assessed | Proposed |

## 2. Decisions explicitly not made

WP2 does not:
- publish a new JSON Schema;
- change the 0.1 schema or 0.9 validator;
- claim full machine validation of the proposed relationship matrix;
- approve any domain profile for 1.0;
- claim that a requirement is satisfied because a subject or traceability link exists;
- infer relationship symmetry, transitivity, inverse, exclusivity, causality, or authority;
- claim independent peer review has occurred.

## 3. Review requirements

Before acceptance:
- an ontology/modeling reviewer should inspect category, kind, role, and object boundaries;
- a systems architect should attempt representative models beyond the current three case studies;
- a formal-methods reviewer should assess typed relationship and state/transition definitions;
- a tooling reviewer should check that the proposed typed references can be represented without ambiguity;
- a reviewer should test legacy status migration using conflicting and incomplete evidence cases.

Every objection must be recorded with its scope, supporting example, response, and disposition.

## 4. Review response record

No independent external review has been claimed or received.

| Reviewer | Expertise | Date | Finding | Disposition |
|---|---|---|---|---|
| Pending | Ontology/modeling | Pending | No independent review recorded | Open |
| Pending | Systems architecture | Pending | No independent review recorded | Open |
| Pending | Formal methods/tooling | Pending | No independent review recorded | Open |

## 5. WP2 completion criteria

WP2 documentation is complete when:
- the core model objects and their distinctions are defined;
- relationship semantics and conceptual signatures are recorded;
- n-ary/reified relationship rules are explicit;
- status and evidence dimensions are orthogonal;
- the tooling gaps and migration constraints are accurately documented;
- no existing schema, validator, or profile is overstated as 1.0 conformant;
- independent review remains visible as an open requirement.
