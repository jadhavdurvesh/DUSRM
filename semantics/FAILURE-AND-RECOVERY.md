# DUSRM 0.4 — Failure, Degradation, and Recovery Semantics

**Document ID:** DUSRM-SEM-005  
**Status:** Working draft; non-normative  
**Version:** 0.4-draft

## 1. Purpose

This document defines a vocabulary for describing faults, errors, failures, degraded operation, and recovery across the DUSRM layers.

DUSRM does not prescribe a universal fault-tolerance architecture. It requires descriptions to state what can go wrong, how the condition is detected or observed, what effects are possible, and what recovery claims are supported.

## 2. Distinguish fault, error, and failure

For the purposes of this draft:

- **Fault:** a cause or hypothesized cause of an incorrect condition.
- **Error:** an incorrect internal state or value that may lead to a failure.
- **Failure:** a deviation from a required or expected service or behavior at a declared boundary.

The relationship may be causal but is not always directly observable. A failure may occur without its cause being known; a fault may exist without producing an error or externally visible failure.

Descriptions must distinguish observed facts from inferred causes.

## 3. Failure observation

A failure description should record:
- affected system, element, operation, or interface;
- expected behavior or requirement;
- observed deviation;
- detection method and time;
- scope and duration;
- affected users, systems, or resources;
- confidence and evidence;
- known or suspected cause;
- current operational status.

## 4. Failure classes

The following are useful descriptive categories. They are not a complete universal taxonomy:

| Class | Description | Example category |
|---|---|---|
| Omission | Expected action or output does not occur | Missing response |
| Timing | Action occurs too early, too late, or outside a timing bound | Deadline miss |
| Value/data | Output or state is incorrect or corrupted | Invalid measurement |
| Crash/stop | Participant halts or becomes unavailable | Process termination |
| Communication | Communication is lost, delayed, duplicated, or reordered | Network partition |
| Resource | Required resource is exhausted or unavailable | Power or memory exhaustion |
| Interface/contract | Interaction violates an agreed contract | Invalid response |
| Physical/environmental | Physical conditions prevent intended behavior | Overtemperature |
| Security/trust | Unauthorized or untrusted behavior affects the system | Compromised credential |
| Partial/system-of-systems | Some participants fail while others continue | One robot unavailable |

A fault may belong to more than one class. Classification should not hide the underlying evidence.

## 5. Fault detection and diagnosis

DUSRM distinguishes:
- **Detection:** recognizing that a condition may be abnormal.
- **Diagnosis:** determining or narrowing down its cause.
- **Isolation:** limiting the affected scope or preventing propagation.
- **Containment:** restricting the consequences.
- **Mitigation:** reducing impact while the condition persists.

A detection signal is not proof of root cause. Diagnostic confidence and unknowns should be recorded.

## 6. Degraded operation

A degraded mode is a declared operating condition in which some capabilities, quality levels, or guarantees are reduced while selected responsibilities remain available.

A degraded-mode description should include:
- entry conditions;
- retained capabilities;
- unavailable or reduced capabilities;
- additional constraints;
- operator notification or authority requirements;
- exit and recovery conditions;
- safety implications.

Do not call a mode safe merely because it is labeled degraded or fail-safe. Safety must be supported by hazard analysis and verification.

## 7. Recovery

Recovery is a set of activities intended to restore an acceptable system condition after a fault, error, or failure.

Possible recovery categories include:
- retry;
- restart or reinitialize;
- restore from a known checkpoint;
- reconcile divergent states;
- switch to redundant capacity;
- isolate and replace a component;
- compensate for a completed but undesirable effect;
- enter a controlled degraded mode;
- require operator intervention.

The description must state which effects are preserved, undone, repeated, or left uncertain.

## 8. Recovery semantics

A recovery specification should define:
- triggering conditions;
- preconditions and required authority;
- affected state and resources;
- recovery actions and their order or dependencies;
- retry limits and timing, if applicable;
- idempotency or duplicate-effect handling;
- success criteria;
- failure of recovery behavior;
- evidence and operator notification.

Recovery must not be assumed to mean rollback. Physical effects may be irreversible; distributed actions may have partially completed; an external system may have processed a request even if its acknowledgment was lost.

## 9. Fault containment and independence

A claimed independent recovery or safety path should identify:
- shared power, compute, communication, sensors, clocks, and control dependencies;
- common-cause failure possibilities;
- authority and override paths;
- assumptions about isolation;
- evidence that independence is achieved at the required level.

Separate software modules are not automatically independent safety mechanisms.

## 10. Layer mapping

Failure can originate in or affect any layer:
- L1: physical damage, power loss, environmental limits;
- L2: resource exhaustion or allocation failure;
- L3: stalled, uncontrolled, or terminated execution;
- L4: corrupt, stale, inconsistent, or unavailable state;
- L5: incorrect or incomplete computation;
- L6: interaction failure, message loss, or coordination error;
- L7: capability unavailable or below declared quality;
- L8: mission/application outcome not achieved.

These examples are illustrative. A failure may span multiple layers and should be linked through causal and impact relationships.

## 11. Safety and assurance boundary

DUSRM can organize fault, hazard, control, evidence, and recovery descriptions. It is not a safety standard, hazard-analysis method, certification scheme, or substitute for domain-specific functional-safety requirements.

For safety-critical systems, hazard analysis must determine appropriate controls and independent verification. A reference-model mapping alone is insufficient.

## 12. Open questions

- Should DUSRM separate fault models from operational failure models?
- How should partial completion and uncertain external effects be represented?
- How should recovery success be evidenced?
- How should common-cause and cascading failure be represented?
- Which failure categories belong in the universal model versus domain profiles?
