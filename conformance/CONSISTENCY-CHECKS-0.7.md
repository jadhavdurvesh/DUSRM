# DUSRM 0.7 — Consistency Check Catalogue

**Status:** Proposal; non-normative  
**Purpose:** Define checks that a future validator and human reviewer can apply to a DUSRM description.

## 1. Check classes

- **S — Schema:** can be checked using the JSON Schema structure.
- **M — Model semantics:** requires cross-reference or semantic logic.
- **P — Profile:** requires profile registry and compatibility information.
- **E — Evidence:** requires provenance and evidence assessment.
- **H — Human review:** requires engineering judgement or domain expertise.

## 2. Core checks

| ID | Class | Severity | Check | Expected result |
|---|---|---|---|---|
| DUSRM-S-001 | S | Error | Required top-level fields exist | Description validates against declared schema version |
| DUSRM-S-002 | S | Error | Field types and enumerations are valid | No invalid structural field values |
| DUSRM-M-001 | M | Error | Identifiers are unique within each namespace | No duplicate IDs in elements, responsibilities, relationships, operations, states, transitions or evidence |
| DUSRM-M-002 | M | Error | All references resolve | Every reference resolves to a declared object or explicit external reference |
| DUSRM-M-003 | M | Error | Realizations resolve | Every realization links a declared element and responsibility |
| DUSRM-M-004 | M | Error | Core responsibility layer assignment | Every core responsibility has exactly one primary layer |
| DUSRM-M-005 | M | Error | Many-to-many realization | One element may realize responsibilities in several layers |
| DUSRM-M-006 | M | Error | Relationship signatures | Source and target kinds are valid for the relationship type |
| DUSRM-M-007 | M | Error | Relationship scope | Endpoints belong to or are explicitly external to the stated scope |
| DUSRM-M-008 | M | Error | Operation owners | Every operation owner reference resolves |
| DUSRM-M-009 | M | Error | State-variable subjects | Every state owner reference resolves |
| DUSRM-M-010 | M | Error | Transition state references | Transition endpoints refer to declared states or permitted literals |
| DUSRM-M-011 | M | Error | Evidence references | Every evidence reference resolves |
| DUSRM-M-012 | M | Warning | Unmapped responsibilities | Candidate gaps are recorded, not silently assigned |
| DUSRM-P-001 | P | Error | Core/profile compatibility | Selected profiles explicitly support the declared core version |
| DUSRM-P-002 | P | Error | Namespaced extensions | Extensions do not silently redefine core concepts |
| DUSRM-P-003 | P | Error | Profile composition | No unacknowledged contradictory profile rules |
| DUSRM-E-001 | E | Error | Verified-claim support | Verified claims cite a criterion, method and evidence |
| DUSRM-E-002 | E | Warning | Evidence revision | Evidence can be traced to a source revision or observation context |
| DUSRM-E-003 | E | Error | Status promotion | Planned/simulated states are not promoted without evidence |
| DUSRM-E-004 | E | Warning | Documentation versus execution | Repository documentation is not reported as independent test execution |
| DUSRM-H-001 | H | Review | System boundary | Reviewer assesses whether relevant external dependencies are included |
| DUSRM-H-002 | H | Review | Layer responsibility allocation | Reviewer checks responsibility definitions and rationale |
| DUSRM-H-003 | H | Review | Safety/security scope | Claims are referred to appropriate domain-specific assurance |
| DUSRM-H-004 | H | Review | Implementation independence | No accidental duplication of an API, protocol, engine, or standard |

## 3. Severity

- **Error:** blocks a pass at the applicable conformance level.
- **Warning:** does not alone block a pass, but must be disclosed.
- **Review:** requires a recorded human judgement; JSON Schema alone cannot decide it.

## 4. Validator stages

A future validator should:
1. parse JSON and report syntax errors;
2. validate against the selected JSON Schema version;
3. validate uniqueness and cross-references;
4. validate responsibility allocation and relationship signatures;
5. validate profile compatibility and extension rules;
6. validate evidence status and traceability consistency;
7. produce machine findings and human-review items.

The validator must not report overall DUSRM conformance solely from successful schema validation.

## 5. Determinism and reproducibility

The same description, schema, profile registry, and validator version should produce the same machine-checkable findings. Human-review outcomes must be recorded separately with reviewer role, date, rationale, and evidence.
