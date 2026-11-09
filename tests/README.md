# DUSRM Tests

- `test_semantics.py` — semantic validator unit and regression tests.
- `../scripts/validate_schema_fixtures.py` — JSON Schema and structural fixture expectations.

Run:

```bash
python scripts/validate_schema_fixtures.py
python -m unittest discover -s tests -v
```

The CI workflow additionally runs the CLI against expected semantic-negative fixtures and TLC against the formal task-completion model.
