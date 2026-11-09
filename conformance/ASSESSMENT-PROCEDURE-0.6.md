# DUSRM 0.6 — Description Assessment Procedure

**Status:** Draft; non-normative  
**Purpose:** Define a repeatable assessment of a DUSRM system description.

## 1. Assessment target

The assessment target is a named and versioned DUSRM description and its supporting evidence. It is not automatically the real system or its implementation.

## 2. Assessment inputs

Required inputs:
- DUSRM version;
- profile and profile version;
- system of interest and scope;
- architecture description or model;
- evidence register;
- list of assumptions and exclusions;
- validation method and assessment date.

## 3. Assessment stages

1. **Scope review:** verify SOI, context, boundary, environment, and exclusions.
2. **Ontology review:** verify elements, roles, state, operations, interfaces, constraints, and evidence terms.
3. **Allocation review:** inspect responsibility definitions, primary layer allocations, and element realization relations.
4. **Relationship review:** inspect typed relations, non-adjacent links, feedback, and cross-cutting concerns.
5. **Operational review:** inspect execution, events, time, concurrency, transitions, failure, and recovery.
6. **Traceability review:** inspect links from needs/requirements to responsibilities, elements, operations, criteria, and evidence.
7. **Profile review:** verify profile obligations, allowed omissions, and extensions.
8. **Evidence review:** confirm status, provenance, method, and limitations.
9. **Findings and report:** publish result, open issues, and next actions.

## 4. Assessment levels

The draft levels in `TRACEABILITY-AND-CONFORMANCE.md` remain:
- Level A — Vocabulary-compatible
- Level B — Structurally well-formed
- Level C — Behaviorally specified
- Level D — Formally assessed
- Level E — Implementation-evaluated

The assessor must state which optional capabilities are not applicable and why. A small application need not have a distributed-system model if no distributed behavior exists in the declared scope.

## 5. Result

Permitted outcomes:
- Pass
- Pass with findings
- Fail
- Not assessable

The report must identify mandatory checks, failed or skipped checks, evidence, assumptions, profile, tool versions, reviewer, and limitations.

## 6. Prohibited interpretations

A DUSRM assessment is not:
- safety certification;
- regulatory approval;
- security certification;
- proof of fitness for purpose;
- proof that undocumented or unobserved implementation behavior exists;
- endorsement of a particular DMJ technology.

## 7. Report template

- Assessment ID:
- SOI:
- DUSRM version:
- Profile:
- Scope and exclusions:
- Assessment level:
- Checks performed:
- Checks not applicable:
- Findings:
- Evidence:
- Assumptions:
- Limitations:
- Result:
- Reviewer/date:
