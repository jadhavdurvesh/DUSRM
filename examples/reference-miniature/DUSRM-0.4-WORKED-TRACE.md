# DUSRM 0.4 — Worked Operational Trace

**Status:** Illustrative only; hypothetical system  
**Purpose:** Demonstrate operation, execution, event, state, transition, time, and failure concepts.

## 1. System of interest

A hypothetical monitoring controller receives a measurement, evaluates it, and presents an alert when a declared condition is met.

This example is intentionally simple and is not a real product design or a safety control design.

## 2. States

- `Idle`: no measurement evaluation is in progress.
- `Evaluating`: a measurement is being evaluated.
- `AlertActive`: an alert condition has been established.
- `Degraded`: the controller cannot establish a trustworthy current result.
- `Terminated`: the illustrative execution occurrence has ended.

These are illustrative state definitions. A production system may require more detail.

## 3. Operation specification

`EvaluateMeasurement`

- Preconditions: a measurement observation is available and its provenance is known.
- Inputs: measurement value, unit, occurrence timestamp, observation timestamp, quality metadata.
- Effect: evaluate the declared condition and emit a result.
- Success condition: result is produced and recorded with its input reference.
- Failure conditions: invalid measurement, stale observation, unavailable computation, or an unspecified error.
- Timing: no numerical deadline is assumed in this example.

## 4. Event and time record

| Event | Meaning | Time label |
|---|---|---|
| E1 | Sensor sample occurs | t_occurrence |
| E2 | Controller receives sample | t_observation |
| E3 | Evaluation begins | t_start |
| E4 | Evaluation result is produced | t_result |
| E5 | Alert presentation is observed | t_effect |

The time values are symbols, not actual timestamps. The clock source and uncertainty would need to be recorded in a real description.

## 5. Illustrative trace

```text
Initial configuration:
  controller.state = Idle

E1: MeasurementSampled
  controller.state remains Idle

E2: MeasurementObserved
  if observation is valid and fresh:
    controller.state -> Evaluating
    create execution X1 of EvaluateMeasurement
  else:
    controller.state -> Degraded
    record reason

X1:
  if evaluation completes and condition is false:
    X1 outcome = Succeeded
    controller.state -> Idle

  if evaluation completes and condition is true:
    emit LimitExceededEvent
    X1 outcome = Succeeded
    controller.state -> AlertActive
    request alert presentation

  if evaluation cannot complete:
    X1 outcome = Failed or Unknown
    controller.state -> Degraded
    record available failure evidence
```

## 6. Transition table

| Source | Trigger/guard | Result | Notes |
|---|---|---|---|
| Idle | Valid, fresh sample observed | Evaluating | Create execution occurrence |
| Idle | Invalid or stale sample | Degraded | No trustworthy evaluation |
| Evaluating | Evaluation succeeds; condition false | Idle | Record result |
| Evaluating | Evaluation succeeds; condition true | AlertActive | Request alert presentation |
| Evaluating | Evaluation fails or times out | Degraded | Outcome may be uncertain |
| AlertActive | Declared clear condition satisfied | Idle | Clear policy is domain-specific |
| Degraded | Recovery condition satisfied | Idle or Evaluating | Must be separately specified |

## 7. Concurrency example

Two samples may be received before the first evaluation has finished. A real model must declare whether:
- both evaluations may execute concurrently;
- newer samples supersede older ones;
- evaluations are serialized;
- stale results are discarded;
- results are ordered by event time, observation time, sequence, or another rule.

DUSRM does not prescribe a policy.

## 8. Failure example: lost acknowledgment

Suppose the controller requests the display to show an alert, but no acknowledgment is received.

The controller must not automatically conclude that the alert was not displayed. The effect may have occurred while its acknowledgment was lost.

The outcome should be recorded as unknown until additional evidence is obtained or a declared retry/reconciliation policy resolves it.

## 9. DUSRM concepts demonstrated

- Operation specification vs execution occurrence
- Event occurrence vs observation
- State vs transition
- Preconditions and guards
- Time semantics
- Concurrent executions
- Uncertain external effects
- Failure and degraded mode

## 10. Limitations

This example does not define thresholds, units, sensor accuracy, clock synchronization, control-loop stability, safety integrity, or real-time guarantees. Those require domain-specific specification and evidence.
