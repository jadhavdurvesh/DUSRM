# DUSRM 1.0 Preparation — WP6 SAND OS Implementation Plan

**Scope:** future SAND-side adoption proposal  
**Current state:** no SAND OS repository changes authorized or made

## Phase 0 — Read-only architecture model

- [x] Inspect SAND OS repository architecture, roadmap, integration guide, API catalogue, security policy, Veyra ABI and SAPP format.
- [x] Create operating-system profile and SAND OS schema 0.2 fixture in DUSRM.
- [x] Record source revision identifiers and limitations.
- [x] Validate fixture in DUSRM CI.
- [ ] Project owner reviews architecture map and findings.

**Exit:** owner agrees that the DUSRM fixture accurately describes the current SAND OS architecture and maturity.

## Phase 1 — DUSRM-side CI proof (no SAND repo mutation)

- [x] Add JSON profile fixture.
- [x] Add structural and semantic regression test.
- [x] Add a CI workflow step in DUSRM.
- [ ] Keep a known-good pinned schema/validator revision for the future SAND workflow.
- [ ] Produce a reproducibility command bundle for local host validation.

**Exit:** DUSRM can validate its SAND OS description deterministically on its own CI.

## Phase 2 — Proposed SAND-side reference only

Requires separate approval before implementation.

Suggested future SAND tree location:
`architecture/dusrm/sand-os-architecture-0.2.json`

Possible supporting files:
- `architecture/dusrm/README.md` — scope, owner and version pin.
- `architecture/dusrm/evidence-map.md` — cross-links to authoritative SAND docs and CI.
- `architecture/dusrm/compatibility.json` — core/profile/schema versions and reviewed compatibility state.

Avoid copying a full DUSRM validator into SAND. Prefer a pinned external validator/tool release or CI action with checksum/version pinning, unless the project intentionally vendors a reviewed tool.

## Phase 3 — SAND CI validation step (proposed)

A future host-side workflow step could:
1. check out SAND source;
2. fetch or install a pinned DUSRM validator/schema package (or vendor a reviewed immutable release);
3. validate `architecture/dusrm/sand-os-architecture-0.2.json`;
4. upload machine-readable findings as CI artifacts;
5. fail the architecture-validation job for schema/semantic errors;
6. keep compatibility warnings visible while the profile remains not-assessed.

The validation job must not run inside the guest, alter boot image contents, generate kernel headers, or add a kernel dependency.

## Phase 4 — Architecture change governance

For a SAND subsystem change:
1. update SAND's authoritative docs/specification first;
2. update source code and subsystem tests as required;
3. update the DUSRM description/evidence mapping;
4. run the DUSRM schema and semantic validator;
5. review maturity changes against actual CI/test/hardware evidence;
6. record compatibility and reviewer disposition;
7. only then merge the SAND and DUSRM changes in their separate repositories.

## Phase 5 — Future conformance maturity

Only after the OS has sufficiently stable contracts:
- define profile rules for syscall ABI and user-pointer handling;
- define process/address-space authority invariants;
- define device/driver resource ownership and lifecycle constraints;
- define persistent-format compatibility and recovery requirements;
- define package signing/trust and update requirements;
- define service IPC and supervisor contracts;
- create cross-milestone traceability and test-evidence mapping.

No current SAND subsystem is certified by this plan. DUSRM validation is architecture consistency, not a replacement for kernel tests, security analysis, hardware validation or code review.

## Repository safety rule

This document is only a proposal. Do not open a SAND OS pull request, branch, commit or workflow change without separate explicit authorization.
