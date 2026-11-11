# DUSRM Tests

## Historical schema 0.1 and 0.x tooling

- `test_semantics.py` — schema 0.1/0.9 semantic validator unit and regression tests.
- `../scripts/validate_schema_fixtures.py` — schema 0.1 structural fixture expectations.

## Schema 0.2 tooling

- `test_semantics_0_2.py` — typed-reference, relationship, realization, state, interface, resource, evidence, profile and migration regression tests.
- `test_profiles_0_2.py` — schema and semantic consistency checks for standalone, ANANTA and FireBot profile fixtures; confirms compatibility warnings remain present.
- `../scripts/validate_schema_0_2_fixtures.py` — core schema 0.2 structural fixture expectations.
- `../scripts/validate_semantics_0_2.py` — schema 0.2 cross-reference and semantic checks.
- `../scripts/migrate_schema_0_1_to_0_2.py` — loss-aware migration CLI.

Run from the repository root:

```bash
python scripts/validate_schema_fixtures.py
python scripts/validate_schema_0_2_fixtures.py
python -m unittest discover -s tests -v
python scripts/validate_semantics_0_2.py schema/fixtures/0.2/valid-minimal.json
python scripts/validate_semantics_0_2.py schema/fixtures/0.2/valid-sand-os-architecture.json
python -m unittest discover -s tests -p 'test_profiles_0_2.py' -v
```

The profile fixtures should produce no semantic errors. They intentionally produce a profile-compatibility warning until their registry compatibility status is independently assessed and explicitly changed.

The 0.8 and 0.9 workflows additionally run their historical semantic checks and TLA+ model checks through TLC. The dedicated 1.0-preparation workflow runs schema 0.2 structural, semantic, profile and migration tests.

Passing tests do not establish full DUSRM conformance, implementation correctness, safety or security.
