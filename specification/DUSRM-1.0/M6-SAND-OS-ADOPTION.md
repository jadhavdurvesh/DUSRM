# DUSRM 1.0 Preparation — WP6 SAND OS Adoption Plan

**Work package:** WP6 — Independent Review Findings and Release Candidate Gate  
**Adoption pilot:** DUSRM profile for operating systems, using SAND OS as a reference case  
**Status:** DUSRM-side architecture pilot prepared; SAND OS implementation not modified  
**Date:** 2026-11-11

## 1. Objective

Make DUSRM usable as an architecture-description and validation framework for SAND OS while preserving SAND OS's own interfaces, source ownership and runtime independence.

The target is **adoption of DUSRM as a design-time model and CI validation input**, not integration of DUSRM into the bootloader, kernel, driver code, SAPP runtime or operating-system image.

## 2. Repository boundary

Target inspected read-only:
- Repository: `jadhavdurvesh/sand-os`
- Branch: `main`
- Tree snapshot: `661cdedd38e2e24e202dee22798047fd7311353a`
- Files inspected: README, architecture, roadmap, integration guide, API catalogue, security policy, Veyra ABI foundation, SAPP format/SDK, selected public headers, filesystem source and native boot CI workflow.

**No SAND OS files, branches, commits, workflows or releases were created, modified or deleted during this WP6 work.** All new files are in DUSRM only.

## 3. Why an operating-system profile is needed

The existing standalone application profile is too narrow to describe kernel privilege, process/address-space isolation, drivers, storage, boot, ABI, filesystem and native application formats. DUSRM needs an OS-specific profile that adds vocabulary and evidence rules without changing core layer semantics or prescribing a kernel implementation.

The profile is [DUSRM-PROFILE-OPERATING-SYSTEM-0.1](../../profiles/operating-system/PROFILE.md). Its DUSRM 0.2 pilot fixture is [sand-os-operating-system.json](../../schema/fixtures/0.2/profiles/sand-os-operating-system.json).

## 4. Adoption model

SAND can consume DUSRM through three design-time artifacts:

1. **Architecture description:** a versioned DUSRM JSON description representing the selected SAND OS system-of-interest, elements, responsibilities, interfaces, requirements, constraints, evidence and maturity.
2. **Traceability:** links from DUSRM records to SAND-owned architecture documents, ABI specifications, source locations and CI evidence.
3. **CI validation:** a host-side Python step validates the DUSRM description against the pinned DUSRM schema and semantic validator. It runs before or beside SAND OS's existing build/QEMU workflow and does not alter the guest image.

DUSRM must not become a required build-time or runtime dependency of SAND OS. SAND must still boot if DUSRM's repository, validator, JSON file or documentation is unavailable.

## 5. Architecture mapping

SAND documents nine implementation strata:
1. boot and platform entry;
2. architecture-specific CPU, interrupt, paging and context-switch code;
3. kernel core;
4. device framework and hardware drivers;
5. storage and native filesystem;
6. syscall ABI and user-mode runtime;
7. native services and shell;
8. graphics, windowing and input;
9. applications, package management and SDK.

DUSRM has eight responsibility layers. The mapping is intentionally many-to-many; see [M6-SAND-OS-ARCHITECTURE-MAP.md](M6-SAND-OS-ARCHITECTURE-MAP.md).

The model describes how SAND's modules realize responsibilities; it does not require SAND's architecture strata to be renamed, reordered or merged.

## 6. Current SAND OS capabilities captured

The model captures:
- SAND-authored legacy BIOS boot sector and second-stage loader;
- 32-bit x86 kernel and architecture support;
- E820 memory discovery, bounded frame allocation, non-PAE paging and early heap;
- uniprocessor kernel-thread scheduler and synchronization prototype;
- bounded process table and distinct address spaces;
- limited ring-3/syscall proof of concept and Veyra descriptor foundation;
- block-device registration and primary-master ATA PIO;
- SANDFS v1 prototype;
- framebuffer and early windowing;
- SAPP container, SDK and packer.

It marks networking, full service IPC/supervision and the complete compositor as planned.

## 7. What the current CI evidence means

The inspected SAND OS Native Boot CI run [#42876341368](https://github.com/jadhavdurvesh/sand-os/actions/runs/42876341368) completed successfully on the inspected SAND OS main tree. Its workflow:
- runs `make clean` and `make check`;
- runs the SAPP unit tests;
- compiles and executes the Veyra ABI descriptor host test;
- builds the raw boot image;
- boots it in QEMU and asserts named kernel self-test markers including process/address-space, syscall, storage/SANDFS and graphics markers.

This establishes that the specified build and QEMU test job passed at that revision. It does not prove physical hardware compatibility, production security, complete OS functionality, general ABI stability or safety.

## 8. Integration boundary with SAND-owned technologies

DUSRM does not replace:
- **Veyra** — SAND's ABI/interface contract architecture;
- **SAPP** — SAND's native executable container and SDK;
- **SANDFS** — SAND's filesystem format/prototype;
- **SAND's block, graphics, scheduler or process interfaces**.

DUSRM describes and checks the responsibilities, boundaries, evidence and relationships of those elements. Technical details remain authoritative in SAND's own specifications and code.

Third-party technology projects such as ANANTA, NOCTIS, EREBUS, CONTRACT, OCTET, DATAGRAM and CALLGRAPH remain separately specified. DUSRM does not require them to be present in the kernel.

## 9. Standards relationship

DUSRM should complement architecture-description and systems-engineering practices, not replace them:
- ISO/IEC/IEEE 42010:2022 addresses structure and expression of architecture descriptions.
- ISO/IEC/IEEE 15288:2023 provides system life-cycle process descriptions.
- OMG SysML v2 is a formal systems modeling language and API/interchange ecosystem.

See [M6-STANDARDS-CROSSWALK.md](M6-STANDARDS-CROSSWALK.md).

## 10. Adoption gates

Before any SAND OS repository implementation:
- obtain explicit owner approval for a DUSRM reference file and CI step;
- decide where the DUSRM model will live (DUSRM-only canonical copy, or a later reviewed SAND-side copy);
- resolve the source-status conflicts documented in M6 review findings;
- pin the DUSRM schema/validator revision and record its license/dependency requirements;
- prove the validation step is host-only and does not affect image generation or boot;
- define update policy and failure behavior if DUSRM validation is unavailable;
- keep DUSRM as a non-runtime dependency;
- review security-sensitive claims independently.

No changes to SAND OS are authorized by this adoption plan. A separate explicit implementation authorization is required before modifying that repository.

