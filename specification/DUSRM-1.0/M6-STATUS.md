# DUSRM 1.0 Preparation — WP6 Status

**Work package:** WP6 — SAND OS Adoption Pilot and Release-Gate Review  
**Status:** DUSRM-side OS profile and adoption package prepared; CI passed; SAND-side adoption and independent review pending  
**Date:** 2026-11-11

## Objective

Make DUSRM usable for SAND OS architecture description and CI validation while preserving SAND's independent boot, kernel, Veyra, SAPP and SANDFS contracts.

## Deliverables

- [SAND OS adoption plan](M6-SAND-OS-ADOPTION.md)
- [SAND OS architecture mapping](M6-SAND-OS-ARCHITECTURE-MAP.md)
- [WP6 desk review findings](M6-REVIEW-FINDINGS.md)
- [SAND OS implementation plan](M6-IMPLEMENTATION-PLAN.md)
- [Standards crosswalk](M6-STANDARDS-CROSSWALK.md)
- [WP6 validation report](M6-VALIDATION.md)
- [DUSRM profile — Operating System](../../profiles/operating-system/PROFILE.md)
- [SAND OS schema 0.2 fixture](../../schema/fixtures/0.2/profiles/sand-os-operating-system.json)
- [SAND OS profile regression tests](../../tests/test_sand_os_profile_0_2.py)

## Automated validation

The dedicated [WP6 DUSRM CI run](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813575) passed on 2026-11-11 at commit `2c0cc444303dafdb443f077dccdb8835fb84d4d9`.

- 22 schema 0.2 semantic/migration tests passed.
- 4 existing domain profile tests passed.
- 8 SAND OS profile tests passed.
- The SAND OS profile CLI returned zero semantic errors and the expected single profile compatibility warning.
- The migration smoke test passed.

The [schema 0.1](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813742), [0.8](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813499) and [0.9](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813600) validation workflows also passed on the tested commit.

## SAND OS repository boundary

SAND OS (`jadhavdurvesh/sand-os`) was inspected read-only at tree `661cdedd38e2e24e202dee22798047fd7311353a`. No SAND OS files, branches, commits, workflows or releases were created, modified or deleted.

DUSRM is proposed as a design-time architecture description and host-side validation input only. It is not a kernel module, syscall, Veyra service, boot component or runtime dependency.

## Profile outcome

The operating-system profile is registered as `DUSRM-PROFILE-OPERATING-SYSTEM-0.1`, candidate core `1.0-preparation`, candidate schema `0.2-draft`, reconciliation state `review-prepared`, compatibility state `not-assessed`.

The fixture maps SAND's nine implementation strata many-to-many to DUSRM's eight responsibility layers. It does not assert one-to-one layer equivalence.

## Open review findings

- README status says M0 while detailed architecture/roadmap and CI show later process, storage and graphics milestones.
- Scheduler header declares eight thread slots while the architecture narrative mentions four descriptors/stacks.
- SAPP SDK identifies v0.2 while the format document labels the container v0.1.
- Veyra is a descriptor/status foundation, not a stable general-purpose syscall ABI or service IPC.
- SANDFS v1 remains a limited filesystem prototype without journaling/crash consistency/permissions/concurrency locks.
- SAPP signing and trust-store verification are absent.
- SAND's security policy says experimental and unsuitable for production/safety-critical use.

See [WP6 review findings](M6-REVIEW-FINDINGS.md). These questions are not resolved by DUSRM and do not invalidate the successful QEMU CI pass.

## Standards relationship

DUSRM complements ISO/IEC/IEEE 42010:2022, ISO/IEC/IEEE 15288:2023 and OMG SysML v2 rather than replacing architecture-description, lifecycle-process or systems-modeling standards. See [standards crosswalk](M6-STANDARDS-CROSSWALK.md).

## Exit criteria and next step

WP6 is complete as a DUSRM-side SAND OS adoption pilot, but SAND-side adoption is not approved or implemented. Required next actions:
1. Review the architecture map and findings with the SAND OS owner.
2. Reconcile SAND source-document inconsistencies in SAND only after separate authorization.
3. Obtain independent architecture/schema review.
4. Obtain separate explicit authorization before adding a DUSRM reference file or host-side CI validation job to SAND.
5. Pin validator/schema versions and keep DUSRM outside the SAND runtime.

## Next work package

**WP7 — Independent Review Findings and SAND OS Adoption Approval**

Resolve DUSRM core/profile review findings, obtain approval for any SAND-side adoption changes, and determine whether a DUSRM 1.0 release candidate is justified. Do not declare a stable release without explicit governance approval.
