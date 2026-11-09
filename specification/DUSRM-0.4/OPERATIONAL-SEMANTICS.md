# DUSRM 0.4 — Operational Semantics

**Document ID:** DUSRM-SEM-001  
**Status:** Working draft; non-normative  
**Version:** 0.4-draft  
**Date:** 2026-11-09

## 1. Purpose

This document defines the first operational vocabulary for describing how a system behaves over time. It connects the DUSRM 0.2 ontology to the candidate hybrid structure in DUSRM 0.3.

DUSRM operational semantics describe the externally relevant and internally modeled behavior of a system of interest (SOI). They do not prescribe a programming language, runtime, API, protocol, scheduler, database transaction model, control algorithm, or implementation architecture.

The rules here are a proposed semantic foundation. They are not yet a complete formal semantics or conformance standard.

## 2. Semantic separation

A system description must distinguish:

1. **Operation specification:** what behavior is defined or offered.
2. **Execution occurrence:** a particular attempt or instance of carrying out an operation.
3. **Event occurrence:** something that happens and is relevant to the system.
4. **State:** a modeled condition of a subject at a time or interval.
5. **Transition:** a modeled change between states.
6. **Observation:** information obtained about a subject; it may be delayed, uncertain, incomplete, or incorrect.
7. **Effect:** a change or externally visible consequence attributable to behavior.

A definition does not prove that an execution occurred. An event record does not prove that the represented event was correctly observed. A requested effect does not prove that the effect occurred.

## 3. Operation specification

An operation specification describes a behavior a subject may perform or offer.

A complete operation description should identify, where applicable:

| Field | Meaning |
|---|---|
| Identity | Stable identifier and version of the operation definition |
| Owner | Subject or component responsible for offering or performing it |
| Purpose | Intended result or responsibility |
| Preconditions | Conditions required before it may be admitted or begun |
| Inputs | Values, events, resources, or references required |
| Authority | Required permission or control authority, if applicable |
| Resource requirements | Capacity or resources needed, reserved, or consumed |
| Effects | Possible changes or externally visible consequences |
| Postconditions | Conditions expected after successful completion |
| Failure conditions | Declared ways the operation may fail or be unable to proceed |
| Timing constraints | Deadlines, durations, periods, freshness, or other temporal constraints |
| Interruption behavior | Whether and how it may be paused, cancelled, or interrupted |
| Repeatability | Whether repeated invocation is allowed and whether effects are idempotent, cumulative, or otherwise constrained |
| Evidence | Tests, analysis, measurements, or assumptions supporting the definition |

Not every operation needs every field. An omitted field means unspecified, not automatically unrestricted.

## 4. Execution occurrence

An execution occurrence is a particular instance of behavior associated with an operation specification.

It should have a unique identity within its declared scope and record, where applicable:
- operation identity and version;
- initiating subject or event;
- execution context;
- input references;
- admission decision;
- resource and authority conditions;
- observed lifecycle status;
- start, suspension, resumption, and end times;
- outputs and effects;
- outcome and failure information;
- evidence and provenance.

Different execution occurrences of the same operation may have different inputs, contexts, durations, effects, and outcomes.

## 5. Abstract execution lifecycle

DUSRM proposes the following lifecycle vocabulary. It is an abstract vocabulary, not a mandatory finite-state machine for every implementation.

| State | Meaning |
|---|---|
| Created | An execution occurrence has been identified or requested |
| Admitted | The system has accepted it for possible execution under declared admission rules |
| Ready | It is eligible to begin but has not started |
| Active | Its behavior is currently progressing |
| Suspended | Progress is temporarily stopped while the occurrence remains resumable |
| Terminated | It will perform no further steps as the same execution occurrence |

A terminated execution must additionally record an outcome, where known:
- **Succeeded:** declared success conditions are satisfied and supported by evidence appropriate to the description.
- **Failed:** execution ended without satisfying its declared success conditions.
- **Cancelled:** execution was intentionally ended before success.
- **Timed out / expired:** a declared temporal condition was exceeded or expired.
- **Rejected:** the request was not admitted; this is normally a request disposition rather than a started execution.
- **Unknown:** the outcome cannot be determined from available evidence.

Profiles may add states or distinguish more detailed outcomes. They must define their meanings and mappings to this abstract vocabulary.

A system may omit explicit Created, Admitted, or Ready states if those distinctions are not observable or useful in its scope. It must not claim that a skipped state occurred unless evidence supports it.

## 6. Operation enabling and admission

A proposed abstract enabling predicate is:

`Enabled(o,c) = Preconditions(o,c) ∧ ConstraintsPermit(o,c) ∧ AuthoritySatisfied(o,c) ∧ AdmissionRulesSatisfied(o,c)`

where:
- `o` is an operation specification;
- `c` is the current modeled configuration;
- `Preconditions` checks declared preconditions;
- `ConstraintsPermit` checks relevant constraints and invariants;
- `AuthoritySatisfied` checks required authority where applicable;
- `AdmissionRulesSatisfied` checks the declared admission policy.

