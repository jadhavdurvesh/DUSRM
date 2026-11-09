# DUSRM 0.8 — Semantic Validation and Formal-Methods Integration

**Status:** Research draft; non-normative  
**Milestone:** M7 — Semantic Validation and Formal-Methods Pilot  
**Release label:** 0.8-draft  
**Date:** 2026-11-09

## Objective

Extend DUSRM beyond structural JSON validation by implementing selected semantic consistency checks and demonstrating a traceable formal-methods workflow for a small operational behavior.

## Included

- Semantic validator for identifiers, realization links, relationships, operation owners, state subjects, transition domains, evidence references, profile registry compatibility, and extension namespaces.
- Unit tests for positive, negative, and edge-case semantic behavior.
- CLI for validating an individual DUSRM JSON description.
- TLA+ task-completion pilot with explicit DUSRM mapping and assumptions.
- CI workflow for schema checks, semantic tests, CLI negative tests, and TLC model checking.
- Recorded validation output and explicit limits.

## Validation result

The 0.8 workflow [run #1](https://github.com/jadhavdurvesh/DUSRM/actions/runs/42653412176) passed on 2026-11-09:
- JSON Schema fixture checks passed.
- 9 semantic unit tests passed.
- Two positive CLI descriptions were accepted with no findings.
- Duplicate-ID and dangling-realization CLI fixtures were rejected.
- TLC model checking completed with 4 states generated, 2 distinct states, and no error found.

See [0.8 validation results](../../validation/0.8-VALIDATION-RESULTS.md).

## What semantic validation means here

A semantic pass means that the enabled, machine-checkable rules found no errors in the supplied description and registry. It does not mean that the system is correct, safe, implemented, or fully DUSRM-conformant. Warnings are reported separately.

## What formal verification means here

TLC checks a finite manually authored TLA+ model against its invariants and temporal property. The mapping is deliberately narrow. No automatic translator from free-text DUSRM descriptions exists.

## Known limitations

- The semantic validator covers a selected subset of the 0.7 check catalogue.
- Relationship type participant signatures remain incomplete.
- Profile registry entries remain `not-assessed`; profile-bearing descriptions are rejected until compatibility is explicitly reviewed.
- Evidence checks enforce references and basic support for verified claims; evidence quality still requires human review.
- Natural-language guards and effects are not parsed into executable logic.
- The TLA+ model assumes stable authorization and atomic completion; it omits revocation, failure, multi-user concurrency, persistence, and physical effects.
- The eight-layer model remains provisional.

## Next work

- Expand semantic validation from the check catalogue with additional fixture coverage.
- Review profile compatibility for the standalone profile first.
- Add state/relationship type signatures.
- Model concurrency, cancellation, and recovery in separate formal examples.
- Obtain independent formal-methods and systems-engineering review before considering a stable specification.
