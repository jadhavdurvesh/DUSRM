# DUSRM Schema Migration — 0.1-draft to 0.2-draft

**Status:** Proposed migration guidance; non-normative  
**Source schema:** urn:dusrm:schema:description:0.1-draft  
**Target schema:** urn:dusrm:schema:description:0.2-draft

## 1. Migration rule

A schema 0.1 description must not be relabelled as schema 0.2 by changing only its `schemaVersion`. The object model, typed references, required collections and status dimensions are different.

Preserve the original file and create a separate 0.2 output. Record the source file hash, source schema, target schema, migration tool/version, human decisions and all unresolved mappings.

## 2. Field mapping

| Schema 0.1 | Schema 0.2 | Migration treatment |
|---|---|---|
| schemaVersion | schemaVersion | Set to 0.2-draft only after all conversion steps and validation |
| dusrmVersion | dusrmVersion | Preserve source conceptual version or assign the explicitly approved target draft; do not infer stable 1.0 |
| descriptionId/title/summary | descriptionId/title/summary | Preserve unchanged where meaning is unchanged |
| status | descriptionState | Map only to a description lifecycle state after review; legacy status is not a universal lifecycle value |
| context.systemOfInterest.status | context.systemOfInterest.realizationState | Contextual conversion; source status is not automatically realization maturity |
| context.scope | context.scope | Preserve |
| context.boundary | context.boundary | Add stable boundary identifier and retain inclusions/exclusions |
| context.environment | context.environment | Convert entries to typed Environment Participants; choose category and kind explicitly |
| elements[].kind | elements[].kind | Preserve as a provisional specific kind; assign category and roles with review |
| elements[].status | elements[].realizationState | Contextual conversion; not a mechanical enum substitution |
| elements[].external | context.environment or elements | If true and outside the SOI boundary, move to environmentParticipants; otherwise clarify boundary and internal status |
| responsibilities[].status | responsibilities[].realizationState | Contextual conversion; retain original status in migration report |
| responsibilities[].primaryLayer | responsibilities[].primaryLayer | Preserve and validate against L1–L8 |
| realizations[].status | realizations[].realizationState | Contextual mapping; preserve rationale/evidence |
| relationships[].sourceRef/targetRef | relationships[].source/target | Replace each string with a typed reference chosen from the target object registry |
| relationships[].status | designDisposition / realizationState / assessmentResult | Inspect the assertion. Do not map mechanically because one legacy status may mean different things |
| relationships[].type = realizes | realizations collection or implements | If element-to-responsibility, convert to Realization record; if implementation-to-specification, convert to implements; otherwise manual resolution |
| operations[].ownerRef | operations[].ownerRef | Convert string to participantReference with explicit kind |
| stateVariables[].subjectRef | stateVariables[].subjectRef | Convert string to participantReference with explicit kind |
| transitions[].from/to | states and transitions[].fromStateRef/toStateRef | Create explicit State objects linked to State Variable; retain source values and meaning |
| transitions[].trigger | events and triggerEventRefs | Create Event only when source semantics are known; otherwise leave unmapped and record a finding |
| evidence[].kind/method/sourceUri/revision | evidence typed fields | Map kind where possible; add method, context, relation and scope based on provenance; do not invent missing metadata |
| constraints/invariants[].status | assessmentResult and/or assertion properties | Human review required; preserve source value and assumptions |
| extensions | extensions | Retain only if namespace and ownership are documented; check core redefinition |

## 3. Legacy status conversion is contextual

Schema 0.1 status values are overloaded. Examples:
- `planned` may map to realizationState planned;
- `implemented` may map to realizationState implemented, but assessmentResult remains notAssessed unless an assessment exists;
- `simulated` describes an evidence context and does not mean physical realization is implemented;
- `observed` or `tested` describes evidence method/context, while pass/fail/inconclusive is a separate assessment result;
- `verified` must not map to assessmentResult pass unless criterion, method, scope, evidence and assessor are recorded;
- `assumed` should become an explicit assumption assertion or assumption evidence record;
- `unknown` may indicate realization, applicability, or assessment is unknown; the object must be inspected;
- `notApplicable` maps to applicability only when the concern is genuinely outside the declared scope;
- `rejected` normally maps to designDisposition rejected, but can describe an assessment failure in some records.

A migration tool must emit a manual-review finding when the source value does not identify which dimension it describes.

## 4. Typed endpoint mapping procedure

For each relationship endpoint:
1. locate the referenced identifier;
2. identify the actual source object kind;
3. map to one of the schema 0.2 typed-reference kinds;
4. check the relationship's endpoint-kind table;
5. record any unresolved, missing, or ambiguous target;
6. do not infer an operation, event, state, requirement, or specification from a name alone.

An unresolved identifier must stop automatic migration of that relationship. It must not be represented as an arbitrary Element just to make schema validation pass.

## 5. Loss and preservation

A migration report must identify:
- legacy fields removed or renamed;
- categories and roles supplied by a reviewer;
- typed references inferred or manually selected;
- relationships that changed meaning or split into multiple records;
- state values converted into explicit State records;
- evidence metadata that was unavailable;
- statuses that could not be mapped without human judgement;
- profile compatibility that remains not-assessed.

## 6. Dual validation

During migration:
- retain the original schema 0.1 file;
- validate the original with schema 0.1 and its legacy validator;
- validate the new file with schema 0.2 structural validation;
- run a future schema 0.2 semantic validator when available;
- compare the migration report and preserve all unresolved findings.

A schema 0.2 structural pass does not imply semantic conformance or source-to-target equivalence.

## 7. Status

This document is migration guidance only. No general-purpose schema 0.1 to 0.2 migration utility is included in WP3.
