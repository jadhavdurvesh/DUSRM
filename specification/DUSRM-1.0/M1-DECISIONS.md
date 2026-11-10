# DUSRM 1.0 Preparation — WP1 Decisions and Review Record

**Work package:** WP1 — Layer Definitions and Boundaries  
**Status:** Proposed decisions; awaiting independent review  
**Date:** 2026-11-10

## 1. Decisions proposed for the 1.0 core

| ID | Proposed decision | Rationale | Status |
|---|---|---|---|
| WP1-D01 | Retain eight candidate responsibility layers for the next review cycle | Three domain descriptions can be mapped without requiring one component per layer; independent review is still needed | Proposed |
| WP1-D02 | Keep the current layer names provisionally | Existing drafts and mappings already use them; names should change only with evidence of ambiguity | Proposed |
| WP1-D03 | Make responsibility-first allocation the core allocation rule | A component can realize several responsibilities without being split | Proposed |
| WP1-D04 | Treat layer order as a reading convention, not a normative processing sequence | The 0.3 arrows risk suggesting an obligatory adjacent-layer pipeline | Proposed |
| WP1-D05 | Use explicit boundary tests for L1/L2, L2/L3, L3/L5, L4/L5, L4/L6, L6/L7, L7/L8, and L8/L3 | These were the most visible overlaps in the case studies | Proposed |
| WP1-D06 | Separate internal responsibility from external dependency | Prevents external host infrastructure or services being treated as internally realized components | Proposed |
| WP1-D07 | Keep cross-cutting concerns as scoped overlays | Safety, security, trust, evidence, time, and resilience span multiple layers | Proposed |
| WP1-D08 | Keep APIs, protocols, formats, databases, and engines independently specified | DUSRM maps their responsibilities without duplicating technical contracts | Proposed |

## 2. Decisions not made

WP1 does not decide:
- that the eight layers are complete for every possible system;
- that the current layer names are final;
- that one layer must map to one module, product, team, or deployment unit;
- that every system must instantiate all eight layers;
- that stack order defines execution flow or authority;
- that the old DUSRM 0.3 document is retroactively changed;
- that DUSRM 1.0 is stable or approved.

## 3. Review requirements

Before these decisions are accepted:
- at least one independent systems architect should review layer scope and the boundary matrix;
- a formal-methods reviewer should examine responsibility allocation and typed relationships;
- reviewers should attempt a counterexample from a domain not already used (for example, a power grid, compiler toolchain, or medical-device architecture);
- each objection should be recorded with disposition and rationale;
- the ANANTA, FireBot, and standalone mappings should be updated only after the core wording is accepted.

## 4. Review response record

No external review has been claimed or received as part of this work package.

| Reviewer | Expertise | Date | Finding | Disposition |
|---|---|---|---|---|
| Pending | Pending | Pending | No independent review recorded | Open |

## 5. WP1 completion criteria

WP1 documentation is complete when:
- eight layer definitions include purpose, scope, exclusions, and boundary test;
- all identified overlap pairs have explicit decision rules;
- external dependencies are distinguished from internal realizations;
- mappings for the three current case studies are checked against the rules;
- unresolved concerns are recorded;
- the review state remains visible and is not misrepresented as approval.
