# DUSRM 0.8 — TLA+ Pilot Mapping

**Status:** Formal-methods pilot; non-normative  
**Model:** TaskCompletion  
**TLA+ tools:** TLC / tla2tools v1.7.4  
**Purpose:** Demonstrate how a deliberately finite DUSRM behavior can be represented in an established formal specification tool.

## 1. Why this is a pilot, not automatic translation

DUSRM descriptions currently contain prose guards, effects, preconditions, postconditions, and claims. Natural-language text is not sufficiently formal to translate safely into executable TLA+ expressions without a controlled expression language and reviewed semantics.

Therefore this pilot uses a manually authored, traceable mapping for one small behavior. It does not claim that arbitrary DUSRM JSON can be converted automatically into TLA+.

## 2. DUSRM source behavior

The illustrative task application description contains:
- element `app-process`;
- state owner `task-state`;
- operation `CompleteTask`;
- state variable `taskStatus`, with allowed values `active` and `completed`;
- transition `TRANS-COMPLETE` from `active` to `completed`;
- guard: task exists and editing is permitted.

For this pilot, authorization is abstracted into the constant `Authorized`, and a pending request is represented by `requestPending`.

## 3. Mapping

| DUSRM concept | TLA+ representation | Interpretation |
|---|---|---|
| State variable `taskStatus` | `taskState` | Finite task lifecycle state |
| Initial condition | `Init` | Task begins active with a pending request |
| Operation `CompleteTask` | `CompleteTask` action | Operation occurrence represented as a state transition |
| Transition guard | Action conjuncts | Request is pending, authorization is true, and task is active |
| Transition effect | Primed assignments | Task becomes completed and request ceases to be pending |
| Allowed state values | `TypeOK` | State-domain invariant |
| Authorization safety condition | `CompletionSafety` | Completed state implies authorization constant is true |
| Progress assumption | `WF_vars(CompleteTask)` | A continuously enabled completion action eventually occurs |
| Desired progress | `CompletionTerminates` | Eventually the request is no longer pending |

## 4. Model assumptions and boundaries

- Authorization is a constant for the duration of this model; revocation and time-of-check/time-of-use races are not modeled.
- The operation is atomic at the abstraction level of this model.
- There is one task and one completion request.
- No storage failure, concurrency between writers, network partition, or physical effect is modeled.
- Weak fairness is an explicit progress assumption. Without it, stuttering forever is permitted and eventual completion does not follow.
- The model does not prove that a real user interface, application, or database implementation behaves this way.

## 5. Checks executed by TLC

The configuration checks:
- invariant `TypeOK`;
- invariant `CompletionSafety`;
- temporal property `CompletionTerminates`.

A successful TLC run means no counterexample was found within this finite model and its declared assumptions. It is not a proof of the implementation, nor a general proof of the full FireBot or ANANTA system.

## 6. Reproducibility

From this directory, using Java 17 or newer:

```bash
curl -L --fail --silent --show-error \
  -o tla2tools.jar \
  https://github.com/tlaplus/tlaplus/releases/download/v1.7.4/tla2tools.jar

java -cp tla2tools.jar tlc2.TLC \
  -cleanup -config TaskCompletion.cfg TaskCompletion.tla
```

The JAR is downloaded during CI rather than committed to this repository.

## 7. Next formal-methods work

- Model authorization revocation and command cancellation.
- Add an explicit failure/degraded mode.
- Model concurrent requests and idempotency.
- Map selected ANANTA WAL/recovery claims to a separate state machine.
- Model FireBot's local emergency-stop precedence independently of network or AI availability.
- Require a traceability record and review for every abstraction or assumption introduced by a formal model.
