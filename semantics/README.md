# DUSRM Operational Semantics

This directory contains the 0.4 working draft describing how systems behave over time.

## Documents

- [Operational semantics](../specification/DUSRM-0.4/OPERATIONAL-SEMANTICS.md)
- [Abstract transition-system kernel](../specification/DUSRM-0.4/FORMAL-KERNEL.md)
- [Events, time, and temporal constraints](EVENTS-AND-TIME.md)
- [Concurrency, causality, and coordination](CONCURRENCY-AND-CAUSALITY.md)
- [Failure, degradation, and recovery](FAILURE-AND-RECOVERY.md)
- [Cross-layer operational rules](CROSS-LAYER-RULES.md)
- [Operational semantics prior-art notes](../research/OPERATIONAL-SEMANTICS-PRIOR-ART.md)

## Principles

- An operation specification is not an execution occurrence.
- An event occurrence is not necessarily its observation or processing time.
- A transition relation describes permitted behavior, not guaranteed progress.
- Safety and liveness claims require explicit assumptions.
- Concurrency does not imply a global total event order.
- Failure cause, failure observation, and recovery are distinct.
- Cross-layer behavior is traced explicitly; the layer stack is not a mandatory execution pipeline.

All documents are working drafts and non-normative.
