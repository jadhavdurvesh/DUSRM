# DUSRM 0.6 — Validation and Domain Profiles

**Status:** Validation draft; non-normative  
**Milestone:** M5 — Validation and Profiles  
**Release label:** 0.6-draft  
**Date:** 2026-11-09

## Objective

Evaluate whether the DUSRM ontology, hybrid eight-layer responsibility structure, and operational semantics can describe systems from different engineering domains without forcing implementation details or duplicating technology specifications.

## Scope of this milestone

The 0.6 draft establishes:
- a repeatable evidence-based validation method;
- domain-profile rules;
- a standalone software application profile and worked example;
- an evidence-based ANANTA database-engine profile;
- an evidence-based FireBot cyber-physical robotics profile;
- a validation results matrix and unresolved-gap register;
- a description-assessment procedure.

## Case studies

1. **Standalone software application:** a small illustrative application used to test whether DUSRM scales down without unnecessary infrastructure.
2. **ANANTA:** a native Rust database and data platform. Mapping is based on its repository documentation and specifications. The profile distinguishes documented/implemented capabilities from planned features and limits.
3. **FireBot:** a software-first firefighting/rescue robot concept with dashboard and simulation work. Its profile distinguishes simulation and contracts from physical hardware, live perception, and live fleet networking.

## Evidence status

The 0.6 case studies are repository-informed documentation exercises. They are not independent tests of the deployed systems, formal proofs, safety assessments, or claims of DUSRM conformance.

Evidence labels used:
- **Documented:** stated in an inspected project document.
- **Repository-reported implemented:** source repository says code or functionality is present; not independently executed in this DUSRM exercise.
- **Simulated:** behavior is explicitly simulated.
- **Planned:** an intended design or capability, not yet implemented.
- **Unverified:** source does not establish implementation or successful operation.
- **Unknown:** insufficient evidence.
- **Not applicable:** outside the declared system boundary.

## Key findings

- The responsibility-based allocation rule is necessary: a single element may realize responsibilities across several layers.
- ANANTA can be described across all eight layers without DUSRM defining its database format, AQL, WAL, or API.
- FireBot requires a strict distinction between software simulation, proposed interfaces, and physical behavior.
- A simple standalone application can use DUSRM without requiring a network, database, or robot-specific layer implementation.
- Layer completeness and boundary clarity remain open research questions. The eight-layer stack is still a candidate structure.

## Not established

- Universal completeness or uniqueness of DUSRM.
- Independent peer review or external adoption.
- Conformance of ANANTA or FireBot to a stable DUSRM standard.
- Correctness or safety of either system.
- Machine-checked validity of every metamodel rule.
- A final, immutable eight-layer architecture.

## Next milestone

**M6 — Conformance, Tooling Readiness, and Publication Preparation**

Refine assessment criteria, create reviewable conformance examples, prepare a versioned profile registry, and decide whether a machine-readable description format is justified. Do not build a validator until the ontology and validation rules have been sufficiently reviewed.
