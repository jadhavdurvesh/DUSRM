# Schema 0.2 Draft Fixtures

This directory contains fixtures for `urn:dusrm:schema:description:0.2-draft`.

Run from the repository root:

```bash
python scripts/validate_schema_0_2_fixtures.py
python -m unittest discover -s tests -p 'test_profiles_0_2.py' -v
```

## Core structural fixtures

- `valid-minimal.json` — minimum description envelope.
- `valid-sand-os-architecture.json` — populated SAND OS architecture pilot; exercises all 17 relationship endpoint signatures.
- `invalid-wrong-typed-endpoint.json` — expects rejection because a `performs` source is not an Execution.
- `invalid-legacy-status-field.json` — expects rejection because schema 0.2 separates descriptionState and disallows the legacy top-level status.

## WP5 domain profile fixtures

The following three profile descriptions are stored under `profiles/` and tested structurally and semantically by `tests/test_profiles_0_2.py`:

- `profiles/standalone-application.json` — illustrative single-user local task application.
- `profiles/ananta-database-engine.json` — repository-informed ANANTA native DBMS profile with explicit transaction, WAL and embedded API boundaries.
- `profiles/firebot-cyber-physical-robotics.json` — FireBot system description that distinguishes software simulation, planned physical platform and local safety requirements.

All three profile fixtures are expected to have zero semantic errors. Each deliberately emits one profile-compatibility warning because its registry status remains `not-assessed`. This is expected and must not be suppressed.

The SAND OS and FireBot/ANANTA repository references are used as DUSRM-side architecture examples only. No external project repository is modified by fixture validation.

## Validation boundary

Schema/semantic fixture success does not establish independent profile compatibility, implementation behavior, evidence sufficiency, safety, or overall DUSRM conformance.
