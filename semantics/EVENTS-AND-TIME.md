# DUSRM 0.4 — Events, Time, and Temporal Constraints

**Document ID:** DUSRM-SEM-003  
**Status:** Working draft; non-normative  
**Version:** 0.4-draft

## 1. Purpose

This document describes how DUSRM represents events and temporal facts. Time is critical in databases, distributed systems, real-time applications, robotics, and human-machine interactions, but timestamps alone do not establish causality or a guaranteed event order.

## 2. Event occurrence

An event occurrence is a specific occurrence represented as relevant to an SOI. Its description should include, where available:

| Field | Meaning |
|---|---|
| Event identity | Unique identifier within a declared scope |
| Event type | Defined category of event |
| Source | Entity or process reported to have generated it |
| Subject | Entity or condition the event concerns |
| Event time | Time the event is asserted to have occurred |
| Observation time | Time an observer obtained the event information |
| Processing time | Time a system processed the event information |
| Clock reference | Clock domain, epoch, and time scale |
| Uncertainty | Resolution, estimated error, or interval if known |
| Causal references | Events or conditions known to precede or enable it |
| Payload/reference | Associated data or evidence |
| Status | Generated, observed, inferred, delayed, duplicated, lost, or uncertain, as applicable |

Not all fields will be available. Missing timestamps must not be invented.

## 3. Distinct temporal meanings

- **Occurrence time:** when the represented event happened.
- **Observation time:** when it was sensed or received by an observer.
- **Processing time:** when a component processed it.
- **Recording time:** when it was persisted or logged.
- **Decision time:** when a decision based on it was made.
- **Effect time:** when an effect became observable or took effect.

These times may differ significantly. A delayed observation must not be treated as a fresh occurrence without an explicit freshness rule.

## 4. Clock domains

Every timestamp should be associated with its clock domain and interpretation where relevant.

A description should identify:
- clock identity or source;
- monotonic versus wall-clock semantics;
- time scale or epoch;
- resolution;
- synchronization assumptions;
- uncertainty or maximum known offset;
- reset, wraparound, or loss-of-synchronization behavior, when relevant.

Two numeric timestamps cannot safely be ordered solely by comparing their values if their clock domains or synchronization assumptions differ.

## 5. Causality and order

DUSRM distinguishes:
- **temporal order:** based on comparable time information;
- **causal order:** one event or action is known to causally precede another;
- **observation order:** the order in which an observer received or recorded information;
- **processing order:** the order in which a component processed information.

These orders are not interchangeable.

A causal relation should be transitive and irreflexive within the described causal model. If neither event is known to causally precede the other, their causal order is unspecified; do not invent an order from display order or unsynchronized wall-clock timestamps.

## 6. Temporal constraints

DUSRM may record the following temporal constraint types:

| Constraint | Meaning |
|---|---|
| Deadline | Latest permitted completion or effect time |
| Timeout | Maximum wait or duration before a specified disposition |
| Duration | Time interval associated with an operation or state |
| Period | Intended interval between recurring events or activations |
| Latency | Delay between named start and end observations |
| Freshness | Maximum accepted age of information for a purpose |
| Expiry | Time or condition after which an item is no longer considered valid |
| Ordering | Required before/after relationship |
| Synchronization | Required relation between clocks, activities, or observations |
| Dwell time | Minimum or maximum time spent in a state or condition |

Every constraint should identify its start and end points, clock reference, tolerance, and response to violation.

## 7. Deadlines and timeouts

A deadline is not a guarantee that an operation will complete by that time. A system description must specify:
- what completion means;
- which clock measures the deadline;
- whether the deadline is hard, soft, or advisory;
- what happens when it is missed;
- whether cancellation, degraded mode, or escalation occurs.

A timeout indicates that a wait or operation exceeded a declared limit. It does not necessarily prove the remote operation failed; the outcome may be unknown.

## 8. Sampling and freshness

For periodic or sampled information, describe:
- nominal sampling period;
- observed sample time;
- sequence or version information where applicable;
- expected jitter or uncertainty;
- maximum useful age;
- behavior when samples are missing, repeated, delayed, or out of order.

A sensor's sample time and the time it reaches a controller are different facts.

## 9. Timed transitions

A transition may be enabled by:
- an event occurrence;
- an elapsed duration;
- a deadline or timeout;
- a state predicate becoming true;
- a combination of event and guard conditions.

The model should state whether the timing condition is evaluated continuously, at discrete checks, or upon event processing.

## 10. Worked example

A sensor observes a temperature condition at time t1. The controller receives that observation at t2 and processes it at t3.

The description records:
- t1 as occurrence/sample time;
- t2 as observation/receipt time;
- t3 as processing time;
- the relevant clock domains and uncertainty;
- whether the observation is fresh enough for the intended operation.

If the observation is too old, the system may reject it, mark it stale, use a degraded policy, or request a new observation. DUSRM does not prescribe one universal response.

## 11. Open questions

- Should DUSRM define a standard clock-reference vocabulary?
- Should uncertainty always be an interval, or may other uncertainty representations be referenced?
- How should time be described in systems with no global clock?
- How should event-time windows and late arrivals be handled?
- Which temporal constraints are meaningful at the universal level versus a domain profile?

## 12. Reference concepts

The OMG specifications catalog includes formal specifications for UML state-machine semantics and for UML profiles concerning schedulability, performance, and time. DUSRM should map to established temporal and behavioral formalisms where appropriate rather than inventing replacements.

Sources:
- https://www.omg.org/spec
- https://www.omg.org/spec/UML
- https://lamport.azurewebsites.net/tla/high-level-view.html
