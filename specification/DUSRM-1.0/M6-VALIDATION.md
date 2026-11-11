# DUSRM 1.0 Preparation — WP6 SAND OS Profile Validation

**Work package:** WP6 — SAND OS Adoption Pilot and Release-Gate Review  
**Status:** DUSRM-side profile validation passed; SAND-side adoption approval pending  
**Date:** 2026-11-11  
**Commit checked:** `2c0cc444303dafdb443f077dccdb8835fb84d4d9`

## 1. Dedicated DUSRM CI

- Workflow: DUSRM 1.0 preparation — Schema 0.2 and semantic validation
- Run: [WP6 profile validation](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813575)
- Conclusion: **success**
- Job: Validate schema, semantics and migration
- Schema 0.2 semantic/migration regression tests: **22 passed**
- Existing domain profile tests: **4 passed**
- SAND OS profile tests: **8 passed**
- Schema structural fixtures: passed
- Minimal and SAND OS legacy-pilot semantic fixtures: passed without findings
- Loss-aware migration smoke test: passed

## 2. SAND OS profile fixture

Fixture: [sand-os-operating-system.json](../../schema/fixtures/0.2/profiles/sand-os-operating-system.json)

The eight SAND OS-specific tests validate:
1. Draft 2020-12 schema acceptance;
2. no semantic errors;
3. explicit not-assessed compatibility state and warning;
4. eight DUSRM layers mapped to nine SAND implementation strata without one-to-one conflation;
5. DUSRM remains a design-time method, not a SAND runtime dependency;
6. planned networking, service IPC and compositor remain planned;
7. security and SANDFS maturity limitations remain visible;
8. the recorded QEMU CI evidence identifies the inspected SAND OS revision and simulation context.

The SAND OS semantic CLI returned **zero errors and one expected warning**:
- `DUSRM-02-P-001`: profile compatibility is not explicitly approved by the registry.

The warning must remain until an explicit compatibility review is recorded.

## 3. Legacy compatibility

The following validation workflows passed on the same commit:
- [Schema 0.1 validation](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813742) — success.
- [DUSRM 0.8 semantic and formal validation](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813499) — success.
- [DUSRM 0.9 advanced model validation](https://github.com/jadhavdurvesh/DUSRM/actions/runs/43024813600) — success.

## 4. SAND OS source evidence

The profile uses read-only source inspection of `jadhavdurvesh/sand-os` at tree `661cdedd38e2e24e202dee22798047fd7311353a`. The latest inspected [SAND OS Native Boot CI run](https://github.com/jadhavdurvesh/sand-os/actions/runs/42876341368) passed at that repository revision.

The run was a QEMU/emulator workflow. It does not prove physical hardware compatibility, production security, stable general-purpose syscall ABI, filesystem crash consistency or complete OS functionality.

## 5. Repository boundary

All profile fixture, test, CI and documentation writes were confined to DUSRM. SAND OS was inspected read-only; no SAND OS branch, file, commit, workflow or release was modified. The DUSRM test does not clone or mutate SAND OS.

## 6. Limitations and exit gate

- DUSRM OS profile compatibility remains `not-assessed`.
- SAND documentation inconsistencies in README milestone status, scheduler capacity and SAPP version labels remain open.
- SAND's Veyra ABI and service IPC remain incomplete; SANDFS and SAPP remain prototypes; the security policy states the OS is not production-ready.
- DUSRM validation is architecture-description consistency, not OS code verification, security audit or physical hardware testing.
- No SAND-side CI adoption step has been implemented.

**Outcome:** the DUSRM-side SAND OS profile fixture and its regression checks pass. SAND-side adoption still requires separate owner approval, source-document reconciliation and a future host-only CI integration review.
