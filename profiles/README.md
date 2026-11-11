# DUSRM Domain Profiles

Profiles specialize the DUSRM core for a class of systems. They may add domain terminology, responsibility refinements, operational semantics, evidence obligations, and conformance requirements.

A profile must not silently redefine core DUSRM concepts or make one DMJ technology mandatory.

## Historical profile definitions

- [Standalone software application](standalone-application/PROFILE.md)
- [Database engine — ANANTA](database-engine/ANANTA-PROFILE.md)
- [Cyber-physical robotics — FireBot](cyber-physical-robotics/FIREBOT-PROFILE.md)

These 0.1-draft profiles preserve their historical identity and origin. They were initially prepared against an earlier core draft and are not automatically compatible with the DUSRM 1.0-preparation target.

## DUSRM 1.0-preparation reconciliation

WP5 has prepared schema 0.2 typed pilot descriptions for the standalone, ANANTA and FireBot profiles:

- [Standalone application fixture](../schema/fixtures/0.2/profiles/standalone-application.json)
- [ANANTA database-engine fixture](../schema/fixtures/0.2/profiles/ananta-database-engine.json)
- [FireBot cyber-physical robotics fixture](../schema/fixtures/0.2/profiles/firebot-cyber-physical-robotics.json)

WP6 has added a fourth profile:
- [Operating system — SAND OS pilot](operating-system/PROFILE.md)
- [SAND OS schema 0.2 fixture](../schema/fixtures/0.2/profiles/sand-os-operating-system.json)

See the [WP5 reconciliation report](../specification/DUSRM-1.0/M5-RECONCILIATION.md), [WP6 SAND OS adoption plan](../specification/DUSRM-1.0/M6-SAND-OS-ADOPTION.md), and [WP6 status](../specification/DUSRM-1.0/M6-STATUS.md).

## Registry

See [registry.json](registry.json). It now identifies DUSRM 1.0-preparation/schema 0.2-draft as the current assessment target. The original profile IDs and versions are retained. Every compatibility status remains `not-assessed`.

`review-prepared` means only that a mapping fixture and review material have been prepared. It is not an approval, compatibility result or conformance statement.

## Compatibility

See [Profile Compatibility Policy](COMPATIBILITY-POLICY.md) for profile identity, versioning, refinement, extension, composition, and migration rules.

## Profile requirements

Each profile must declare identity/version, compatible core version, scope/exclusions, concept refinements, layer responsibility mappings, operational rules, evidence obligations, permitted omissions, and conformance requirements.

A profile is a specialization of DUSRM, not a new API, protocol, programming language, or implementation requirement.
