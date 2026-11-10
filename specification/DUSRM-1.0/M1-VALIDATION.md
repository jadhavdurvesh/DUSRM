# DUSRM 1.0 Preparation — WP1 Layer Boundary Review

**Work package:** WP1 — Layer Definitions and Boundaries  
**Status:** Internal consistency review; non-normative  
**Date:** 2026-11-10

## 1. Review scope

This review checks whether the proposed layer charter and boundary rules can describe:
- a standalone local software application;
- ANANTA as a native database/data platform;
- FireBot as a software-first, planned cyber-physical robotics system.

It is a documentation-level review using existing DUSRM mappings. It is not a new source-code audit, test execution, external peer review, or system conformance assessment.

## 2. Case-study boundary results

### 2.1 Standalone application

| Concern | Proposed primary layer | Boundary rationale | Status |
|---|---|---|---|
| Host computer, display, storage device | L1 | Physical/hosting substrate; external dependency for the application SOI | External dependency |
| Local storage quota or memory budget | L2 | Capacity and resource limits | Illustrative |
| Dispatch of CompleteTask execution | L3 | Execution lifecycle | Illustrative |
| Task identity, fields, completion state | L4 | Meaning and authoritative state | Illustrative |
| Task validation, filtering and derived counts | L5 | Computation and transformation | Illustrative |
| UI event/interface contract | L6 | User/application interaction | Illustrative |
| Create/edit/complete/search task ability | L7 | Consumable application capability | Illustrative |
| Help one user organize tasks | L8 | Stakeholder outcome | Illustrative |

**Finding:** The application does not need a network service or database server to have L6 interaction, L7 capability, or L8 purpose. Its host platform is recorded as an external L1 dependency rather than falsely represented as an internal component.

### 2.2 ANANTA

| Concern | Proposed primary layer | Boundary rationale | Evidence status in existing mapping |
|---|---|---|---|
| Host CPU, memory devices, disks, OS/filesystem substrate | L1 | Hosting substrate | Documented |
| Bounded batches, execution budgets, single-writer ownership limits | L2 | Capacity and ownership constraints | Documented/repository-reported |
| Query iterator lifecycle, cancellation, operation execution | L3 | Execution progression | Documented/repository-reported |
| Schemas, typed values, catalog identities, durable artifacts | L4 | Information and state | Documented/repository-reported |
| AQL parsing, planning, optimization, vectorized computation | L5 | Computational semantics | Documented/repository-reported |
| Embedded API request/result/error contract | L6 | Interaction | Documented; API status remains version-specific |
| Ingestion, scanning, query, analytics, backup/restore capabilities | L7 | Database capabilities | Repository-reported with limits |
| Independent native DBMS/data-platform purpose | L8 | Product/application outcome | Documented goal |

**Finding:** ANANTA illustrates why a database must not be assigned wholly to L4. It realizes information, computation, execution, resource, interface, capability, and product responsibilities. Its engine and APIs remain defined by ANANTA's own specifications.

### 2.3 FireBot

| Concern | Proposed primary layer | Boundary rationale | Evidence status in existing mapping |
|---|---|---|---|
| Chassis, motors, cameras, LiDAR, batteries, compute boards | L1 | Physical substrate | Planned/unconnected in inspected project status |
| Available energy, load budgets, compute/network capacity | L2 | Resource capacity and allocation | Simulated/planned |
| Command arbitration, execution lifecycle, local emergency-stop state | L3 | Runtime control and actuation progression | Simulation/contracts; physical control unverified |
| Pose, map, detection, mission and power state | L4 | Information/state representation | Contracts/simulation |
| Perception, sensor fusion, localization, route planning | L5 | Computation and inference | Mixed simulated/planned/unverified |
| Operator, subsystem, station, and fleet contracts | L6 | Interaction and coordination | Contracts/proposals |
| Detection, navigation assistance, alerts, diagnostics, firefighting support | L7 | Consumable capabilities | Software/simulation/planned |
| People-first rescue and firefighting objectives | L8 | Mission outcomes and priorities | Documented goal; real-world outcome unverified |

**Finding:** FireBot makes the L3/L5 and L7/L8 boundaries important. A vision algorithm derives a detection at L5; L3 controls whether and how a resulting command executes; the detection service is a capability at L7; rescue priority and mission success belong at L8. Physical hardware remains L1 and planned until evidence changes.

## 3. Findings and disposition

| ID | Finding | Disposition |
|---|---|---|
| WP1-F01 | L1 and L2 were blended in references to storage, memory, and power | Clarified as substrate versus available/allocated capacity |
| WP1-F02 | L3 and L5 were blended in operation wording | Clarified as execution lifecycle versus computational meaning |
| WP1-F03 | L4 and L5 could both claim data processing | Clarified as information meaning/state versus transformation |
| WP1-F04 | L6 and L7 both used service/interface language | Clarified as interaction contract versus consumable capability |
| WP1-F05 | L7 and L8 could both describe a workflow | Clarified as provided capability versus stakeholder/mission outcome |
| WP1-F06 | L1 external hosting dependencies could be misrepresented as internal realizations | Added external-dependency applicability state |
| WP1-F07 | Stack arrows could be read as a strict pipeline | Proposed layer order as a reading convention only |

## 4. WP1 result

**Documentation result: complete with review findings open.**

The eight layer definitions and boundary tests have been tightened, and all three existing case studies can be explained using the proposed distinctions without altering the source project repositories.

This does not mean the eight-layer model is complete or universally valid, the layer names are approved, the case-study implementations are verified, the definitions have received independent peer review, or DUSRM 1.0 is ready for release.

## 5. Next work package

**WP2 — Foundational Ontology and Relationship Consolidation**

Review entity kinds, responsibility semantics, relationship signatures, evidence/status vocabulary, and compatibility with the layer charter and DUSRM tooling.
