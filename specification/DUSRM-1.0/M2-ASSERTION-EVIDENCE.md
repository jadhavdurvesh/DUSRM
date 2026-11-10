# DUSRM 1.0 Preparation — Assertion, Applicability, Realization, and Evidence Model

**Work package:** WP2 — Foundational Ontology and Relationship Consolidation  
**Status:** Proposed status and evidence model; non-normative  
**Target:** DUSRM 1.0

## 1. Problem

The 0.7 description schema uses one status enumeration for multiple questions. Its values include design disposition, implementation maturity, epistemic state, evidence method/outcome, and applicability. These dimensions are not interchangeable.

For example:
- implemented does not mean tested;
- tested does not necessarily mean passed;
- simulated describes the context in which behavior was exercised, not whether a production realization exists;
- observed describes how a claim was obtained, not necessarily whether the behavior is acceptable;
- notApplicable is an applicability decision, not an implementation status;
- rejected is a decision disposition, not an evidence result.

## 2. Proposed orthogonal status dimensions

### 2.1 Design disposition

Describes the lifecycle of a design or architecture decision:
- proposed;
- accepted;
- rejected;
- superseded.

A disposition applies to a decision or design assertion. It must not be used to describe implementation maturity.

### 2.2 Realization state

Describes how far a modeled responsibility, element, operation, or capability has been realized:
- notStarted;
- planned;
- inProgress;
- implemented;
- retired;
- unknown.

A project may add profile-specific values with explicit definitions. Simulated is not a realization state by itself. A simulation can be implemented as software while the physical realization remains planned.

### 2.3 Applicability

Describes whether a concept is relevant to the declared system scope:
- internal;
- externalDependency;
- notApplicable;
- notModeled;
- unknown.

These values must not be confused with realization state. A layer can be an external dependency even if its provider is fully implemented. A planned internal responsibility is still applicable.

### 2.4 Assessment result

Describes the outcome of an assessment against stated criteria:
- notAssessed;
- pass;
- passWithFindings;
- fail;
- inconclusive.

An assessment record must identify its criterion, method, scope, assessor or tool, date/revision, evidence, and limitations.

### 2.5 Evidence method and context

The way evidence was produced is recorded as method/context, not as a maturity status. Examples include:
- source inspection;
- design review;
- static analysis;
- unit/integration/system test;
- measurement;
- operational observation;
- simulation;
- model checking;
- mathematical proof;
- inspection of an independently produced artifact.

The context should identify whether the evidence concerns a paper design, simulation, laboratory setup, hardware-in-the-loop setup, deployed software, or physical operation.

## 3. Assertion model

A material assertion should identify:
- assertion identifier and exact statement;
- subject and scope;
- assertion category: design, implementation, behavior, requirement, assumption, or assessment claim;
- design disposition, where the assertion is a design decision;
- realization state, where implementation is applicable;
- assessment result, where an assessment has been performed;
- assumptions and known exclusions;
- evidence references;
- validity period or version, where claims can become stale.

Not every assertion needs every dimension. A design decision may have a disposition but no realization state. A measurement claim may have an assessment result without being a design decision.

## 4. Evidence record

An evidence record should identify:
- stable evidence identifier;
- evidence artifact kind;
- source URI or repository/path/reference;
- immutable revision or configuration identifier where available;
- evidence-producing method;
- subject and scope of the evidence;
- collection or execution context;
- date/time and clock basis where relevant;
- result or evidential relation to the assertion (supports, contradicts, qualifies, or inconclusive);
- limitations, sampling bounds, and uncertainty;
- producing actor, tool, or reviewer where relevant.

Source documents and source code are provenance evidence. They can establish what is specified or present in a repository; they do not alone prove runtime behavior, physical effects, safety, or conformance.

## 5. Evidence rules

- A claim may have supporting and contradicting evidence at the same time.
- Evidence must be evaluated for subject, version, scope, recency, method, and independence.
- A test result must name what was tested and under which configuration.
- A simulation result must remain explicitly scoped to the simulation model and assumptions.
- A model-checking result applies to the formal model and configuration that were checked.
- A measurement must identify the measured property, unit, instrument or method, and uncertainty where material.
- A repository document must not be presented as evidence that a physical device is connected or operational unless the document is backed by an appropriate observation.
- An accepted design does not prove implementation.
- An implemented feature does not prove that a requirement is satisfied.
- A test pass does not establish verification unless the criterion and scope are adequate for the claim.
- Conflicting evidence must be recorded rather than hidden by promoting a single status.

## 6. Verification and satisfaction

A claim may be marked assessed as pass only when:
1. the criterion is explicit;
2. the assessment method is recorded;
3. the evidence references resolve;
4. the evidence pertains to the claimed subject, version, and scope;
5. limitations and assumptions are stated;
6. the assessment authority is identified.

A requirement satisfaction relationship is an assertion to be assessed, not proof in itself. The existence of a design element or a traceability link is not sufficient evidence of satisfaction.

## 7. Migration from the legacy status vocabulary

| Legacy 0.x value | Proposed 1.0 treatment |
|---|---|
| proposed | designDisposition = proposed, where it describes a decision; otherwise assertion category/record lifecycle |
| specified | retain as a specification-state or document artifact property, not general evidence strength |
| planned | realizationState = planned |
| implemented | realizationState = implemented; separate assessment remains notAssessed until performed |
| simulated | evidence context = simulation; simulated implementation may also have its own realization state |
| observed | evidence method = observation; assessment result is separately recorded |
| tested | evidence method = test; pass/fail/inconclusive is separately recorded |
| verified | assessment result = pass only when criterion, method, evidence, scope and assessor are recorded; otherwise not established |
| assumed | explicit assumption record with rationale, scope, and impact |
| unknown | applicability or assessment completeness = unknown, depending on the question |
| rejected | designDisposition = rejected or assessment result = fail, depending on meaning |
| notApplicable | applicability = notApplicable |

The mapping is intentionally contextual. A migration tool must not mechanically convert a legacy value without inspecting the record it describes.

## 8. Status

This orthogonal model is proposed for DUSRM 1.0. The 0.1 schema and 0.9 validator retain their legacy status enum until a separately versioned schema and migration design are reviewed.