Resource availability is included only to the extent that the operation's admission or execution contract requires it. Some resources may be reserved at admission, acquired when execution starts, acquired incrementally, or not modeled.

If the predicate is false, the operation is not enabled under that configuration. A system may reject, defer, queue, or leave the request pending according to its separately declared policy. DUSRM does not prescribe one universal response.

## 7. Effects and completion

Operation effects must be described with their timing and commitment semantics.

Possible effect categories include:
- immediate and indivisible at the selected abstraction;
- incremental or visible during execution;
- deferred until a declared commit point;
- compensatable by a later operation;
- externally initiated and only partially observable;
- eventual, subject to declared progress assumptions.

An operation's successful termination must not be inferred merely because its execution stopped. Its postconditions and success evidence must be considered.

DUSRM does not assume all operations are atomic, reversible, idempotent, or transactional. Such properties must be declared for each operation or domain profile.

## 8. Configuration and transition model

A **configuration** is a modeled snapshot of the system at the level of detail selected by a description. It may include:
- values of relevant state properties;
- active execution occurrences;
- pending events;
- resource allocations;
- active constraints and authority conditions;
- relevant environment observations.

A transition relates a source configuration to a permitted destination configuration under a declared step or event.

For an informal operational model:

`c --a--> c'`

means that, under the description's assumptions, action or step `a` may take the system from configuration `c` to configuration `c'`.

A model may permit more than one destination configuration from the same source. This represents nondeterminism or underspecified behavior; it must not be silently replaced with a single deterministic outcome.

The selected granularity matters. A step may represent a processor instruction, a database operation, a robot maneuver, or a high-level mission transition. Descriptions must state the chosen abstraction.

## 9. State transition contract

A transition description should identify:
- subject and state variables or properties affected;
- source condition;
- triggering or enabling event, if any;
- guard condition;
- action or effect;
- destination condition;
- timing assumptions;
- constraints and invariants;
- failure, interruption, or cancellation behavior;
- evidence status.

A transition is permitted only when its declared guards and constraints hold. Whether it must eventually occur is a separate progress or liveness claim.

## 10. Safety and progress properties

DUSRM separates two broad kinds of behavioral claim.

**Safety property:** something prohibited never happens within the stated scope and assumptions. Example form: "an actuator command is never issued while the independent safety interlock reports an unsafe condition."

**Progress property:** something desirable eventually happens, subject to explicit assumptions. Example form: "an admitted request eventually reaches a terminal outcome if required resources remain available and the responsible execution service continues to make progress."

A model that describes only allowed transitions may establish safety properties but may not establish that a system makes progress. Progress claims require assumptions about fairness, scheduling, communication, resources, or environmental behavior.

Do not state an unconditional "eventually" guarantee when the required assumptions are absent.

## 11. Layer relationship

Operational semantics apply across all DUSRM layers. An operation may:
- consume or reserve resources described at L2;
- be activated, scheduled, or controlled at L3;
- observe or change state represented at L4;
- perform a transformation at L5;
- interact with other elements through L6;
- realize a capability described at L7;
- contribute to an outcome described at L8;
- depend on physical conditions and infrastructure at L1.

This is a traceability pattern, not a mandatory execution pipeline. Operations may cross layers directly, and feedback or control loops may return to lower layers.

## 12. Status and evidence rules

Every important behavioral claim should be marked as one of:
- planned;
- specified;
- implemented;
- observed;
- tested;
- verified;
- assumed;
- unknown.

These labels are not interchangeable. "Implemented" does not mean "verified"; "tested" does not mean every relevant behavior has been proven; "specified" does not mean implemented.

The method and evidence must accompany a verification claim.

## 13. Relationship to established formal methods

DUSRM uses familiar ideas from transition systems, state machines, and temporal reasoning. It does not attempt to replace established formalisms.

TLA+ describes systems using an initial condition and a next-state relation, with temporal properties used to reason about behavior over sequences of states. This is a useful reference for DUSRM's state/transition vocabulary, particularly for concurrency and distributed systems.

UML state machines and SysML state-machine concepts provide established approaches to modeling states, transitions, events, guards, and actions. DUSRM should map to existing tools when useful rather than inventing a complete modeling language.

Sources:
- Leslie Lamport, "A High-Level View of TLA+": https://lamport.azurewebsites.net/tla/high-level-view.html
- OMG, UML specification: https://www.omg.org/spec/UML
- OMG, SysML specification: https://www.omg.org/spec/SysML
- OMG specifications catalog, including Precise Semantics of UML State Machines: https://www.omg.org/spec

## 14. Open questions

- Should execution lifecycle states be normative or remain profile-defined?
- How should an execution's partial effects be represented?
- How should an operation be modeled when it spans several systems?
- How should uncertainty in postconditions be represented?
- What constitutes sufficient evidence for a successful outcome?
- How should compensation, rollback, and recovery be distinguished?
- Which formalism best expresses DUSRM's core without making it a new modeling language?

## 15. Status

This is an operational-semantics working draft. It establishes vocabulary and candidate rules but does not yet define complete mathematical semantics, an executable notation, or conformance tests.
