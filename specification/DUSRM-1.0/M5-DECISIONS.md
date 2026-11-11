# DUSRM 1.0 Preparation — WP5 Profile Reconciliation Decisions

**Status:** Proposed internal decisions; compatibility remains not-assessed  
**Date:** 2026-11-11

| ID | Decision | Rationale | Status |
|---|---|---|---|
| WP5-D01 | Keep legacy profile identity/version 0.1-draft | Preserve historical profile IDs and source documents | Accepted for preparation |
| WP5-D02 | Set current assessment target to DUSRM 1.0-preparation/schema 0.2-draft | Profiles are being reconciled against the candidate 1.0 metamodel | Implemented in registry |
| WP5-D03 | Keep all three compatibility statuses not-assessed | Internal fixture success is not independent compatibility review | Required |
| WP5-D04 | Use separate schema 0.2 profile fixtures in DUSRM | Enables repeatable structural and semantic review without mutating source system repositories | Implemented |
| WP5-D05 | Model ANANTA transaction and WAL boundaries narrowly | Avoid overclaiming MVCC, multi-operation ACID or universal physical durability | Implemented in pilot |
| WP5-D06 | Mark FireBot physical hardware and local safety controller planned | Inspected current-state snapshot reports no connected physical platform | Implemented in pilot |
| WP5-D07 | Treat ANANTA Windows checkpoint wording as an unresolved evidence conflict | Source documents disagree; DUSRM must not choose an unverified statement | Open |
| WP5-D08 | Treat ANANTA FireBot workload as file-based JSONL only | The workload README does not establish live integration | Implemented in pilot |
| WP5-D09 | Do not approve profile composition in WP5 | The three separate profile exercises do not test a combined-profile system description | Open |
| WP5-D10 | Require independent reviewers to disposition open findings before any profile compatibility update | Prevents CI success being misrepresented as profile approval | Required |

## Decisions not made

WP5 does not approve any profile as compatible, does not approve FireBot safety behavior, does not certify ANANTA durability, does not prove standalone application implementation, and does not declare DUSRM 1.0 stable.
