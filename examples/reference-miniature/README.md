# Generic Monitoring System — DUSRM Example

**Status:** Illustrative only; hypothetical example.

This example demonstrates how the DUSRM 0.2 draft ontology can describe a small system. It is not a reference design, product specification, or safety guidance.

## System of interest

A hypothetical monitoring system contains a sensor assembly, a controller, and an operator display. It receives measurements, evaluates them against a configured condition, and presents an alert.

## Scope and boundary

- **SOI:** Monitoring system.
- **Inside:** Sensor assembly, controller, operator display, and their modeled interfaces.
- **Outside:** Physical environment being measured and the human operator.
- **Purpose of description:** Demonstrate entities, membership, interfaces, dependencies, operations, states, and transitions.

## Element register

| ID | Element | Kind | Status |
|---|---|---|---|
| SYS-01 | Monitoring system | System of interest | Hypothetical |
| E-01 | Sensor assembly | Component | Hypothetical |
| E-02 | Controller | Component | Hypothetical |
| E-03 | Operator display | Component | Hypothetical |
| I-01 | Measurement interface | Interface | Hypothetical |
| I-02 | Alert presentation interface | Interface | Hypothetical |
| OP-01 | Evaluate measurement | Operation specification | Hypothetical |
| EV-01 | Limit exceeded | Event type | Hypothetical |
| ST-01 | Idle | State | Hypothetical |
| ST-02 | Monitoring | State | Hypothetical |
| ST-03 | Alert active | State | Hypothetical |

## Relationship assertions

- E-01 memberOf SYS-01
- E-02 memberOf SYS-01
- E-03 memberOf SYS-01
- E-01 exposes I-01
- E-02 requires I-01
- E-02 exposes I-02
- E-03 requires I-02
- E-02 dependsOn E-01 for measurement input

These assertions are part of a hypothetical description and are not evidence of an implementation.

## Behavioral sketch

- OP-01 describes evaluating a measurement.
- A particular execution of OP-01 may observe a measurement.
- If a declared condition is met, EV-01 may be recorded.
- EV-01 may trigger a transition from ST-02 to ST-03.
- The controller may cause an alert to be presented through I-02.

The condition, timing, accuracy, failure response, and safety properties are intentionally unspecified.

## What this example tests

- System versus component distinction.
- Interface versus API distinction.
- Operation versus execution distinction.
- Event versus state distinction.
- Relationship assertions with declared semantics.
- Hypothetical versus implemented status.

## Limitations found

This miniature does not test distributed coordination, resource contention, uncertain observations, system evolution, assurance evidence, concurrency, or nested subsystems. Those remain validation work.
