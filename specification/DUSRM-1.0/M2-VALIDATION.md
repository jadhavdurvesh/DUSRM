# DUSRM 1.0 Preparation — WP2 Ontology and Relationship Validation

**Work package:** WP2 — Foundational Ontology and Relationship Consolidation  
**Status:** Internal consistency review; non-normative  
**Date:** 2026-11-10

## 1. Review method

This is a documentation-level consistency review of:
- DUSRM 0.2 Core Ontology and relationship catalogue;
- DUSRM 0.5 Formal Metamodel and allocation rules;
- DUSRM 0.9 relationship signature rules, JSON schema, and semantic validator;
- DUSRM 1.0 WP1 Layer Charter;
- the proposed WP2 ontology, relationship matrix, and evidence model.

No new source-project implementation tests, physical tests, or external peer review were performed.

## 2. Cross-document consistency findings

| ID | Question | Result | Required control |
|---|---|---|---|
| WP2-V01 | Is the SOI distinct from its description? | Consistent in the 0.2 and 0.5 foundation; retained | Keep subject, description, and evidence levels explicit |
| WP2-V02 | Are components assigned directly to one layer? | No; responsibility allocation is the intended model | Keep one primary layer per Responsibility and many-to-many Element realization |
| WP2-V03 | Are responsibility, requirement, operation, and capability distinct? | Earlier documents define them separately but some examples and generic records can blur them | Adopt the consolidated definitions and explicit typed references |
| WP2-V04 | Is Realization unambiguous? | No; it describes element-to-responsibility allocation and is also used as a general relationship name | Reserve Realization for allocation; use implements for implementation-to-specification |
| WP2-V05 | Are all relationship endpoint kinds machine-checkable? | No; only broad participant kinds are available in schema 0.1 and ten provisional signatures are checked | Keep unsupported signatures as warnings until typed references exist |
| WP2-V06 | Can a multi-party allocation/interchange be represented faithfully as one binary edge? | Not always | Reify shared relationships with named roles |
| WP2-V07 | Are status values orthogonal? | No; the legacy enum mixes design, implementation, evidence, and applicability | Adopt separate status dimensions in a future schema |
| WP2-V08 | Can source code or specification text prove an operational claim? | No, not alone | Separate provenance from test, observation, measurement, analysis, and formal evidence |
| WP2-V09 | Are profile compatibility claims supported? | No; all current profile entries are not-assessed against a 0.7-draft candidate core | Retain not-assessed until a dedicated compatibility review |

## 3. Layer charter compatibility

The proposed ontology preserves the WP1 allocation model:
- only Responsibilities receive a primary core layer;
- an Element may realize Responsibilities in more than one layer;
- a Capability, Operation, Interface, Resource, or Evidence item does not receive a layer simply because it exists;
- an Environment Participant is not an internal realization;
- cross-cutting concerns attach to named model objects and assertions;
- no layer order implies a relationship.

No contradiction with the WP1 layer definitions was identified in this documentation review.

## 4. Representative domain sanity checks

### 4.1 ANANTA

- Database engine remains an Element/subject, not a layer.
- Query Operation is a behavior specification; a query Execution is a particular run.
- AQL parsing/planning/evaluation are computational responsibilities, distinct from execution progression.
- Data schemas and durable artifacts are information/state concepts.
- Embedded API contract is an Interface; the database's query/ingestion abilities are Capabilities.
- Host OS and filesystem may be Environment Participants when outside the SOI boundary.
- WAL or repository documentation is evidence about a specification or implementation claim, not automatic proof of runtime durability.

### 4.2 FireBot

- Physical chassis, sensors, motors, batteries, and compute boards are Elements with physical kinds/roles.
- Detection, localization, or route-planning algorithms are Operations or computational responsibilities; individual runs are Executions.
- A detection event is distinct from a persistent detection record or mission state.
- An operator/robot command contract is an Interface; a transport or message format is separately specified.
- A battery is a physical Element and may also participate in a Resource model; the available energy budget and its allocation are distinct.
- Emergency-stop policy/authority is a constraint and control relationship; a software stop flag is not proof of a physical stop.
- Simulation evidence remains scoped to the simulation.

### 4.3 Standalone application

- The host OS/device can remain an external dependency.
- A UI event/interface contract can exist without a network.
- Task data/state, task operations, execution occurrences, and user-visible capabilities remain distinct.
- The application purpose and user outcome are not the same as the task-management capability.

These checks are model-level consistency tests, not implementation verification.

## 5. Validation outcome

**Documentation result: internally consistent with explicit tooling gaps.**

The consolidated conceptual model aligns with the WP1 responsibility-layer charter and the earlier ontology/metamodel intent. The largest remaining gap is implementation: schema 0.1 and validator 0.9 do not represent or check the full typed ontology.

The correct next implementation step is a separately versioned schema and migration proposal with fixtures, not an unreviewed expansion of the current schema.

## 6. Open review questions

- Is the proposed category/kind/role distinction sufficient for systems-of-systems and organizational architectures?
- Should State be represented as explicit state objects, variable valuations, or both with a declared relation?
- What minimum participant role metadata is required for n-ary interactions and allocations?
- Which relationship signatures should be mandatory in the first 1.0 schema?
- How should evidence independence, freshness, and contradiction be assessed?
- Which ontology terms should remain core and which should be profile extensions?
