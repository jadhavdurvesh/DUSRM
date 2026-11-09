# DUSRM 0.4 — Abstract Transition-System Kernel

**Document ID:** DUSRM-SEM-002  
**Status:** Formalization proposal; non-normative  
**Version:** 0.4-draft

## 1. Purpose and limitation

This document gives DUSRM a compact mathematical vocabulary for discussing behavior. It is a minimal abstract kernel, not a complete formal semantics, executable language, model checker, or replacement for TLA+, temporal logic, automata theory, Petri nets, process algebras, or established modeling notations.

Its primary purpose is to ensure that descriptions of operations, states, events, and transitions have an unambiguous conceptual basis.

## 2. Abstract model

A basic transition-system description may be represented as:

`M = (C, A, →, C₀)`

where:
- `C` is a set of modeled system configurations;
- `A` is a set of step labels or action descriptions;
- `→` is a transition relation, a subset of `C × A × C`;
- `C₀` is a set of admissible initial configurations, a subset of `C`.

A transition `c --a--> c'` means that action `a` is permitted by the model to relate configuration `c` to configuration `c'`.

This relation describes permitted behavior. It does not, by itself, say which permitted behavior must occur or when.

## 3. Behaviors and traces

A finite behavior trace is a sequence:

`c₀, a₁, c₁, a₂, c₂, ..., aₙ, cₙ`

such that:
- `c₀ ∈ C₀`;
- for each step `i`, `cᵢ₋₁ --aᵢ--> cᵢ`.

An infinite behavior trace is defined analogously with an unbounded sequence of steps.

A trace is valid only relative to the selected model, its declared scope, and its assumptions. A valid model trace is not automatically evidence that a physical implementation produced the trace.

## 4. State and configuration

A configuration represents all facts selected as relevant at the chosen abstraction. It may include:
- state properties;
- execution statuses;
- pending or observed events;
- resource claims and allocations;
- authority and constraints;
- environment facts and uncertainty.

A configuration is not required to represent every microscopic physical detail. It is an abstraction chosen to answer a stated engineering question.

## 5. Nondeterminism

If several destination configurations are permitted for a given configuration and action, the model is nondeterministic.

Nondeterminism may represent:
- genuine variability;
- concurrency or scheduling choices;
- uncertain environment behavior;
- unspecified implementation choices;
- abstraction of details not relevant to the current view.

Descriptions must not interpret nondeterminism as randomness unless a probability model is explicitly defined.

## 6. Initial conditions and invariants

An initial condition defines which configurations are allowed as starting points for the described behavior.

An invariant `I` is a predicate over configurations that is claimed to hold in every reachable configuration under the model's assumptions.

A basic inductive proof obligation is:
1. Every allowed initial configuration satisfies `I`.
2. For every permitted transition from a configuration satisfying `I`, the destination also satisfies `I`.

This is a proof pattern, not a claim that all DUSRM invariants are automatically inductive or that a particular tool has checked them.

## 7. Safety and liveness

A safety claim states that no forbidden configuration or transition occurs in any behavior covered by the specification.

A liveness claim states that a desired condition is eventually reached, under explicit progress assumptions.

The transition relation alone does not establish liveness. Scheduling, fairness, availability, environmental assumptions, and resource guarantees may be required.

## 8. Time extension

A time-aware model may annotate configurations, events, or transitions with time values or intervals. The basic transition-system tuple above is not itself a real-time semantics.

A timed extension must declare:
- clock domains;
- timestamp meaning;
- clock resolution and uncertainty;
- whether time is discrete, dense, or interval-valued;
- deadline and timeout interpretation;
- rules for simultaneous or unordered events.

Do not compare timestamps from different clock domains as if they were perfectly synchronized.

## 9. Concurrency extension

A concurrent model may represent several independently progressing execution occurrences in one configuration.

A global interleaving model may serialize modeled steps for analysis even where the physical system is concurrent. If interleaving is an abstraction, say so. It does not mean the implementation has a single thread or total global event order.

For distributed descriptions, causal ordering should be distinguished from timestamp ordering.

## 10. Refinement and abstraction

A more detailed model may refine a more abstract model if its behaviors and observations satisfy the abstraction relation defined between them.

DUSRM does not yet define a universal refinement calculus. A refinement claim must identify:
- abstract and concrete models;
- mapping or abstraction relation;
- preserved properties;
- allowed nondeterminism or behavior reduction;
- assumptions and evidence.

## 11. Notation conventions

The following are informal mathematical conventions used in DUSRM documentation:

- `x ∈ S`: x is an element of set S.
- `R ⊆ A × B`: R is a relation between A and B.
- `c --a--> c'`: a labeled transition from c to c'.
- `P(c)`: predicate P holds for configuration c.
- `∀`: for every.
- `∃`: there exists.
- `⇒`: implies.
- `∧`: and.
- `∨`: or.
- `¬`: not.

No parser, compiler, canonical serialization, or machine validation is implied by these conventions.

## 12. Relationship to formal methods

The basic transition-system model is intentionally compatible in spirit with established state-based formal methods. TLA+ uses an initial condition and next-state relation to describe possible behaviors; temporal formulas can then express properties over those behaviors.

DUSRM borrows no claim of novelty from this mathematical structure. Its research question is how a common cross-domain reference ontology and layered responsibility model can organize these semantics while remaining independent of the chosen formal verification technique.

Reference: https://lamport.azurewebsites.net/tla/high-level-view.html
