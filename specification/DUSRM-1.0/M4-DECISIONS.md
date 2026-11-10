# DUSRM 1.0 Preparation — WP4 Validator and Migration Decisions

**Work package:** WP4 — Schema 0.2 Semantic Validator and Migration Tooling  
**Status:** Proposed decisions; implementation draft validated in CI  
**Date:** 2026-11-10

## 1. Decisions

| ID | Decision | Rationale | Status |
|---|---|---|---|
| WP4-D01 | Keep schema 0.2 structural validation separate from semantic validation | JSON Schema cannot resolve cross-collection references or establish semantic consistency | Implemented |
| WP4-D02 | Build deterministic indexes for every typed object collection | Supports explicit reference-kind and identifier resolution | Implemented |
| WP4-D03 | Require identifiers to be globally unique within one description | Avoids ambiguity across object namespaces and relationship endpoints | Implemented |
| WP4-D04 | Keep relationship endpoint signatures explicit and conservative | Prevents type guessing from relationship names | Implemented |
| WP4-D05 | Separate errors from warnings and preserve deterministic ordering | Allows automation while keeping incomplete evidence visible | Implemented |
| WP4-D06 | Treat profile compatibility as explicit registry data | No compatibility is inferred from similar version identifiers | Implemented |
| WP4-D07 | Make migration loss-aware and source-preserving | Prevents overwriting historical descriptions or inventing semantics | Implemented |
| WP4-D08 | Require explicit opt-in to emit an incomplete migration draft | Makes omitted/ambiguous records visible before adoption | Implemented |
| WP4-D09 | Keep the schema 0.1 validator and all historical fixtures/workflows | Preserves reproducibility and legacy compatibility | Verified in CI |
| WP4-D10 | Use the SAND OS description fixture as a DUSRM-side test only | Demonstrates cross-domain utility without changing the source OS repository | Implemented |

## 2. Decisions not made

WP4 does not make schema 0.2 stable, claim exhaustive semantic coverage, approve profiles, prove implementation conformance, automatically migrate every 0.1 description without review, or modify any downstream project repository.

## 3. Review requirements

Before 1.0 acceptance:
- review every finding code and severity;
- review false-positive/false-negative behavior using independent descriptions;
- assess the migrator against multiple real schema 0.1 files;
- independently review loss reports and status conversions;
- review whether scope containment needs stronger graph semantics;
- review profile composition and evidence-quality assessment.

## 4. Review record

No independent external review has yet been recorded. CI success is internal automated evidence, not peer approval.
