# DUSRM 0.5 — Formal Notation Refinements

**Status:** Draft; non-normative

This document refines informal notation introduced in DUSRM 0.2 and 0.4. It is a documentation convention, not a grammar, programming language, or machine-readable interchange format.

## 1. Sets and relations

- `x ∈ S`: x belongs to set S.
- `S ⊆ T`: S is a subset of T.
- `R ⊆ A × B`: R is a binary relation from A to B.
- `f : A → B`: f is a total function from A to B.
- `f : A ⇀ B`: f is a partial function from A to B.
- `dom(R)`: domain of a relation or function.
- `ran(R)`: range of a relation.
- `∀x ∈ S`: for every x in S.
- `∃x ∈ S`: there exists an x in S.

## 2. Responsibility allocation

Let:
- `E` be system-description elements;
- `P` be responsibility definitions;
- `L` be the set of core layers;
- `primaryLayer : P → L`;
- `realizes ⊆ E × P`.

The derived layer set for element e is:

`Layers(e) = { primaryLayer(p) | p ∈ P ∧ (e,p) ∈ realizes }`

This permits an element to realize responsibilities in several layers without assigning the entire element to one exclusive layer.

## 3. Typed relationships

A relationship instance can be written:

`r = (id, kind, participants, scope, validity, status, evidence)`

The relation kind determines allowed participant roles and any specific constraints. Do not assume generic relationships are reflexive, symmetric, transitive, or exclusive.

## 4. State and transition system

Let:
- `C` be configurations;
- `A` be action labels;
- `Next ⊆ C × A × C`;
- `C₀ ⊆ C`.

Write:

`c --a--> c'`

when the model permits action a to relate configuration c to configuration c'.

A finite trace is a sequence `c₀, a₁, c₁, …, aₙ, cₙ` where `c₀ ∈ C₀` and every step satisfies Next.

## 5. Invariants

An invariant is a predicate `I : C → Bool` that is claimed to hold over every reachable configuration:

`∀c ∈ Reach(C₀, Next) : I(c)`

An inductive proof strategy requires:
- `∀c ∈ C₀ : I(c)`;
- `∀c,c' ∈ C : I(c) ∧ NextState(c,c') ⇒ I(c')`.

Here `NextState(c,c')` abbreviates the existence of an action label a such that `(c,a,c') ∈ Next`.

## 6. Safety and progress

An illustrative safety claim is:

`∀c ∈ Reach(C₀, Next) : ¬Forbidden(c)`

An illustrative progress claim is:

`For every behavior satisfying declared fairness assumptions, eventually Goal holds.`

Progress claims require explicit assumptions. Do not infer them from the invariant rules.

## 7. Notation status

The notation may be replaced or mapped into established tools such as TLA+, Alloy, SysML v2, or another suitable formalism. DUSRM descriptions must preserve the meaning of the model when mapped; no particular tool is mandatory.
