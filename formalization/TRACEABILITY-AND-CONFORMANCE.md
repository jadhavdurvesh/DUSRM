# DUSRM 0.5 — Traceability and Conformance Foundations

**Document ID:** DUSRM-FRM-004  
**Status:** Research draft; non-normative

## 1. Purpose

This document defines a traceability structure connecting needs and claims to DUSRM architecture, behavior, and evidence. It also proposes staged assessment levels for DUSRM descriptions.

## 2. Traceability chain

A useful traceability chain is:

`Stakeholder Need → Requirement → Responsibility → Layer → Element → Operation/Transition → Verification Criterion → Evidence`

This is a navigation pattern, not a mandatory one-to-one chain:
- one requirement may map to several responsibilities;
- one responsibility may be realized by several elements;
- one element may realize responsibilities in several layers;
- one operation may support multiple requirements;
- one verification activity may provide evidence for several claims.

Every link must have a declared meaning. Do not infer satisfaction merely from the existence of a traceability path.

## 3. Required traceability links

A system description should support these relationships where applicable:

| From | To | Meaning |
|---|---|---|
| Stakeholder need | Requirement | Derivation or interpretation |
| Requirement | Responsibility | Responsibility allocated to address the requirement |
| Responsibility | Layer | Primary reference layer |
| Element | Responsibility | Realization |
| Element | Interface | Interface exposure or requirement |
| Operation | Execution occurrence | Specification instantiated by an occurrence |
| Operation | State/transition | Behavior reads or changes modeled state |
| Constraint/invariant | Element/operation/transition | Scope of the constraint |
| Requirement | Verification criterion | Condition used to assess satisfaction |
| Criterion | Evidence | Test, analysis, inspection, measurement, or proof result |
| Claim | Evidence | Support, refutation, or qualification |

## 4. Claim status

A traceability or evidence record should distinguish:

- **Proposed:** suggested but not yet accepted as a design statement.
- **Specified:** included in an approved system specification, but not necessarily implemented.
- **Implemented:** exists in the implementation.
- **Observed:** seen in a stated operational context.
- **Tested:** evaluated using a recorded test method.
- **Verified:** assessed against a declared criterion with adequate evidence.
- **Assumed:** accepted temporarily without sufficient evidence.
- **Unknown:** information is unavailable.
- **Rejected:** considered and explicitly not accepted.

Projects may define additional states with clear meanings. Status must not be promoted without evidence.

## 5. Conformance scope

DUSRM conformance applies to a **system description**, not directly to the real system, unless an assessment explicitly includes implementation evidence.

A DUSRM description may be assessed at the following draft levels:

### Level A — Vocabulary-compatible

The description uses DUSRM terms consistently and identifies the DUSRM version/profile used.

### Level B — Structurally well-formed

The description declares scope, SOI, boundary, elements, typed relationships, responsibility definitions, layer allocations, and relevant constraints.

### Level C — Behaviorally specified

The description includes applicable operations, executions, states, transitions, events, timing, concurrency, and failure behavior at its declared level of detail.

### Level D — Formally assessed

The description includes defined invariants or properties, assumptions, proof obligations, and recorded assessment results.

### Level E — Implementation-evaluated

The description is traced to a real implementation and includes tests, observations, measurements, inspection, or analysis against declared criteria.

These levels are cumulative in intent, but not every system needs every feature. A profile must state applicability and permitted omissions. No level is a certification or safety approval.

## 6. Assessment outcomes

An assessment may report:
- **Pass:** all applicable checks at the claimed level are satisfied.
- **Pass with findings:** mandatory checks pass, but non-blocking issues or limitations remain.
- **Fail:** one or more mandatory checks are not satisfied.
- **Not assessable:** the description or evidence is insufficient to perform the assessment.

The report must identify version, profile, scope, exclusions, reviewer, method, evidence, and limitations.

## 7. Conformance rules

- Conformance does not require use of any DMJ technology.
- Conformance does not require eight software modules or physical subsystems.
- A description must not claim a level beyond the evidence supplied.
- Profile-specific rules must not contradict core DUSRM definitions.
- A DUSRM assessment does not establish safety, security, regulatory compliance, or fitness for purpose unless those are separately assessed under appropriate criteria.
- An implementation may be useful even when its description is not yet DUSRM-conformant.

## 8. Open questions

- What is the minimum mandatory set for each level?
- How should profile-specific exclusions be represented?
- How should conflicting evidence or stale evidence affect status?
- Who may approve conformance claims?
- Should conformance reports have a machine-readable format?
- How should the framework map to existing architecture-description and systems-modeling tools?
