# DUSRM Profile — Operating System

**Profile ID:** DUSRM-PROFILE-OPERATING-SYSTEM-0.1  
**Profile version:** 0.1-draft  
**Status:** WP6 adoption pilot; non-normative  
**Core target:** DUSRM 1.0-preparation / schema 0.2-draft  
**Compatibility:** not-assessed  
**Reference implementation case:** SAND OS

## 1. Purpose

This profile specializes DUSRM for operating-system architecture descriptions. It is intended to describe the responsibilities and contracts of boot, architecture support, kernel core, memory, scheduling, drivers, storage, system interfaces, services, graphics, applications and toolchains.

The profile does not define an operating-system API, kernel ABI, executable format, driver model, filesystem, syscall number, process scheduler or boot protocol. Those remain owned by each operating-system project.

## 2. Scope

Applicable systems may include:
- boot and platform entry;
- architecture-specific CPU, interrupt, memory and context-switch support;
- kernel core and execution lifecycle;
- memory management and resource allocation;
- scheduler and synchronization;
- process/address-space management;
- device framework and drivers;
- storage, filesystem and persistent formats;
- syscall ABI, user-mode runtime and process interfaces;
- native services, IPC and shell;
- graphics, compositor, windowing and input;
- application execution, package management and developer SDK;
- build, test and release infrastructure when included in the selected system-of-interest.

The profile must distinguish external platform dependencies and development tools from the operating-system runtime.

## 3. Boundary guidance

Typical external participants include:
- CPU and machine platform;
- firmware (BIOS/UEFI);
- physical memory and devices;
- host build toolchain;
- emulator and test harness;
- external developer workstation;
- applications and services outside the selected SOI.

QEMU or another emulator is a test environment, not part of the OS runtime unless the operating system is specifically an emulator-host platform.

## 4. Layer mapping rule

DUSRM's eight layers classify responsibilities. An operating-system project's own implementation strata, subsystem graph and module decomposition may have any number of entries.

**Do not force one-to-one correspondence.** A single OS subsystem may realize responsibilities in several DUSRM layers, and a DUSRM responsibility may span multiple OS modules.

The SAND OS pilot maps nine SAND architecture strata to the eight DUSRM responsibility layers in [the WP6 architecture map](../../specification/DUSRM-1.0/M6-SAND-OS-ARCHITECTURE-MAP.md).

## 5. Profile requirements

An OS description should model, where applicable:
- boot stages and platform assumptions;
- CPU architecture and privilege levels;
- interrupt and exception model;
- physical and virtual memory responsibilities;
- scheduler and execution-context lifecycle;
- process/address-space boundaries;
- kernel/user ABI and syscall contracts;
- driver and device-resource ownership;
- block I/O, filesystems and persistence formats;
- service boundaries, IPC and supervision;
- graphics/input interfaces and user-facing services;
- executable/package formats and loader behavior;
- security boundaries, trust, signing, updates and recovery;
- test/verification evidence, platform scope and known limitations.

Absence of a subsystem may be recorded as planned, external, optional or not applicable with rationale.

## 6. Machine-checkable OS coverage

The schema 0.2 OS profile extension defines a required domain catalogue. Each domain is represented exactly once in `subsystemCoverage` and is declared as `internal`, `externalDependency` or `notApplicable`.

The current catalogue includes:
- boot/firmware and processor architecture;
- kernel core, memory management and execution/scheduling;
- process isolation and device drivers;
- storage/filesystems and kernel interfaces;
- user runtime and native services/IPC;
- graphics/input and application packaging;
- networking, security/trust and build verification.

Every internal domain must reference at least one declared OS element. Every applicable domain must reference evidence. A not-applicable domain must include a rationale. Element/evidence identifiers must resolve.

The profile maps implementation strata to DUSRM's core layers. All eight DUSRM layers must appear in the union of the mapping. This is a coverage check, not a one-to-one structure requirement.

### Evidence and maturity rules

The machine-checkable evidence levels are `planned`, `documented`, `sourceInspected`, `testInSimulation`, `testOnHardware`, `independentlyReviewed` and `verified`.

- `testInSimulation` requires linked test/simulation evidence with simulation context.
- `testOnHardware` requires linked physical/field test, measurement or observation evidence.
- `independentlyReviewed` requires a linked review record.
- `verified` requires linked supporting test, formal, measurement or observation evidence.
- A domain marked `implemented` cannot reference elements that are only planned or in progress.
- Planned and in-progress domains must not be promoted to verified merely because documentation exists.

The validator enforces these checks for the operating-system profile. It does not infer implementation or hardware maturity from names, documentation wording or a CI badge.

## 7. Maturity and evidence

Keep at least these distinctions:
- designed/documented;
- planned;
- implemented;
- tested in an emulator or simulation;
- tested on physical hardware;
- independently reviewed;
- verified against a stated property or requirement.

Do not promote emulator success to physical hardware support. Do not treat a header, API declaration, design note or roadmap item as proof of a stable runtime contract.

## 8. SAND OS pilot

The DUSRM-side fixture is [sand-os-operating-system.json](../../schema/fixtures/0.2/profiles/sand-os-operating-system.json). It models the current documented SAND OS architecture and evidence without changing the SAND OS repository.

See:
- [WP6 adoption plan](../../specification/DUSRM-1.0/M6-SAND-OS-ADOPTION.md)
- [Architecture mapping](../../specification/DUSRM-1.0/M6-SAND-OS-ARCHITECTURE-MAP.md)
- [Review findings](../../specification/DUSRM-1.0/M6-REVIEW-FINDINGS.md)
- [Implementation plan](../../specification/DUSRM-1.0/M6-IMPLEMENTATION-PLAN.md)

## 9. Compatibility status

This profile remains `not-assessed`. Passing a schema fixture or a DUSRM semantic validator is not proof that this profile is complete, compatible with all of DUSRM 1.0, or satisfied by a real OS implementation.
