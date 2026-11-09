# DUSRM 0.4 — Cross-Layer Operational Rules

**Document ID:** DUSRM-SEM-006  
**Status:** Working draft; non-normative  
**Version:** 0.4-draft

## 1. Purpose

The DUSRM 0.3 candidate architecture defines eight responsibility layers. This document explains how behavior may span these layers without implying that every operation must traverse them in order.

## 2. Core rule

**Layer assignment classifies responsibility; it does not dictate execution order.**

An operation may involve elements or responsibilities in several layers. Every important cross-layer relationship should be represented using the typed relationship graph and linked to the relevant operation, event, state, constraint, or evidence.

## 3. Cross-layer pattern

A generic activity may involve:
1. L8: an application or mission outcome creates a need;
2. L7: a capability is selected or requested;
3. L6: participants interact through declared interfaces;
4. L5: a computation or transformation defines the result;
5. L4: relevant information or state is read or updated;
6. L3: an execution occurrence progresses and is controlled;
7. L2: resources are allocated or consumed;
8. L1: physical or infrastructure conditions enable or constrain realization.

This is a reasoning pattern, not a compulsory sequential pipeline. The actual ordering depends on the system and operation. The pattern may have feedback, concurrent branches, loops, or direct relationships that skip layers.

## 4. Cross-layer contract

Each cross-layer dependency should state:
- source and target elements;
- source and target layer assignments;
- relationship type;
- why the relationship exists;
- required assumptions and constraints;
- information, resource, or control effect;
- timing or ordering requirement, if any;
- failure and recovery behavior;
- evidence and status.

Do not infer that a higher layer owns a lower layer's internal state or that a lower layer can choose mission-level policy unless the authority relationship is explicit.

## 5. Feedback

Feedback is a relationship in which an observation of system behavior or environment influences a later operation or control decision.

A feedback description should identify:
- reference or desired condition;
- measured or observed condition;
- estimation or interpretation process;
- decision or controller;
- actuator or action path;
- delay and sampling assumptions;
- saturation, uncertainty, and failure behavior;
- stability or performance claims and their evidence, if applicable.

DUSRM does not define a control theory or guarantee stability. Such claims require appropriate domain analysis.

## 6. Authority and control

The following concepts must remain distinct:
- **Capability:** ability to perform an action.
- **Permission:** authorization to perform an action.
- **Authority:** recognized right or role to direct a decision or action.
- **Control:** ability to influence or constrain behavior.
- **Execution:** occurrence of the behavior.

A component may be capable of actuation but lack permission or authority to request it. A controller may issue a command without evidence that the actuator executed it. A command acknowledgment is not proof of the physical effect unless the observation chain supports that conclusion.

## 7. Cross-cutting constraints

Identity, trust, safety, governance, observability, lifecycle, time, uncertainty, and resilience apply across layers. They should be attached to the relevant elements, relationships, operations, transitions, and interfaces rather than represented as an additional mandatory layer.

## 8. Technology neutrality

Cross-layer semantics must not prescribe:
- a specific API or RPC mechanism;
- a specific transport or network protocol;
- a specific encoding or serialization format;
- a specific database engine;
- a specific runtime or operating system.

For DMJ implementations, their own specifications define actual technical behavior. DUSRM describes where those responsibilities are relevant in the system architecture.

## 9. Open questions

- How should layer allocation be represented for an element performing multiple responsibilities?
- How should cross-layer cycles be analyzed?
- What minimum evidence is required for a claim that an operation produced a physical effect?
- How should authority propagation be represented in distributed systems?
