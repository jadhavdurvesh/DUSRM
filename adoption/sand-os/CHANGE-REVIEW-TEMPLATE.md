# SAND OS Architecture Change Review — DUSRM

Use this template for proposed SAND OS changes that may affect architecture. It is an engineering review aid, not a replacement for the normal code review or test plan.

## 1. Change identity

- Change / PR:
- SAND OS base commit:
- Author:
- Reviewers:
- Date:
- Subsystem owner:
- Change category: new subsystem / boundary change / interface change / resource policy / state lifecycle / security constraint / documentation-only / pure refactor

## 2. DUSRM impact

- DUSRM description revision:
- DUSRM validator/schema revision:
- Profile ID/version:
- Validation report artifact:

### Affected layers

- [ ] L1 — platform and environment responsibilities
- [ ] L2 — resource responsibilities
- [ ] L3 — execution and lifecycle responsibilities
- [ ] L4 — state and information responsibilities
- [ ] L5 — computation and transformation responsibilities
- [ ] L6 — interaction and interface responsibilities
- [ ] L7 — capability and service responsibilities
- [ ] L8 — system-purpose and outcome responsibilities

Explain why each selected layer is affected. Layer numbers do not imply module order or execution order.

### Affected DUSRM records

- Elements:
- Responsibilities:
- Realizations:
- Relationships:
- Operations / executions / events:
- States / transitions:
- Interfaces / interactions:
- Resources / allocations:
- Capabilities / services:
- Requirements / constraints / invariants:
- Decisions / assertions / evidence:

## 3. OS profile domain coverage

- Required OS domain(s) affected:
- Current applicability and maturity:
- Proposed applicability and maturity:
- Realizing elements:
- Evidence records:
- Does this change add a required OS domain? If yes, explain the profile update and tests.
- Does it change the many-to-many mapping from SAND strata to DUSRM layers?

## 4. Technical contract impact

Identify the SAND-owned specification affected:
- Veyra / syscall / user-mode interface:
- SAPP / loader / packaging:
- SANDFS / block storage:
- CPU / memory / scheduler / process:
- Device / driver:
- Graphics / input:
- Service / IPC / networking:
- Security / trust / updates:
- Other:

DUSRM must link to these contracts, not silently redefine them.

## 5. Evidence and maturity

- [ ] Schema validation passed.
- [ ] DUSRM semantic/profile validation passed.
- [ ] Host-side unit tests passed.
- [ ] Kernel self-tests passed.
- [ ] QEMU/emulator tests passed.
- [ ] Physical hardware tests passed (only when actually run).
- [ ] Independent review completed (only when actually performed).
- [ ] DUSRM evidence references updated and limitations retained.

Never label QEMU tests as physical hardware verification. Never mark an element implemented or verified solely because documentation or a planned roadmap item exists.

## 6. Integration boundary

- [ ] DUSRM remains host-side/design-time only.
- [ ] SAND still builds and boots without DUSRM availability.
- [ ] No DUSRM code is linked into the kernel or SAPP runtime.
- [ ] No SAND-owned ABI, executable format or filesystem contract is duplicated by DUSRM.
- [ ] Update pin and report digest are recorded.

## 7. Review decision

- [ ] Accept
- [ ] Accept with findings
- [ ] Changes requested
- [ ] No DUSRM architecture impact (rationale required)

Findings, owners and closure evidence:

## 8. Merge gate

The DUSRM description and SAND technical contract should agree on the responsibility and boundary being changed. Any disagreement must be resolved explicitly; do not choose one silently. Compatibility state changes require a separately recorded assessment decision.
