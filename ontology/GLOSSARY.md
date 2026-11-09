# DUSRM 0.2 — Controlled Glossary

**Document ID:** DUSRM-GLO-001  
**Status:** Working draft; non-normative

| Term | Draft definition | Notes / distinction |
|---|---|---|
| Assertion | A statement in a description about a subject, design, requirement, or assumption | Must carry status and provenance when material |
| Boundary | A declared distinction between what is inside, outside, or crossing a system scope | May be physical, logical, organizational, temporal, or analytical |
| Capability | An ability to perform an operation, provide an interaction, or access a resource under conditions | Separate from permission or authority |
| Component | An element considered as a constituent of a particular system | A contextual role, not always a permanent intrinsic type |
| Constraint | A condition restricting allowable structure, properties, states, or behavior | May be violated in an actual system |
| Element | A distinguishable subject represented in a system description | Not the representation artifact itself |
| Environment | External entities, conditions, events, and influences relevant to an SOI | Relative to the selected boundary |
| Evidence | Information used to support, refute, qualify, or trace an assertion | Evidence quality and provenance matter |
| Event | An occurrence represented as relevant to a system | May be internal/external and observed/generated |
| Execution | An occurrence of behavior over time | Distinct from the operation specification |
| Interface | A specified point or boundary of interaction between participants | Broader than software API |
| Invariant | A constraint that must remain true across a declared scope or conditions | Requires scope and assumptions |
| Operation | A specification of behavior a subject can perform or offer | Distinct from a specific execution |
| Property | A characteristic attributed to an element or relationship | May be measured, assumed, or computed |
| Relationship | A typed assertion connecting two or more elements | A line with no defined meaning is insufficient |
| Requirement | A documented need, obligation, or condition expected of a system or element | Not proof of satisfaction |
| Resource | An entity, capacity, or means required, allocated, occupied, consumed, shared, or controlled | Can be physical or non-physical |
| State | A modeled condition of a subject over a declared scope and time or interval | Need not be a single global mode |
| Subsystem | A system included within a larger system's scope | May have its own boundary and environment |
| System | An organized whole considered within a declared scope and boundary | In this project, system-of-interest is the subject selected for analysis |
| System description | A representation of an SOI using DUSRM concepts | Not the SOI itself |
| System of interest (SOI) | The real, planned, or hypothetical system selected for analysis, design, operation, or assurance | Must have declared purpose/reason, scope, boundary, and context |
| Transition | A defined change from one modeled state or condition to another | May include trigger, guard, effect, timing, and failure semantics |

## Preferred usage

- Use **SOI** for the real or intended subject being examined.
- Use **system description** for the model or document representing the SOI.
- Use **DUSRM concept** for a term defined by the reference model.
- Use **component** only relative to a named parent system.
- Use **operation** for defined behavior and **execution** for an occurrence.
- Use **capability** for ability and **authority/permission** for authorization.
- Use **requirement** for an obligation and **constraint** for a condition applied to a model or behavior.

If a term is overloaded in a domain, qualify it rather than silently importing domain-specific meaning.
