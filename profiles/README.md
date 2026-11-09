# DUSRM Domain Profiles

Profiles specialize the DUSRM core for a class of systems. They may add domain terminology, responsibility refinements, operational semantics, evidence obligations, and conformance requirements.

A profile must not silently redefine core DUSRM concepts or make one DMJ technology mandatory.

## Profiles in the 0.6 draft

- [Standalone software application](standalone-application/PROFILE.md)
- [Database engine — ANANTA](database-engine/ANANTA-PROFILE.md)
- [Cyber-physical robotics — FireBot](cyber-physical-robotics/FIREBOT-PROFILE.md)

## Registry

See [registry.json](registry.json). Each entry records its profile version, candidate core version, and compatibility assessment status. The existing profiles are currently marked `not-assessed`; a candidate core version is not an approval.

## Compatibility

See [Profile Compatibility Policy](COMPATIBILITY-POLICY.md) for profile identity, versioning, refinement, extension, composition, and migration rules.

## Profile requirements

Each profile must declare identity/version, compatible core version, scope/exclusions, concept refinements, layer responsibility mappings, operational rules, evidence obligations, permitted omissions, and conformance requirements.

A profile is a specialization of DUSRM, not a new API, protocol, programming language, or implementation requirement.
