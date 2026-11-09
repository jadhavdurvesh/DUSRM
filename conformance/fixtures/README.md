# DUSRM Conformance Fixtures

**Suite:** DUSRM-CONFORMANCE-FIXTURES-0.1-draft  
**Target:** DUSRM 0.7-draft / description schema 0.1-draft

| Fixture | Expected result | Purpose |
|---|---|---|
| valid-minimal.json | Schema pass | Small structurally valid description |
| valid-multilayer-realization.json | Schema and semantic pass | One element realizes responsibilities in L3, L4 and L5 |
| invalid-missing-boundary.json | Schema fail | Required system boundary omitted |
| invalid-layer.json | Schema fail | Invalid layer identifier |
| invalid-duplicate-element-identifiers.json | Semantic fail | Duplicate element IDs across collection |
| invalid-dangling-reference.json | Semantic fail | Realization references a missing element |
| invalid-status-upgrade.json | Schema fail | Unsupported status value |

## Important note

The suite has been authored but has not yet been executed using a JSON Schema validator or semantic validator. Expected outcomes are specifications for future tests, not test results.
