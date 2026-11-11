# DUSRM 1.0 Preparation — WP5 Status

**Work package:** WP5 — Domain Profile Reconciliation and Independent Review Preparation  
**Status:** Internally complete; profile fixtures and CI passed; independent review pending  
**Date:** 2026-11-11  
**Assessment target:** DUSRM 1.0-preparation / schema 0.2-draft

## Objective

Reconcile standalone application, ANANTA and FireBot profiles against the 1.0-preparation ontology/schema, preserve maturity and evidence boundaries, and prepare independent reviewer cases.

## Deliverables

- [Profile reconciliation report](M5-RECONCILIATION.md)
- [Compatibility matrix](M5-COMPATIBILITY-MATRIX.md)
- [Independent reviewer cases](M5-REVIEW-CASES.md)
- [Read-only evidence snapshot](M5-EVIDENCE-SNAPSHOT.md)
- [Proposed decisions](M5-DECISIONS.md)
- [Independent reviewer package](M5-REVIEW-PACKAGE.md)
- [Automated validation report](M5-VALIDATION.md)
- [Schema 0.2 profile fixtures](../../schema/fixtures/0.2/profiles/)
- [Profile regression tests](../../tests/test_profiles_0_2.py)

## Profile outcomes

| Profile | Fixture status | Compatibility |
|---|---|---|
| Standalone application | Structural and semantic CI passed | not-assessed |
| ANANTA DBMS | Structural and semantic CI passed | not-assessed |
| FireBot CPS | Structural and semantic CI passed | not-assessed |

The profile registry targets DUSRM 1.0-preparation/schema 0.2-draft while preserving the original profile IDs/versions and `not-assessed` compatibility status. `review-prepared` means only that a mapping and review materials exist.

## Automated validation

The dedicated [WP5 CI run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43020354463) passed on 2026-11-11 at commit `59167c68120c968a416c146f15f6fdbdfedfea96`.

- 22 schema 0.2 semantic/migration tests passed.
- 4 profile regression tests passed.
- All three profile CLI checks reported zero semantic errors and the expected single not-assessed compatibility warning.
- The migration smoke test passed.

The [schema 0.1](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43020348588), [0.8](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43020368107) and [0.9](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43020368182) workflows also passed on the same commit.

These runs validate fixtures and the implemented check subset only; they are not profile approvals or independent review.

## Preserved evidence limits

- ANANTA remains an independently specified native database; its FireBot JSONL workload is a file-based adapter, not live integration.
- ANANTA's inspected README and older WAL/concurrency specifications disagree on Windows checkpoint rotation support. This remains open.
- ANANTA's embedded API M7.1 status remains in progress in the inspected source.
- FireBot's inspected current-state snapshot is dated 2026-10-11 and reports physical hardware and several integrations pending/unverified.
- The standalone profile is illustrative; no deployed application was used.
- No independent reviewer has responded yet.

## Repository boundary

All WP5 work is in DUSRM. ANANTA and FireBot files were fetched for read-only source inspection only. SAND OS was not consulted or modified in WP5.

## Exit criteria

WP5 is complete as an internal reconciliation and reviewer-preparation milestone. Its remaining external gate is independent review, source-conflict resolution and explicit profile compatibility decisions. Do not change compatibility status without documented reviewer disposition.

## Next work package

**WP6 — SAND OS Adoption Pilot and Release-Gate Review: DUSRM-side pilot complete.** See [WP6 status](M6-STATUS.md).

The next work package is **WP7 — Independent Review Findings and SAND OS Adoption Approval**.
