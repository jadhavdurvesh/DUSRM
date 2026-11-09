# DUSRM 0.5 — Consistency Review

**Status:** Initial editorial and conceptual review; non-normative  
**Date:** 2026-11-09

## 1. Changes introduced

DUSRM 0.5 adds:
- a compact formal metamodel;
- responsibility-based layer allocation;
- structural and semantic well-formedness conditions;
- invariant and proof-obligation templates;
- traceability and staged conformance foundations.

## 2. Consistency findings

### Finding C-01 — Element-to-layer mapping

**Previous ambiguity:** DUSRM 0.3 described layers as responsibility groupings but left room for a reader to treat each component as belonging to one layer.

**Resolution:** DUSRM 0.5 assigns a primary layer to each core responsibility and uses a many-to-many `realizes` relation between elements and responsibilities.

**Impact:** A single engine, board, service, or robot subsystem may realize responsibilities across several layers without duplicating the element.

### Finding C-02 — Operation versus execution

**Previous ambiguity:** Operation definitions and actual execution occurrences could be confused.

**Resolution:** DUSRM 0.4 semantics are retained and made explicit in the formal metamodel. Executions reference operation specifications.

### Finding C-03 — Model versus subject

**Previous ambiguity:** System, architecture, and written description could be treated as the same thing.

**Resolution:** The formal metamodel preserves the distinction between DUSRM reference-model concepts, the SOI, the description, and supporting evidence.

### Finding C-04 — Structural relationships versus behavior

**Previous ambiguity:** A structural link or layer arrow might be read as a mandatory execution sequence.

**Resolution:** Layer assignment classifies responsibility. Operational behavior is represented separately through operations, configurations, and transitions. Cross-layer dependencies require typed relations.

### Finding C-05 — Verification and evidence status

**Previous ambiguity:** A stated or planned property might be interpreted as implemented or proven.

**Resolution:** Claims have explicit status and evidence. Implemented, tested, and verified are distinct.

## 3. Remaining conceptual gaps

- The ontology still needs a reviewed type system and relationship signatures.
- The formal kernel does not yet specify a full temporal logic or concurrency calculus.
- The eight-layer structure has not undergone sufficient independent validation.
- The formal model has not been machine-checked.
- ANANTA and FireBot mappings remain exploratory and need repository/specification audits.
- Conformance levels require detailed applicability and evidence rules.
- No complete literature review or novelty assessment has been completed.

## 4. Review result

DUSRM 0.5 improves internal precision and resolves several ambiguities, but it is not a complete formal standard. This review is an editorial consistency pass, not external peer review, formal proof, or implementation conformance assessment.

## 5. Next milestone recommendation

**DUSRM 0.6 — Validation and Reference Profiles**

- Build fully evidenced system descriptions for a small application, ANANTA, and FireBot.
- Test allocation rules against components with cross-layer responsibilities.
- Test invariants and transition models against at least one appropriate formal tool or manual proof.
- Define domain profile rules for software engines and cyber-physical robotics.
- Record model gaps and revise the core only when evidence justifies it.
