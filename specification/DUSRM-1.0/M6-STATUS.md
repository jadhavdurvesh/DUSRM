# DUSRM 1.0 Preparation — WP6 Status

**Work package:** WP6 — Independent Review Findings and Release Candidate Gate  
**Status:** SAND OS adoption pilot model and review package prepared; independent review and SAND-side adoption approval pending  
**Date:** 2026-11-11

## Objective

Make DUSRM usable for SAND OS architecture description and CI validation while preserving SAND's independent boot, kernel, Veyra, SAPP and SANDFS contracts.

## Deliverables

- [SAND OS adoption plan](M6-SAND-OS-ADOPTION.md)
- [SAND OS architecture mapping](M6-SAND-OS-ARCHITECTURE-MAP.md)
- [WP6 desk review findings](M6-REVIEW-FINDINGS.md)
- [SAND OS implementation plan](M6-IMPLEMENTATION-PLAN.md)
- [Standards crosswalk](M6-STANDARDS-CROSSWALK.md)
- [DUSRM profile — Operating System](../../profiles/operating-system/PROFILE.md)
- [SAND OS schema 0.2 fixture](../../schema/fixtures/0.2/profiles/sand-os-operating-system.json)
- [SAND OS profile regression tests](../../tests/test_sand_os_profile_0_2.py)
- [WP6 validation report](M6-VALIDATION.md)

## SAND OS repository boundary

SAND OS (`jadhavdurvesh/sand-os`) was inspected read-only at tree `661cdedd38e2e24e202dee22798047fd7311353a`. No SAND OS branch, file, commit, workflow or release was modified.

DUSRM is proposed as a design-time architecture description and host-side CI validation input only. It is not a kernel module, syscall, Veyra service, boot component or runtime dependency.

## Profile outcome

The new operating-system profile is registered as `DUSRM-PROFILE-OPERATING-SYSTEM-0.1`, candidate core `1.0-preparation`, candidate schema `0.2-draft`, reconciliation state `review-prepared`, compatibility state `not-assessed`.

The SAND OS fixture represents its nine architecture strata as a many-to-many mapping onto DUSRM's eight responsibility layers. No one-to-one layer equivalence is asserted.

## Open desk-review findings

- README status says M0 while detailed architecture/roadmap and current CI show later process, storage and graphics milestones.
- Scheduler header declares eight thread slots while the architecture narrative mentions four descriptors/stacks.
- SAPP SDK identifies v0.2 while the format document labels the container v0.1.
- Veyra is a descriptor/status foundation, not a stable general-purpose syscall ABI or service IPC.
- SANDFS v1 remains a limited filesystem prototype without journaling/crash consistency/permissions/concurrency locks.
- SAPP signing and trust-store verification are absent.
- SAND's security policy says experimental and unsuitable for production/safety-critical use.

See [WP6 review findings](M6-REVIEW-FINDINGS.md). These questions are not resolved by DUSRM and do not invalidate the latest QEMU CI pass.

## Standards crosswalk

DUSRM should complement ISO/IEC/IEEE 42010:2022, ISO/IEC/IEEE 15288:2023 and OMG SysML v2 rather than replace architecture-description, lifecycle-process or system-modeling standards. See [standards crosswalk](M6-STANDARDS-CROSSWALK.md).

## Exit criteria

WP6 is not a stable 1.0 release gate closure yet. Required next actions:
1. Validate the SAND OS profile fixture and tests in DUSRM CI.
2. Review the layer/strata mapping and evidence with the SAND OS owner.
3. Reconcile SAND source-document inconsistencies in the SAND repository only after separate authorization.
4. Obtain independent architecture/schema review.
5. Only after a separately approved SAND-side adoption step, add a pinned host-side DUSRM validation job to SAND CI.

Do not change compatibility status to compatible or declare DUSRM 1.0 stable based only on internal fixture/CI success.
