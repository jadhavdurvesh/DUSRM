# DUSRM 1.0 Preparation — WP5 Domain Profile Reconciliation

**Work package:** WP5 — Domain Profile Reconciliation and Independent Review Preparation  
**Status:** Internal reconciliation draft; profile compatibility remains not-assessed  
**Date:** 2026-11-11  
**Assessment target:** DUSRM 1.0-preparation / schema 0.2-draft

## 1. Purpose and boundary

WP5 reconciles the three existing domain profiles against the current DUSRM 1.0-preparation ontology, schema 0.2 and semantic validator:

1. Standalone software application
2. Native database engine (ANANTA)
3. Cyber-physical robotics (FireBot)

This work checks whether the profile descriptions can be expressed by the draft core and whether current source evidence supports their stated maturity boundaries. It is an internal mapping/review-preparation exercise. It is **not** independent peer review, profile approval, system verification, or a compatibility certification.

All source inspections were read-only. No files were created, modified, deleted or committed in ANANTA, FireBot, or SAND OS repositories.

## 2. Reconciliation method

For each profile:
- identify the system-of-interest and its boundary;
- identify external participants and platform dependencies;
- map profile responsibilities to one primary DUSRM layer;
- map profile concepts to typed schema 0.2 objects;
- preserve the distinction between implementation, simulation, planned work and unverified behavior;
- attach repository evidence with source revision identifiers and limitations;
- check the profile fixture against schema 0.2 and the current semantic validator;
- record uncovered concepts and reviewer questions.

A clean schema/semantic result means only that the fixture is internally consistent under the implemented check set. It does not imply that the profile is compatible with the full DUSRM ontology.

## 3. Summary matrix

| Profile | Domain coverage | Main core fit | Main open issue | Compatibility |
|---|---|---|---|---|
| Standalone application | Single-user local application with optional persistence | All eight layers can be represented without requiring network or database subsystems | Existing profile is illustrative and not backed by an identified deployed application; persistence variants need separate descriptions | Not assessed |
| ANANTA DBMS | Native storage, catalog, AQL, execution, embedded API and scoped WAL recovery | Strong mapping across L2–L8; L1 correctly remains an external host platform | Source specifications disagree on some Windows checkpoint/durability details; M7.1 API remains in progress | Not assessed |
| FireBot CPS | Software dashboard/simulation plus intended physical robot and safety/control subsystems | Core model can distinguish simulation, physical platform, interfaces, mission outcomes and external fireground context | Current-state snapshot is dated 2026-10-11; hosted/test verification and physical realization remain outstanding in inspected evidence | Not assessed |

## 4. Standalone software application

### Fit

The profile is a useful scale-down test. The model can express:
- host computer and operating system as external participants;
- application logic, local UI and task state as internal elements;
- L2 resource use without requiring a dedicated database or resource-manager component;
- L3 task operations, L4 task state and L5 filtering/sorting as different responsibilities;
- L6 human interaction without a network protocol;
- L7 application capabilities and L8 individual-user outcome.

The profile fixture describes a task-list application as an illustrative design. It does not claim a deployed product.

### Gaps and questions

- The profile needs explicit variants for transient state and local-file persistence. These are different design descriptions, not necessarily different core profiles.
- The original profile's task-state transition is conceptual; any implementation must define persistence failure, duplicate events, concurrency and recovery.
- The profile is not evidence that all standalone applications have the same responsibility allocation.
- The profile should clarify which host resource concerns are modeled as external dependencies versus application-owned abstractions.

**Internal mapping result:** schema/validator expressive enough for the illustrative case; no compatibility approval.

## 5. ANANTA database-engine profile

### Fit

The ANANTA mapping retains the product's own technical contracts and models:
- L1 as external host OS/filesystem/device primitives;
- L2 as batch/working-set limits and exclusive writer ownership;
- L3 as query, scan, ingestion and DDL execution lifecycles;
- L4 as catalog, schema snapshots, native artifacts and WAL state;
- L5 as AQL parsing/planning and supported analytical operators;
- L6 as the in-process embedded API and AQL client boundary;
- L7 as supported database capabilities;
- L8 as the independent native database/data-platform purpose.

The fixture explicitly models the embedded Rust API as an in-process interface, not a stable network server protocol.

### Guarantee boundaries preserved

The inspected transaction/concurrency specification describes operation-scoped atomic redo units, one exclusive writer owner, and shared-reference readers through the same open handle. It explicitly excludes arbitrary user-defined multi-operation atomicity, savepoints, MVCC and general ACID claims.

The WAL specification limits redo to named immutable artifacts and supported metadata operations. It does not establish universal physical power-loss immunity.

The optional FireBot workload is a privacy-minimized, file-based JSONL connector targeting `ananta.firebot_events`. It is not a live FireBot database/network connection or evidence of production telemetry ingestion.

### Evidence conflict requiring owner clarification

