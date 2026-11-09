# DUSRM 0.2 — Informal Notation Guide

**Document ID:** DUSRM-NOT-001  
**Status:** Illustrative only; not a formal language or interchange format

## 1. Purpose

This notation provides a compact way to discuss DUSRM concepts in documents and reviews. It is not a programming language, configuration format, schema, or executable specification.

## 2. Basic forms

### 2.1 Declare a system of interest

```text
System <id> {
  purpose: <reason for analysis or design>
  boundary: <boundary-id>
  environment: <environment-id>
  status: planned | implemented | observed | hypothetical
}
```

### 2.2 Declare elements and membership

```text
Element <id> {
  kind: <descriptive category>
  status: <claim status>
}

<element-id> --memberOf--> <system-id>
```

### 2.3 Declare a typed relationship

```text
<source-id> --<relationship-type>--> <target-id>
```

A relationship may include scope, validity, rationale, and evidence:

```text
Relationship <id> {
  type: dependsOn
  source: <element-id>
  target: <element-id>
  scope: <system-id>
  status: assumed
  rationale: "<why this dependency is asserted>"
}
```

### 2.4 Declare an interface

```text
Interface <interface-id> {
  participants: [<participant-a>, <participant-b>]
  interaction-kind: <logical | physical | informational | human | other>
  contract: <reference to separate interface specification>
}
```

The interface contract may reference an external API, protocol, mechanical specification, signal definition, or human procedure. DUSRM does not redefine those specifications.

### 2.5 Declare state and transition

```text
State <state-a> of <subject-id>
State <state-b> of <subject-id>

Transition <transition-id> {
  subject: <subject-id>
  from: <state-a>
  to: <state-b>
  trigger: <event-id>
  guard: <condition-or-unspecified>
  effect: <effect-or-unspecified>
}
```

### 2.6 Record uncertainty and evidence

```text
Assertion <assertion-id> {
  statement: "<claim about the SOI>"
  status: planned | implemented | observed | assumed | verified | rejected
  evidence: [<evidence-id>, ...]
  confidence: <qualitative or quantified, if justified>
}
```

Do not use `verified` without recording the verification method and evidence.

## 3. Status vocabulary

The following values are suggested labels, not automatic proof:

- `planned`: intended for a future design or release.
- `implemented`: present in an implementation; not necessarily tested.
- `observed`: observed under a stated context.
- `assumed`: used as an assumption without sufficient evidence.
- `verified`: assessed against a defined criterion using recorded method and evidence.
- `rejected`: considered and explicitly not accepted.

A project may define additional status labels, but their meanings must be documented.

## 4. Worked miniature example

The following example is intentionally generic. It demonstrates the notation, not a complete engineering design.

```text
System MonitoringSystem {
  purpose: "Describe a simple measurement-and-alert system"
  boundary: MonitoringBoundary
  environment: OperatingEnvironment
  status: hypothetical
}

Element SensorAssembly { kind: physical-subsystem }
Element Controller { kind: computing-subsystem }
Element OperatorDisplay { kind: user-interface }

SensorAssembly --memberOf--> MonitoringSystem
Controller --memberOf--> MonitoringSystem
OperatorDisplay --memberOf--> MonitoringSystem

SensorAssembly --exposes--> MeasurementInterface
Controller --requires--> MeasurementInterface
Controller --dependsOn--> SensorAssembly

State MonitoringIdle of Controller
State MonitoringActive of Controller
State AlertActive of Controller

Transition StartMonitoring {
  subject: Controller
  from: MonitoringIdle
  to: MonitoringActive
  trigger: StartCommand
  guard: "required preconditions satisfied"
}

Transition RaiseAlert {
  subject: Controller
  from: MonitoringActive
  to: AlertActive
  trigger: LimitExceededEvent
  guard: "alert condition is true"
}
```

## 5. Notation limitations

The notation does not yet define:
- grammar, parsing, or canonical serialization;
- type checking or validation algorithms;
- units, dimensional analysis, or uncertainty calculus;
- temporal logic or concurrency semantics;
- cardinality and multiplicity constraints;
- diagram interchange or machine-readable schema.

Those belong to later formalization work and must not be inferred from these examples.
