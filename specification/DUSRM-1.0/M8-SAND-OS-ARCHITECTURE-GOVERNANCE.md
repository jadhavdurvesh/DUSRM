# DUSRM 1.0 Preparation — SAND OS Architecture Governance

**Purpose:** establish DUSRM as SAND OS's primary project-level architecture reference  
**Status:** adoption policy proposal; SAND OS repository unchanged  
**Target:** SAND OS main architecture and future subsystem development

## 1. Adoption decision proposed

SAND OS should use DUSRM as its **primary system-wide architecture reference model** for:
- classifying responsibilities across the complete OS;
- mapping subsystems, elements and their realizations;
- expressing dependencies, relationships and interface boundaries;
- tracking operations, state, resource allocation and lifecycle;
- tracing requirements, constraints, decisions and evidence;
- recording implementation maturity and architecture gaps.

This is intended to replace informal or inconsistent project-wide layer diagrams as the authoritative responsibility map.

DUSRM does not replace every domain-specific architecture, standard or technical contract. It is not a processor architecture, instruction set, memory model, syscall ABI, driver API, filesystem format, executable format or network protocol. SAND-owned specifications remain authoritative for those concrete contracts.

## 2. What "instead of the usual models" means

DUSRM becomes the top-level reference for how SAND OS is organized and how responsibilities cross subsystem boundaries. It does not forbid using specialized models when they are the right tool for a specific domain.

| Concern | Governing description |
|---|---|
| Whole-system responsibility architecture | DUSRM operating-system profile |
| Eight responsibility layers | DUSRM core |
| CPU instruction set, privilege modes and paging details | x86 architecture manuals and SAND architecture-specific specifications |
| Kernel/user calling convention and syscall contract | SAND Veyra and syscall specifications |
| Executable container and loader contract | SAPP format specification |
| Persistent storage layout and filesystem semantics | SANDFS specification |
| Network protocol layering when networking exists | Appropriate network architecture/protocol specifications |
| Actual runtime behavior | SAND source code, tests, emulator and hardware evidence |

The eight DUSRM layers are **not** a replacement for the OSI network protocol stack. They classify responsibilities across the whole system. Networking will become one domain within the DUSRM description when SAND's network subsystem is implemented.

## 3. Normative project rule proposed for SAND

Every architecture-affecting SAND change should have an associated DUSRM description update whenever it changes:
- a subsystem's responsibility or ownership;
- a boundary, dependency or interface;
- a resource limit or allocation policy;
- an operation, state transition or lifecycle rule;
- a requirement, constraint, invariant or security boundary;
- a capability's maturity or supporting evidence.

Pure code refactors that do not change architecture need not alter the DUSRM model; reviewers should record that judgement in the change description where the impact is non-obvious.

## 4. DUSRM-first architecture change workflow

1. **Propose:** identify the affected system, responsibility, layer, element, relationship and affected requirements.
2. **Model:** update the DUSRM system description and profile coverage before or alongside implementation.
3. **Validate:** run structural schema validation and semantic/profile rules. Missing references, missing required OS domains, unsupported layers and maturity contradictions must fail.
4. **Specify:** update the relevant SAND technical contract (Veyra, SAPP, SANDFS, driver, scheduler or other subsystem specification) where behavior changes.
5. **Implement:** change source code independently of the model; DUSRM is not generated into the kernel.
6. **Test:** run host tests, kernel self-tests, QEMU and hardware tests as appropriate to the claim.
7. **Record evidence:** update DUSRM evidence links and maturity only to the level demonstrated by the tests.
8. **Review:** have an owner/reviewer approve the model and implementation changes together.

## 5. CI policy

The DUSRM validation job should be host-side and separately identifiable.

- Schema and semantic errors: fail the architecture-validation job.
- Missing required domain coverage: fail.
- Dangling element/evidence references: fail.
- Unsupported layer mappings: fail.
- Implemented maturity inconsistent with element maturity: fail.
- QEMU evidence mislabeled as hardware evidence: fail.
- Profile compatibility warning: retain until independently assessed; it is not silently ignored or promoted.
- DUSRM service unavailable: no runtime impact. SAND should keep its normal build/boot path independent.

The first executable implementation of this policy is the portable kit in `adoption/sand-os/`.

## 6. Ownership and source of truth

- DUSRM owns the core reference model, profile vocabulary, schemas and validator rules.
- SAND OS owns its implementation, authoritative technical specifications and test evidence.
- The DUSRM description owns the cross-subsystem responsibility/relationship view and links to SAND evidence.
- A DUSRM model must not silently override a technical SAND spec. A disagreement is recorded as an architecture/specification finding and resolved through SAND's change-control process.
- A profile compatibility state changes only through an explicit assessment decision.

## 7. SAND adoption gate

Before the policy becomes mandatory in SAND:
- the SAND OS owner reviews the DUSRM layer charter and this governance policy;
- the architecture description is accepted as an accurate current baseline;
- DUSRM schema/validator version is pinned;
- a separate host-side CI job is added and verified;
- a model ownership/update policy is recorded;
- the initial profile compatibility state receives an explicit disposition.

This proposal does not make any changes to `jadhavdurvesh/sand-os`. Its adoption there still requires separate authorization.

## 8. Limits

DUSRM checks architecture-description consistency and traceability. It does not prove:
- kernel code correctness;
- CPU/driver correctness;
- concurrency or memory safety;
- filesystem durability;
- security isolation;
- physical hardware compatibility;
- real-time behavior or operational safety.

Those claims require separate technical specifications, tests, analysis and evidence.
