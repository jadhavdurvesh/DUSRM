# DUSRM 0.9 — Core Relationship Participant Signatures

**Status:** Provisional semantic rule catalogue; non-normative

## 1. Purpose

The semantic validator can check participant kinds only where DUSRM has defined a sufficiently clear core signature. This document records the subset implemented in 0.9.

A relationship signature constrains which participant categories may occupy the source and target positions. It does not, by itself, specify execution order, transitivity, symmetry, ownership, or control authority.

## 2. Participant categories

- **Element:** an element declared in the DUSRM description.
- **Environment:** an external participant declared in the system context.
- **System:** the declared system of interest.

## 3. Provisional core signatures

| Relationship type | Permitted source | Permitted target | Intended meaning |
|---|---|---|---|
| decomposesInto | Element | Element | Source element is decomposed into target element |
| memberOf | Element | Element, System | Source element is a member of a larger element/system |
| containedWithin | Element | Element, System | Source element is contained within target boundary/element |
| dependsOn | Element | Element, Environment, System | Source element depends on target participant |
| interactsWith | Element, Environment, System | Element, Environment, System | Participants interact across a declared boundary |
| observes | Element | Element, Environment | Source element observes target participant |
| controls | Element | Element | Source element controls target element |
| allocates | Element | Element | Source element allocates a declared resource/responsibility represented by target element |
| requires | Element | Element, Environment, System | Source element requires target participant or service |
| exposes | Element | Element, Environment | Source element exposes an interface/capability to target participant |

The semantic validator reports an unsupported relationship signature as warning `DUSRM-M-016`. If a supported signature is violated, it reports error `DUSRM-M-006`.

## 4. Types not yet assigned a core signature

The current description schema includes other relationship types such as:
- performs;
- triggers;
- transitionsTo;
- constrainedBy;
- satisfies;
- realizes;
- derivedFrom.

These remain schema-valid but semantically underspecified at the core level. The validator emits warning `DUSRM-M-016` rather than guessing participant kinds.

Some of these relations may ultimately require typed references to operations, events, states, requirements, constraints, or responsibilities instead of element-only endpoints. Their signatures must be defined alongside those metamodel types.

## 5. Semantics not implied

A participant signature does not imply:
- relationship transitivity or symmetry;
- a mandatory execution sequence;
- a protocol or API call;
- a control-authority hierarchy;
- safety approval;
- that an asserted relationship is implemented or verified.

Those properties require separate definitions, scope and evidence.

## 6. Compatibility

These signatures are draft rules for DUSRM 0.9. A future revision may refine them or introduce typed participant references. Such changes must be versioned and validated against existing descriptions and domain profiles.
