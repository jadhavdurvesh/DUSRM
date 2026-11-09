# DUSRM Tests

- `test_semantics.py` — semantic validator unit and regression tests, including relationship signatures.
- `../scripts/validate_schema_fixtures.py` — JSON Schema and structural fixture expectations.

Run:

```bash
python scripts/validate_schema_fixtures.py
python -m unittest discover -s tests -v
```

The DUSRM 0.8 and 0.9 workflows additionally run CLI checks and TLA+ models through TLC.
