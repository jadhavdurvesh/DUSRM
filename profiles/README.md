# DUSRM Domain Profiles

Profiles specialize the DUSRM core for a class of systems. They may add domain terminology, responsibility refinements, operational semantics, evidence obligations, and conformance requirements.

A profile must not silently redefine core DUSRM concepts or make one DMJ technology mandatory.

## Profiles in the 0.6 draft

- [Standalone software application](standalone-application/PROFILE.md) — tests DUSRM on a small local application without networking or distributed infrastructure.
- [Database engine — ANANTA](database-engine/ANANTA-PROFILE.md) — maps a native database engine using repository documentation and explicit maturity boundaries.
- [Cyber-physical robotics — FireBot](cyber-physical-robotics/FIREBOT-PROFILE.md) — maps the integrated robot project while distinguishing simulation, plans, and physical implementation.

## Profile requirements

Each profile should declare:
- profile identity and version;
- compatible DUSRM core version;
- domain scope and exclusions;
- core concept refinements;
- layer responsibility refinements;
- operational and temporal rules;
- safety/security/assurance concerns;
- permitted omissions and applicability rules;
- validation and evidence requirements;
- mapping to other standards or technologies where useful.

A profile is a specialization of DUSRM, not a new API, protocol, programming language, or implementation requirement.
