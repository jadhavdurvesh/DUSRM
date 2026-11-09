# DUSRM Profile Compatibility Policy

**Status:** Proposal; non-normative  
**Applies to:** DUSRM core 0.7-draft and later versioned releases

## 1. Purpose

This policy defines how domain profiles specialize DUSRM without silently changing the meaning of core concepts or creating incompatible profile combinations.

## 2. Profile identity

Every profile must publish:
- stable profile identifier;
- profile version;
- compatible DUSRM core version range or exact draft identifier;
- profile status (draft, reviewed, approved within project, deprecated);
- owner/maintainer;
- scope and exclusions;
- required and optional concepts;
- required and optional layer responsibilities;
- profile-specific relationship and operational rules;
- conformance requirements and allowed omissions;
- migration notes where applicable.

## 3. Core compatibility rules

**PC-01 — No silent core redefinition.** A profile must not change the meaning of a core term, layer, relationship, or status.

**PC-02 — Explicit refinement.** A profile may refine a core responsibility by adding narrower domain responsibilities. Every refinement must identify its parent core responsibility.

**PC-03 — Explicit extension.** A concept that has no suitable core mapping must be declared as a profile extension, not disguised as a core concept.

**PC-04 — Traceable allocation.** Profile responsibilities must map to one primary core layer or be explicitly marked as a profile-only concern with rationale.

**PC-05 — Preserve evidence status.** A profile cannot promote planned, simulated, documented, or assumed claims to implemented, tested, observed, or verified without new evidence.

**PC-06 — Preserve technology neutrality.** A profile may describe use of technologies but must not require a particular DMJ project or vendor implementation in order to conform to the core.

**PC-07 — Version declaration.** Every system description must identify the exact DUSRM core version and all profile versions used.

**PC-08 — No ambiguous profile composition.** When two profiles define overlapping concepts or conflicting rules, the description must declare a resolution or be reported as incompatible/not assessable.

**PC-09 — Profile-local constraints.** A profile may add stricter domain rules, but must identify them as profile requirements rather than universal DUSRM rules.

**PC-10 — Deprecation and migration.** Removed or changed profile concepts require a migration note and a compatibility statement.

## 4. Version policy before 1.0

While DUSRM remains at 0.x:
- every published draft is a potentially breaking research revision;
- profile compatibility must use an exact core draft version unless an explicit compatibility statement exists;
- no automatic compatibility should be inferred from similar version numbers;
- schema and profile versioning are independent of DUSRM conceptual versioning.

## 5. Version policy after a stable 1.0

A future stable release may adopt semantic versioning for the core:
- major: incompatible changes to core concepts, rules, or required description structure;
- minor: backward-compatible additions and clarifications;
- patch: editorial corrections and non-semantic fixes.

This policy is a proposal and is not active until a stable release process is adopted.

## 6. Profile combination

A description using multiple profiles should include a compatibility declaration for every pair of profiles that interact. Where there is no interaction, record that fact. Profile combination must not result in duplicate identifiers, conflicting primary-layer assignments, incompatible status definitions, or contradictory constraints.

## 7. Conformance boundary

Profile conformance assesses the description against the selected profile. It does not establish safety certification, legal compliance, or fitness for purpose.
