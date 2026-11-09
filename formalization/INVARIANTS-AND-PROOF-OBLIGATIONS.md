# DUSRM 0.5 — Invariants and Proof Obligations

**Document ID:** DUSRM-FRM-003  
**Status:** Formalization draft; non-normative

## 1. Purpose

This document provides a common way to state system invariants and record the reasoning or evidence used to support them.

DUSRM does not provide a theorem prover or guarantee that an invariant is true. It defines the proof obligation that a description should expose.

## 2. Configuration predicates

Let:
- `C` be the set of modeled configurations;
- `C₀ ⊆ C` be the set of initial configurations;
- `Next(c,c')` mean that the model permits a step from configuration `c` to configuration `c'`;
- `I(c)` be an invariant predicate over a configuration.

A configuration is reachable if it is an initial configuration or can be reached from an initial configuration by a finite sequence of permitted transitions.

Write `Reach(C₀, Next)` for the set of reachable configurations.

An invariant claim is:

`∀ c ∈ Reach(C₀, Next) : I(c)`

This claim is always relative to the model, abstraction, scope, and assumptions.

## 3. Inductive proof obligation

A common sufficient proof strategy is:

**INV-INIT — Initialization**
`∀ c ∈ C₀ : I(c)`

**INV-STEP — Preservation**
`∀ c,c' ∈ C : (I(c) ∧ Next(c,c')) ⇒ I(c')`

If both obligations hold, then I is preserved over every finite behavior starting in C₀, provided the transition relation and assumptions are correctly defined.

An invariant may be true of all reachable states but fail the simple inductive step because the predicate is too weak to prove locally. In that case, a stronger inductive invariant may be needed. Failure of this proof attempt is not automatically a counterexample to the original invariant.

## 4. Assumptions

Every proof obligation must list assumptions, such as:
- initial-state restrictions;
- environment conditions;
- sensor or input validity conditions;
- resource availability;
- execution or scheduling guarantees;
- communication assumptions;
- authority and policy conditions.

A proof under assumptions does not prove the system when those assumptions are false.

## 5. Safety properties

A safety property excludes an undesirable state or transition. A safety claim should identify:
- the forbidden condition or behavior;
- the scope and system boundary;
- relevant initial conditions;
- transition assumptions;
- the invariant or temporal property used;
- the evidence or proof result.

Illustrative form:

`∀ c ∈ Reach(C₀, Next) : ¬Unsafe(c)`

This is a logical form only. The predicate `Unsafe` must be precisely defined by the domain analysis.

## 6. Progress and liveness properties

A liveness property states that something desirable eventually occurs in a behavior. It requires explicit progress assumptions, such as fairness, availability, or environmental response.

A common informal form is:
- whenever a request is admitted, it eventually reaches a terminal outcome, under the declared progress assumptions.

The model must not claim liveness from an invariant proof alone.

A system that can remain forever in a permitted waiting state may be safe but fail to make progress.

## 7. Constraint categories

DUSRM recommends distinguishing:
- **Structural constraint:** restricts elements, relationships, or decomposition.
- **State constraint:** restricts allowed configurations.
- **Transition constraint:** restricts allowed state changes.
- **Resource constraint:** limits capacity or allocation.
- **Temporal constraint:** limits timing or ordering.
- **Authority constraint:** limits who or what may initiate an action.
- **Environmental assumption:** declares conditions outside the system boundary.
- **Safety/security constraint:** states a risk control or protection obligation.

A constraint is not automatically an invariant. Its scope and enforcement semantics must be stated.

## 8. Proof-obligation record

Each invariant or formal claim should include:

| Field | Required information |
|---|---|
| Claim ID | Stable identifier |
| Statement | Exact predicate or property |
| Type | Invariant, safety, liveness, refinement, consistency, or other declared type |
| Subject/scope | System and abstraction level |
| Assumptions | Preconditions and environment assumptions |
| Model version | DUSRM and system-model version |
| Method | Mathematical proof, model checking, test, analysis, inspection, or other |
| Result | Proven under assumptions, counterexample found, tested, inconclusive, not assessed |
| Evidence | Proof artifact, tool report, test result, analysis record |
| Reviewer | Responsible reviewer or authority |
| Limitations | Known exclusions and uncertainty |

Do not mark a statement "proven" merely because it is written in mathematical notation.

## 9. Refinement obligation

If a concrete model is claimed to refine an abstract model, the description must identify:
- abstract model;
- concrete model;
- mapping between concrete and abstract configurations;
- which abstract behaviors must be preserved;
- whether concrete internal steps may be hidden or treated as stuttering;
- properties preserved by the mapping;
- assumptions and proof evidence.

DUSRM does not yet prescribe one universal refinement relation.

## 10. Worked generic invariant

Suppose a system has a Boolean state variable `authorized` and an action `performProtectedAction`.

Candidate invariant:

`I(c) ≜ performedProtectedAction(c) ⇒ authorizationWasValidAtExecution(c)`

To assess it, the model must define:
- what counts as an action being performed;
- what authorization means;
- how time-of-check and time-of-use are handled;
- whether authorization can be revoked during execution;
- how the action and authorization evidence are recorded.

Without these definitions, the notation is underspecified and the invariant is not ready for proof.

## 11. Limits

DUSRM invariants do not replace hazard analysis, threat modeling, functional safety analysis, security verification, testing, or certification. Proofs apply only to the formal model and its assumptions.
