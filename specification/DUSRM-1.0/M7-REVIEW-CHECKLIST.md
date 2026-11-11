# WP7 Independent Review Checklist — DUSRM Core and SAND OS Pilot

This checklist is intended for reviewers who did not author the DUSRM model, schema, validator or SAND OS profile.

## A. Reference-model identity and scope

- [ ] Is DUSRM clearly a reference model rather than a runtime, API, protocol, OS or modeling language?
- [ ] Are its eight layers defined by responsibilities rather than implementation modules or execution order?
- [ ] Are cross-layer responsibilities and many-to-many realizations represented without contradiction?
- [ ] Does the model provide useful domain-neutral concepts without overfitting to SAND, ANANTA or FireBot?
- [ ] Are terms, relationships and extension points unambiguous enough for independent use?

## B. Ontology and relationship semantics

- [ ] Are system-of-interest and system-description distinct?
- [ ] Are element, responsibility, realization, interface, operation, execution, event, state, requirement, constraint, resource, capability, service, decision and evidence semantics coherent?
- [ ] Are relationship endpoint signatures well-founded and sufficiently complete?
- [ ] Are unsupported or profile-specific relationships clearly distinguished from core relationships?
- [ ] Are relationship direction, cardinality, temporal applicability and scope adequately defined?

## C. Schema and semantic validator

- [ ] Is schema 0.2 structurally complete for the intended 1.0 scope?
- [ ] Does the validator resolve all typed references required by the schema?
- [ ] Are global identifiers, relationship endpoints, allocation, state transitions, interfaces and evidence references checked consistently?
- [ ] Are errors, warnings, assumptions and not-assessed outcomes distinguished accurately?
- [ ] Are validator omissions and known false-positive/false-negative risks documented?
- [ ] Can an independent user reproduce the CI result from the repository and pinned dependency?

## D. SAND OS operating-system profile

- [ ] Is the mapping from nine SAND implementation strata to eight DUSRM responsibility layers valid and non-prescriptive?
- [ ] Are boot/firmware, CPU privilege, memory, scheduler, process lifecycle, storage, ABI, graphics, application loader and toolchain boundaries represented?
- [ ] Are current capabilities separated from planned or unverified capabilities?
- [ ] Are QEMU results scoped to emulator evidence rather than physical hardware proof?
- [ ] Are Veyra, SAPP and SANDFS preserved as SAND-owned contracts instead of duplicated by DUSRM?
- [ ] Are the README milestone, thread-capacity and SAPP-version documentation questions resolved or kept explicitly open?

## E. Practical adoption

- [ ] Is the portable kit self-contained and integrity-pinned?
- [ ] Does host-side validation remain separate from kernel/runtime and guest image generation?
- [ ] Is the CI failure policy appropriate for errors versus compatibility warnings?
- [ ] Is the DUSRM update process clear and reproducible?
- [ ] Is the owner of the architecture description and its evidence identified?

## F. Review disposition

Record one of:
- `accepted` — no blocking or major concerns within the reviewed scope;
- `accepted-with-findings` — usable subject to listed changes;
- `revision-required` — major issues must be corrected before adoption;
- `not-assessable` — insufficient evidence or scope clarity.

A review disposition does not itself approve a domain profile as compatible. Profile compatibility must be updated separately in the registry with rationale and supporting review evidence.
