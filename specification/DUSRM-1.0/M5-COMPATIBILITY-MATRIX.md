# DUSRM 1.0 Preparation — WP5 Profile Compatibility Matrix

**Status:** Review-preparation matrix; no compatibility approval  
**Target:** DUSRM 1.0-preparation / schema 0.2-draft  
**Date:** 2026-11-11

## 1. Interpretation

This matrix records what is ready for review. `review-prepared` means the profile has an updated mapping fixture and evidence snapshot. It is not the same as compatible, approved or conformant.

| Assessment dimension | Standalone application | ANANTA DBMS | FireBot CPS |
|---|---|---|---|
| SOI boundary explicitly declared | Yes, illustrative | Yes, engine/API scope | Yes, intended integrated scope |
| External participants represented | User and host | Host OS, client, optional JSONL workload | Operator, fireground, host computer |
| Eight-layer applicability represented | Yes | Yes | Yes |
| Responsibilities have primary layer | Yes | Yes | Yes |
| Element-to-responsibility realizations represented | Selected | Selected | Selected |
| Operations/executions/states/interfaces represented | Selected | Selected | Selected |
| Relationship endpoint signatures exercised | 5 | 5 | 6 |
| Evidence source/revision recorded | Illustrative source only | Repository docs and specs | Repository docs and status snapshot |
| Physical implementation claim controlled | Not applicable | Native engine docs; source tests not independently run | Physical hardware marked planned |
| Key unresolved issue | No real application implementation evidence | Conflicting Windows checkpoint statements; API M7.1 in progress | Stale-ish 2026-10-11 status snapshot, physical system unimplemented |
| Compatibility disposition | **not-assessed** | **not-assessed** | **not-assessed** |

## 2. Candidate core concept coverage

| Core concept | Standalone | ANANTA | FireBot |
|---|---|---|---|
| System-of-interest and boundary | Application | Native engine/data platform | Integrated robot system |
| Environment participant | User, host OS/hardware | Host OS, embedding app, optional workload file | Operator, fireground, host |
| Element | Core/UI/store | Engine/catalog/storage/AQL/WAL/API | Dashboard/simulation/power/physical platform/vision/safety |
| Responsibility | Task lifecycle, state, computation, interaction | Resource, execution, storage state, query, API, DBMS capability | Simulation, state, computation, dashboard, local safety, physical platform, rescue outcome |
| Realization | Illustrative allocations | Repository-described engine components | Simulation/dashboard only; physical work planned |
| Operation/execution | CompleteTask | IngestBatch/ExecuteAql | AdvanceSimulation/RequestEmergencyStop |
| State/transition/event | Task active/completed | DB open/locked/recoveryRequired | Autonomous/manual/emergencyStop |
| Interface/interaction | Local user UI | Embedded Rust API | Operator dashboard |
| Resource/allocation | Host resources optional | Working-set limit | Physical power/compute constraints (currently mostly planned/simulated) |
| Requirement/constraint/invariant | Offline local use | Single writer, scoped WAL guarantee | People-first and local safety independence |
| Evidence | Illustrative profile specification | Source docs with revision hashes | Current-state and architecture docs with limitations |

## 3. Registry status

All three registry entries are:
- target core: `1.0-preparation`;
- target schema: `0.2-draft`;
- reconciliation status: `review-prepared`;
- compatibility status: `not-assessed`.

The schema 0.2 semantic validator should emit a profile-compatibility warning for each fixture while that status remains unchanged. That warning is intentional and must not be suppressed in order to obtain a cleaner CI display.

## 4. Criteria for changing a status

No profile may move from `not-assessed` to `compatible` solely because:
- it passes JSON Schema;
- its semantic fixture has no errors;
- its source repository contains tests;
- a profile author believes the mapping is correct.

The change requires a recorded review with core-term preservation, layer mapping, profile refinement/extension review, evidence freshness and limitations, and resolved findings. Any unresolved critical finding must block approval or produce an explicit incompatible/not-assessable disposition.

