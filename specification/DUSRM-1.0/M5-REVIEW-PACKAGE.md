# DUSRM 1.0 Preparation — WP5 Independent Reviewer Package

**Status:** Ready for external technical review; no external findings recorded  
**Assessment target:** DUSRM 1.0-preparation/schema 0.2-draft

## 1. Review objectives

Reviewers are asked to evaluate:
1. whether each profile preserves core term and layer meanings;
2. whether profile-local concepts are true refinements/extensions rather than core redefinitions;
3. whether typed schema 0.2 fixtures represent the selected domain concepts accurately;
4. whether source evidence and maturity statements are current and properly qualified;
5. whether semantic validator checks are appropriate, missing or overreaching;
6. whether the unresolved source conflicts or profile composition gaps block compatibility.

## 2. Review materials

- [DUSRM core ontology WP2](M2-ONTOLOGY-CORE.md)
- [Relationship matrix WP2](M2-RELATIONSHIP-MATRIX.md)
- [Schema design WP3](M3-SCHEMA-DESIGN.md)
- [Semantic validator WP4](M4-SEMANTIC-VALIDATOR.md)
- [WP5 reconciliation report](M5-RECONCILIATION.md)
- [WP5 compatibility matrix](M5-COMPATIBILITY-MATRIX.md)
- [WP5 reviewer cases](M5-REVIEW-CASES.md)
- [WP5 evidence snapshot](M5-EVIDENCE-SNAPSHOT.md)
- [WP5 decision record](M5-DECISIONS.md)
- [Profile fixtures](../../schema/fixtures/0.2/profiles/)

## 3. Required reviewer expertise

| Review area | Requested expertise |
|---|---|
| Core ontology and layer semantics | Systems architecture / reference model design |
| JSON Schema and semantic validation | JSON Schema Draft 2020-12, typed graph validation, validator design |
| Database engine profile | Storage engines, WAL/recovery, database concurrency and APIs |
| Cyber-physical robotics profile | Robotics systems, control/safety boundaries, evidence maturity |
| Evidence and conformance governance | Verification, traceability, configuration/change control |

A single reviewer need not cover every area. Findings should identify the expertise and scope of each review.

## 4. Required disposition format

For every finding, record:
- finding ID and affected file/section;
- severity: blocker, major, minor or observation;
- rationale and supporting evidence;
- expected correction or explicit rationale for no change;
- reviewer and date;
- owner and target revision;
- closure evidence and disposition.

## 5. Open issues for reviewers

- WP5-O01: Are the eight layer definitions unambiguous enough across all three profiles?
- WP5-O02: Are profile responsibility refinements and parent-core links sufficiently explicit?
- WP5-O03: Should profile-specific measurement/freshness/safety concepts become typed core objects, or remain versioned profile extensions?
- WP5-O04: Is the semantic validator's current scope and severity taxonomy appropriate?
- WP5-O05: Does the ANANTA documentation conflict on Windows checkpoint rotation require an explicit compatibility blocker until the source documents are synchronized?
- WP5-O06: Is FireBot's 2026-10-11 status snapshot sufficiently current for review, or must a new source status be captured first?
- WP5-O07: What minimum evidence is needed before a profile may move from not-assessed to compatible?
- WP5-O08: Should profile composition have a separate pairwise compatibility matrix and machine-readable declaration?
- WP5-O09: Is the standalone application profile useful as an illustrative scale-down case without an implementation source?

## 6. Review status

No independent reviewer findings have yet been received. The package is prepared for review but must not be described as independently reviewed or approved.
