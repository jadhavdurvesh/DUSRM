# DUSRM 0.7 — Independent Engineering Review Package

**Status:** Review request draft; not yet externally reviewed  
**Review target:** DUSRM core 0.1–0.7 drafts, focusing on ontology, hybrid structure, operational semantics, formalization, profiles and schema proposal.

## 1. Purpose

Request independent technical feedback on whether DUSRM is conceptually coherent, sufficiently distinct from neighboring standards and modeling approaches, and useful as a cross-domain reference model.

The review should challenge the model, not merely approve the current design.

## 2. Review scope

Reviewers are invited to assess:
- ontology clarity and completeness;
- distinction between system of interest, architecture and system description;
- validity and usefulness of the eight responsibility layers;
- whether responsibility-based allocation is well-defined;
- operational semantics and transition-system abstraction;
- relationship catalogue and cross-layer rules;
- profile compatibility and extension mechanisms;
- JSON Schema boundaries and semantic-validator requirements;
- usefulness across standalone software, database engines and cyber-physical robotics;
- overlap with OSI, RM-ODP, ISO/IEC/IEEE 15288, ISO/IEC/IEEE 42010, SysML v2/KerML, TLA+ and Alloy.

## 3. Questions for reviewers

1. Is DUSRM's scope sufficiently distinct from existing systems architecture, modeling and life-cycle standards?
2. Is a universal eight-layer responsibility model defensible, or should it be changed or rejected?
3. Are L3 Execution, L4 Information/State and L5 Computation distinct enough in real systems?
4. Is L6 Interaction/Coordination too broad?
5. Are L7 Capabilities/Services and L8 Application/Mission Outcomes clearly separated?
6. Does the model represent software-only, database, distributed and cyber-physical systems without forced mappings?
7. Are responsibility allocation and cross-cutting concerns semantically consistent?
8. Are operational semantics precise enough to be useful without becoming a new modeling language?
9. Does the schema preserve semantic distinctions, or does it overfit current examples?
10. What concepts, rules or assumptions should be removed, added or rewritten?

## 4. Review materials

- README and versioned specifications in this repository.
- 0.2 ontology and relationship catalogue.
- 0.3 structural candidates and reference structure.
- 0.4 operational semantics and formal kernel.
- 0.5 formal metamodel and allocation rules.
- 0.6 validation method, case studies and evidence register.
- 0.7 schema, profile compatibility policy, consistency checks and fixtures.

## 5. Review response template

- Reviewer name/role (optional if anonymous):
- Relevant expertise:
- Date:
- Documents and versions reviewed:
- Overall assessment: coherent / partly coherent / not coherent / insufficient information
- Major findings:
- Minor findings:
- Prior-art or overlap concerns:
- Suggested changes to core ontology:
- Suggested changes to layer structure:
- Suggested changes to operational semantics:
- Suggested changes to profiles/schema/conformance:
- Example that DUSRM cannot represent adequately:
- Recommendation: continue / revise substantially / narrow scope / discontinue

## 6. Review integrity

- No review is claimed until a reviewer responds and the response is recorded with permission.
- A review response is not an endorsement unless the reviewer explicitly states that.
- Disagreements and negative findings must be preserved, not edited away.
- The review must identify the exact draft versions considered.

## 7. Current project position

DUSRM remains a research proposal. Its layer structure, terminology, semantics, schema, and conformance rules are provisional. This package exists to invite independent scrutiny before any stable standard or implementation is claimed.
