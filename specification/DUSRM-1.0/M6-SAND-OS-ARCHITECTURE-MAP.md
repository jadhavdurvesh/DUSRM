# DUSRM 1.0 Preparation — SAND OS Architecture Mapping

**Reference:** SAND OS repository tree `661cdedd38e2e24e202dee22798047fd7311353a`  
**Mapping type:** descriptive, many-to-many responsibility mapping

## 1. DUSRM layers versus SAND implementation strata

| SAND stratum | SAND architecture area | DUSRM responsibility layers (candidate mapping) | Mapping rationale |
|---:|---|---|---|
| 1 | Boot and platform entry | L1, L3 | Platform context and controlled boot execution |
| 2 | CPU, interrupts, paging and context switch | L1, L2, L3, L5 | Hardware interaction, resource mapping, execution and address-translation decisions |
| 3 | Kernel core | L2, L3, L4, L5, L6 | Resources, lifecycle, state, kernel decisions and interfaces |
| 4 | Device framework and drivers | L1, L2, L3, L6, L7 | Physical device boundary, resource ownership, driver execution, interfaces and device capabilities |
| 5 | Storage and native filesystem | L2, L4, L7 | Storage capacity, persistent information/state and file capabilities |
| 6 | Syscall ABI and user-mode runtime | L3, L4, L6, L7 | Process execution, state, privileged interface and runtime capabilities |
| 7 | Native services and shell | L4, L5, L6, L7, L8 | Service state/processing/interactions/capabilities and user/system outcomes |
| 8 | Graphics, windowing and input | L1, L3, L4, L6, L7 | Display/input hardware, event handling, UI state, interface contracts and graphics capabilities |
| 9 | Applications, packages and SDK | L3, L4, L5, L6, L7, L8 | Application lifecycle, data, computation, APIs, product capability and user outcome |

## 2. Interpretation rules

- SAND's nine strata are its implementation organization; DUSRM's eight layers are responsibility categories.
- A single SAND module can realize multiple DUSRM responsibilities.
- One DUSRM layer can be realized by several SAND modules.
- The mapping does not establish execution sequence, dependency order, privilege level or source-code layout.
- The mapping must not force SAND modules to be renamed or rearranged.
- Layer applicability describes whether a responsibility is in the selected SOI, external or not applicable; it does not require an implementation module for each layer.

## 3. Subsystem mapping examples

| SAND element | Candidate DUSRM responsibilities | Notes |
|---|---|---|
| Boot chain | L1 platform entry, L3 boot sequencing | BIOS and target hardware remain external participants |
| Memory manager | L2 resource management, L4 memory state, L5 address translation | Bounded prototype; not a production VM model |
| Scheduler/synchronization | L2 thread/stack limits, L3 scheduling, L4 thread state, L5 runnable selection | Uniprocessor prototype; not SMP-safe |
| Process manager | L2 process slots/memory, L3 lifecycle, L4 process/address-space state, L7 process capability | Current implementation is not a complete user-process scheduler |
| Veyra/syscall gateway | L6 privileged interface, L3 dispatch, L7 developer/system capabilities | Do not claim stable general-purpose ABI or IPC |
| Block/ATA/SANDFS | L1 device boundary, L2 device/sector resources, L4 persistent filesystem state, L7 storage capability | SANDFS is a limited prototype without journaling/crash consistency |
| Graphics/windowing | L1 display/input dependencies, L3 event behavior, L4 window/focus state, L6 UI interfaces, L7 graphics capability | Current stack is not a complete compositor |
| SAPP SDK/loader | L4 package format, L5 validation/transformation, L6 developer interface, L7 application-loading capability | Signing and trust-store support remain incomplete |

## 4. Important separation: design model versus runtime

DUSRM is used to describe:
- what responsibilities exist;
- which elements realize them;
- what interfaces/constraints govern them;
- what evidence supports maturity claims;
- what remains planned or unverified.

SAND Veyra continues to define actual SAND-owned interface descriptors and ABI conventions. SAPP continues to define the executable container. SANDFS continues to define filesystem semantics. DUSRM must not duplicate or supersede these technical contracts.
