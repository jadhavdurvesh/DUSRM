# DUSRM 1.0 Preparation — WP5 Independent Review Cases

**Status:** Proposed reviewer scenarios; not independent test evidence  
**Date:** 2026-11-11

These cases are designed to challenge the profile/core mapping. They are not claims that an external reviewer has run them.

| ID | Profile | Scenario / question | Expected DUSRM behavior | Evidence needed |
|---|---|---|---|---|
| WP5-R01 | Standalone | A local task application has no network service. Is L6 still meaningful? | Model local UI/human interaction in L6; do not require network or distributed coordination. | Review of interaction semantics and a transient/local-persistence variant. |
| WP5-R02 | Standalone | The same application is built with transient state and local-file persistence. | Model two deployment/design variants without redefining task state or creating a mandatory database layer. | Two descriptions or a documented variation point; persistence failure behavior. |
| WP5-R03 | Standalone | One in-process component realizes L3, L4 and L5 responsibilities. | Permit one element to realize multiple responsibilities across layers. Do not require one component per layer. | Realization graph and layer allocation rationale. |
| WP5-R04 | ANANTA | A second independent writer attempts to open the same database. | Preserve the documented exclusive writer boundary; do not infer multi-writer or MVCC support. | Source contract and targeted lock tests in ANANTA. |
| WP5-R05 | ANANTA | A supported operation has a durable WAL COMMIT but final artifact publication is interrupted. | Model the recovery-required state and idempotent redo/fail-closed conditions only within the documented operation boundary. | Crash-point test matrix and platform-specific recovery output. |
| WP5-R06 | ANANTA | A reviewer reads the README and WAL specification for Windows checkpoint rotation. They disagree. | Treat the conflicting claims as an evidence/version conflict; do not silently pick one. | Updated authoritative ANANTA specification and matching CI evidence. |
| WP5-R07 | ANANTA/FireBot | ANANTA imports a FireBot JSONL file. Does this prove live integration? | No. Represent an optional file-based workload adapter and keep a network/live integration claim absent. | Connector source, input schema, provenance and a reproducible file-ingestion test. |
| WP5-R08 | FireBot | Dashboard shows a synthetic thermal-zone temperature and synthetic cooling failure. | Mark it simulated; never label it measured physical telemetry. | Simulation fixture/source and explicit status/provenance fields. |
| WP5-R09 | FireBot | No motors, sensors, batteries or pump are connected. Can the profile still describe L1? | Yes, when the SOI is the intended integrated robot, but mark hardware elements and related responsibilities planned. | Current-state snapshot and hardware bring-up evidence before changing maturity. |
| WP5-R10 | FireBot | The host dashboard/network becomes unavailable while the robot is operating. | The intended local emergency-stop and immediate safety functions remain independent; a remote service is not the safety authority. | Local controller architecture, hazard analysis and hardware-in-loop tests. |
| WP5-R11 | FireBot | A remote command tries to clear an emergency stop. | Reject or ignore it unless an explicit local authorized reset sequence permits the transition. | Approved safety requirements, state-machine review and physical tests. |
| WP5-R12 | FireBot | Vision, mapping or Hive Mind status is stale or unavailable. | Preserve unknown/stale status; do not infer that a sector is clear or that a remote robot is absent/present. | Contract tests for expiry, freshness, missing data and degraded operation. |
| WP5-R13 | All | A profile adds a new domain term that overlaps a core relationship. | Require a profile extension/refinement with explicit owner/version and prohibit silent core redefinition. | Extension schema, mapping rule and composition conflict test. |
| WP5-R14 | All | Two profiles are used in one system description and impose conflicting constraints. | Report not-assessed/incompatible until an explicit composition resolution is reviewed. | Profile pair compatibility declaration and conflict-resolution decision. |

## Reviewer disposition template

For each case, record:
- reviewer and expertise;
- date and exact repository commit;
- expected behavior accepted/rejected;
- source evidence and test artifact;
- finding severity (blocker, major, minor, observation);
- required correction;
- owner and closure reference.

A passing fixture is not a substitute for an independent review conclusion.
