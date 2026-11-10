# Schema 0.2 Draft Fixtures

This directory contains fixtures for `urn:dusrm:schema:description:0.2-draft`.

Run from the repository root:

```bash
python scripts/validate_schema_0_2_fixtures.py
```

## Cases

- `valid-minimal.json` — minimum description envelope.
- `valid-sand-os-architecture.json` — populated SAND OS architecture pilot that exercises all 17 relationship endpoint signatures.
- `invalid-wrong-typed-endpoint.json` — expects rejection because a `performs` source is not an Execution.
- `invalid-legacy-status-field.json` — expects rejection because schema 0.2 separates descriptionState and disallows the legacy top-level status.

These fixtures validate JSON Schema structure and endpoint kinds only. They do not test cross-collection reference resolution, semantic correctness, evidence adequacy, or system conformance. The SAND OS example is a DUSRM-side architectural fixture and does not modify the SAND OS repository.
