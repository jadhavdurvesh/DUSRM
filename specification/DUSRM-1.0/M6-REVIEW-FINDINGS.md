# DUSRM 1.0 Preparation — WP6 Desk Review Findings

**Review type:** internal read-only technical desk review  
**Date:** 2026-11-11  
**Target:** DUSRM SAND OS profile and read-only SAND OS repository snapshot  
**Independent reviewer:** none recorded

## 1. Executive summary

SAND OS is a strong domain pilot for DUSRM because its architecture spans boot, kernel execution, memory, process isolation, devices, storage, interfaces, graphics and native applications. The profile can map these areas without changing SAND OS's own architecture.

The review also found source inconsistencies and maturity limits that must remain explicit. No compatibility or production-readiness decision is made.

## 2. Findings

### WP6-F01 — README milestone drift

**Severity:** Major documentation issue  
**Evidence:** README.md blob `6510d8c87567628aaf218df0bb71d570bfdb7b6c`; ARCHITECTURE.md blob `1af2bc56a0837693eb90d806694bca38787513f4`; ROADMAP.md blob `a5e5644e44318d6a55fd6ab0899d6d9c667bec0f`; CI run `42876341368`.

README calls the current status M0 boot-chain bring-up, while the detailed architecture describes M5 process/address-space and M6 storage work, and the CI checks corresponding process, storage and graphics markers. The repository's latest successful workflow is authoritative evidence for what was tested at its SHA, but the project owner should reconcile the README milestone label.

**DUSRM handling:** record maturity by subsystem and evidence rather than one global milestone label.

### WP6-F02 — Scheduler capacity wording mismatch

**Severity:** Major technical documentation question  
**Evidence:** `include/sand/kernel/scheduler.h` blob `2265e29e0c3e3be5027c4c116dc10b689270ef38`; architecture narrative in `docs/ARCHITECTURE.md`.

The scheduler header defines `SAND_SCHEDULER_MAX_THREADS 8u`; the architecture narrative describes four thread descriptors/stacks in the early scheduler prototype. This may reflect code evolution or a stale narrative. The active scheduler table/stack implementation and QEMU evidence must settle the value.

**DUSRM handling:** the profile records the source discrepancy and does not assert a single active limit.

### WP6-F03 — SAPP version-label inconsistency

**Severity:** Major compatibility/documentation question  
**Evidence:** `sdk/sapp/README.md` blob `922efd98361dcd6227f3ccae060ffb6073e588be`; `sdk/sapp/FORMAT.md` blob `2f5f52676a64e026cd24a22401af3c67d406d171`.

The SDK README describes SAPP v0.2 while the binary format document identifies SAPP v0.1 and format version 1. Clarify whether v0.2 refers to SDK/packer release or whether the container specification itself changed. Keep container format version distinct from SDK release version.

**DUSRM handling:** profile treats SAPP container and SDK as distinct concepts; future model should track version scheme explicitly.

### WP6-F04 — Veyra is not a complete syscall ABI or IPC

**Severity:** Blocker for claims of general application compatibility  
**Evidence:** `docs/API_CATALOG.md`, `docs/VEYRA_ABI.md`, `include/sand/veyra/abi.h`.

The docs explicitly state that Veyra has a descriptor/status foundation and syscall proof-of-concept, but no complete general-purpose syscall ABI, service IPC or stable published subsystem function tables. Descriptor presence is not proof that arbitrary user pointers are safe or that kernel services can communicate via general IPC.

**DUSRM handling:** interface maturity is marked in-progress; service IPC is planned.

### WP6-F05 — SANDFS is not a production filesystem

**Severity:** Blocker for user data or reliability claims  
**Evidence:** `docs/ARCHITECTURE.md`, `include/sand/fs/sandfs.h`, `kernel/fs/sandfs.c`.

SANDFS v1 is documented as a limited one-sector-per-file prototype with fixed directory capacity, small file sizes and no journaling, crash consistency, checksums, permissions or concurrent access locking.

**DUSRM handling:** storage capability is marked in-progress and constraints remain explicit.

### WP6-F06 — SAPP signing/trust and complete launch path are missing

**Severity:** Blocker for production package trust claims  
**Evidence:** `sdk/sapp/FORMAT.md`, `sdk/sapp/README.md`.

Unsigned packages are development artifacts. Signing/trust-store verification, filesystem launch, shared libraries and dynamic linking are not implemented in the inspected docs.

**DUSRM handling:** SAPP SDK element is in-progress; unsigned-package constraint recorded.

### WP6-F07 — Security policy explicitly rejects production readiness

**Severity:** Blocker for production/security suitability  
**Evidence:** `docs/SECURITY.md`.

SAND OS is declared experimental and unsuitable for production or safety-critical use; production-grade boundary, verified boot, sandbox, cryptographic updates and security audit are absent.

**DUSRM handling:** this is a hard maturity constraint; do not promote CI success into security verification.

### WP6-F08 — Existing CI is valuable but emulator-scoped

**Severity:** Observation / evidence scope  
**Evidence:** [SAND OS Native Boot CI run #42876341368](https://github.com/jadhavdurvesh/sand-os/actions/runs/42876341368).

The workflow passed build, SDK tests, Veyra host test and QEMU boot/self-test assertions. It is strong repeatable implementation evidence for the tested commit and emulator target, but not physical machine compatibility or general-purpose OS correctness.

**DUSRM handling:** evidence context is simulation/QEMU, with limitations stated.

## 3. Architectural recommendation

Treat DUSRM as a design-time architecture model and CI validator:
- keep source-of-truth specifications in SAND OS;
- keep DUSRM model/evidence mapping in DUSRM initially;
- validate the DUSRM JSON from host-side CI;
- do not import validator code into the kernel;
- do not make boot success depend on external DUSRM services;
- only move a copy of the model into SAND after explicit approval and a pinned update policy.

## 4. Closure status

All findings remain open for the SAND OS project owner. WP6 does not change SAND OS documentation to resolve them. Their existence does not invalidate the successful QEMU run; it constrains the claims that can be made from it.
