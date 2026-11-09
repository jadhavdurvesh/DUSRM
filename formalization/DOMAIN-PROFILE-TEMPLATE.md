# DUSRM 0.5 — Domain Profile Template

**Status:** Template; non-normative

Use this template when specializing DUSRM for a domain such as databases, robotics, distributed systems, embedded computing, or applications.

## 1. Profile identity

- Profile name:
- Profile identifier:
- Version:
- DUSRM core version:
- Maintainer:
- Status: draft / reviewed / approved within project
- Intended users:

## 2. Domain scope

- Domain and system classes covered:
- Explicit exclusions:
- Typical operating environments:
- Typical stakeholders:
- Relevant external standards:
- Known assumptions:

## 3. Core concept mapping

For each domain concept, state:
- domain term;
- DUSRM concept;
- definition;
- specialization or extension;
- rationale;
- evidence/prior art.

Do not redefine a DUSRM core term without recording an explicit proposal and compatibility impact.

## 4. Layer responsibility refinement

For each domain-specific responsibility:
- responsibility identifier;
- definition;
- primary DUSRM layer;
- parent core responsibility, if refining one;
- elements that may realize it;
- provided/required responsibilities;
- domain constraints.

A profile-specific responsibility must map to one core responsibility or be explicitly identified as an extension outside the core model.

## 5. Operational semantics

Define relevant:
- operation categories;
- execution lifecycle refinements;
- state variables and state domains;
- event categories;
- transition rules;
- timing and clock assumptions;
- concurrency/coordination assumptions;
- failure, degradation, and recovery semantics.

## 6. Safety, security, and assurance

Identify:
- hazards and threat classes;
- authority boundaries;
- safety/security constraints;
- verification and validation evidence;
- domain-specific assurance methods;
- what the profile does not assess.

## 7. Conformance profile

Define:
- applicable DUSRM conformance level;
- required description content;
- permitted omissions and rationale;
- required evidence;
- assessment method;
- exclusions and limitations.

## 8. Examples

Include at least:
- a minimal example;
- a representative system example;
- a failure/degraded-mode example;
- a traceability example.

## 9. Compatibility

Explain how the profile maps to the DUSRM core and how future core changes affect it.
