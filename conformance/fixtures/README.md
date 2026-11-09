# DUSRM Conformance Fixtures

**Suite:** DUSRM-CONFORMANCE-FIXTURES-0.1-draft  
**Target:** DUSRM 0.7-draft / description schema 0.1-draft

| Fixture | Expected result | Purpose |
|---|---|---|
| valid-minimal.json | Schema pass | Small structurally valid description |
| valid-multilayer-realization.json | Schema pass | One element realizes responsibilities in L3, L4 and L5 |
| invalid-missing-boundary.json | Schema fail | Required system boundary omitted |
| invalid-layer.json | Schema fail | Invalid layer identifier |
| invalid-duplicate-element-identifiers.json | Schema pass; semantic failure pending | Duplicate element IDs across collection |
| invalid-dangling-reference.json | Schema pass; semantic failure pending | Realization references a missing element |
| invalid-status-upgrade.json | Schema fail | Unsupported status value |

## Execution

The GitHub Actions workflow `.github/workflows/dusrm-schema-validation.yml` runs `scripts/validate_schema_fixtures.py` on relevant pushes and pull requests.

The script checks schema syntax and structure and confirms the expected structural acceptance/rejection behavior. The duplicate-ID and dangling-reference fixtures deliberately pass JSON Schema because those conditions require semantic checks.

## Important note

Passing this fixture suite does not establish full DUSRM conformance, profile compatibility, implementation correctness, or system safety. Semantic validation remains future work.