The current ANANTA README describes Windows checkpoint rotation using `MoveFileExW(REPLACE_EXISTING | WRITE_THROUGH)` and refers to a targeted Windows CI job. The inspected transaction/concurrency and WAL-recovery specifications still contain older statements that checkpoint rotation is Unix-only or unsupported on Windows. These source statements are inconsistent. WP5 does not choose one as authoritative; the ANANTA owner should update the superseded specification(s) or identify the exact version/platform scope.

### Other gaps

- The embedded API contract says M7.1 is in progress.
- Source code/build/test execution was not performed as part of this DUSRM profile exercise.
- The current schema fixture captures selected behavior; it does not encode every storage artifact, catalog identity, WAL frame or query-plan semantic.
- Resource budgets are in-process execution limits, not a durable configuration or server-wire contract.

**Internal mapping result:** schema/validator can express the selected architecture and guarantees; source conflict and profile compatibility remain open.

## 6. FireBot cyber-physical robotics profile

### Fit

The profile distinguishes:
- the intended integrated robot system;
- current dashboard and software simulation;
- future physical chassis, motors, cameras, sensors, batteries and pump;
- planned vision, mapping, firmware, fleet and safety-controller capabilities;
- external operator, host computer and fireground environment.

Responsibilities distinguish simulated execution, state, computation and dashboard interaction from planned physical control and mission outcomes.

### Maturity and safety boundaries preserved

The inspected `CURRENT_STATE.md` snapshot is dated 2026-10-11. It reports no physical sensors, motors, pump, batteries, cooling system or microphone connected. It also says hosted deployment and full Node.js test execution still require verification, while real vision AI, live mapping and Hive Mind networking remain pending/unverified.

The FireBot architecture and integration plans require local emergency-stop and time-sensitive safety paths to remain independent of host software and network services. In WP5 this is a planned safety requirement, not a demonstrated physical safety function.

The fixture marks thermal readings as synthetic, physical platform capabilities as planned, and the safety controller as planned. It does not claim physical hazard mitigation, certified control, validated real-time behavior, or mission success in a fire environment.

### Gaps and questions

- Refresh the source snapshot before any later compatibility decision; the 2026-10-11 current-state document may have been superseded.
- Run the FireBot repository's actual Node.js tests and verify hosted deployment independently.
- Define a typed profile concept for measurement provenance, freshness, coordinate frame and uncertainty. The current fixture uses a profile namespace extension; the semantic validator does not yet validate all such extension semantics.
- Keep local safety authority, emergency stop, manual override and hardware interlocks separate from remote mission coordination.
- Physical integration requires separate hazard analysis, electrical/mechanical review and hardware-in-the-loop evidence.

**Internal mapping result:** schema/validator can represent a software-first CPS description and its planned physical scope; safety and profile compatibility remain not assessed.

## 7. Cross-profile findings

### WP5-F01 — Profile refinement versus core responsibility

The profiles map responsibilities to L1–L8, but do not yet provide a complete machine-readable parent-child refinement graph for all profile-local responsibilities. A future profile vocabulary should make the parent core responsibility explicit without changing its meaning.

### WP5-F02 — Profile extensions are structurally open but semantically weak

Schema 0.2 permits namespaced extensions, but the current validator does not validate extension schemas or extension-to-core mapping rules. Extension owners, versioning and conflict detection need a documented registry and tests before extensions can be relied on for conformance.

### WP5-F03 — Applicability and evidence are not proof

The fixtures include layer applicability, evidence references and maturity states. The validator does not decide whether a layer assignment is correct, whether evidence is independent/current/sufficient, or whether a profile's domain constraints are satisfied in the real system.

### WP5-F04 — Compatibility is per target and per version

The legacy profiles were authored against earlier core drafts. Retargeting the registry to DUSRM 1.0-preparation/schema 0.2 identifies the assessment target only; it does not establish backward compatibility. Each profile needs an explicit reviewer disposition.

### WP5-F05 — Profile composition remains unassessed

The three profiles are assessed separately in this package. No cross-profile combination or composition rule is approved. The ANANTA/FireBot workload relationship is only an optional file-based connector; it must not be treated as a composite profile or live integrated system.

## 8. Automated fixture result

The three new schema 0.2 profile fixtures are checked by:
- Draft 2020-12 structural validation;
- the schema 0.2 semantic validator;
- explicit registry checks ensuring the compatibility warning remains visible.

The test suite expects no semantic errors and expects exactly one not-assessed compatibility warning per fixture. This test is evidence of mapping consistency only, not an approval.

## 9. WP5 recommendation

Proceed to independent review with all three profiles marked `not-assessed`. Do not change any registry compatibility status to `compatible` until reviewers have:
- checked the core and profile mappings;
- reviewed the source evidence and freshness;
- resolved the ANANTA source conflict;
- confirmed FireBot maturity and safety wording;
- evaluated extension semantics and profile composition limits;
- documented findings and acceptance decisions.

