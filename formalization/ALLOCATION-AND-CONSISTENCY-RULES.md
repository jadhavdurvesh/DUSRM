# DUSRM 0.5 — Responsibility Allocation and Consistency Rules

**Document ID:** DUSRM-FRM-002  
**Status:** Formalization draft; non-normative

## 1. Problem addressed

DUSRM uses layers to group responsibilities. Whole-system components do not necessarily belong to one layer. A single engine, board, software service, or physical assembly may realize several responsibilities.

To avoid misleading one-component/one-layer mapping, DUSRM allocates **responsibilities** to layers and connects elements to the responsibilities they realize.

## 2. Allocation model

Let:
- `E` be elements;
- `P` be responsibility definitions;
- `L` be the eight core layers;
- `primaryLayer : P → L` assign each core responsibility to one primary layer;
- `realizes ⊆ E × P` connect elements to responsibilities.

The layer set associated with an element is derived:

`Layers(e) = { primaryLayer(p) | p ∈ P ∧ realizes(e,p) }`

This set may contain zero, one, or multiple layers.

## 3. Allocation rules

**AR-01 — Single primary layer per core responsibility.** A core responsibility is assigned to exactly one layer. If a responsibility genuinely spans several layers, decompose it into distinct responsibilities or model the cross-layer dependency explicitly.

**AR-02 — Many-to-many realization.** Multiple elements may realize one responsibility, and one element may realize multiple responsibilities.

**AR-03 — Responsibility evidence.** Each allocation should include a rationale and a status such as planned, specified, implemented, observed, or verified.

**AR-04 — No technology inference.** A product, programming language, repository name, or component name does not determine its layer. Map actual responsibilities.

**AR-05 — No forced allocation.** Context actors, external systems, evidence artifacts, and other elements may remain outside the layer allocation when they do not realize a responsibility inside the SOI. Their role must remain explicit.

**AR-06 — No implied dependency.** Two responsibilities being in adjacent layers does not prove that their implementation elements directly depend on one another.

**AR-07 — Explicit cross-layer links.** Any dependency, control, information flow, or resource relation across layers must be represented by a typed relationship with scope and rationale.

**AR-08 — Domain profiles.** A profile may refine a core responsibility, but the mapping back to the core responsibility must be preserved.

**AR-09 — Layer presence.** A system description can mark a layer as applicable, not applicable, not yet known, or not modeled. These are separate states.

**AR-10 — Unmapped responsibility.** If a responsibility cannot reasonably be assigned to a core layer, record it as a candidate ontology or architecture gap. Do not hide it in an arbitrary layer.

## 4. Consistency rules

- A relationship endpoint must refer to a declared element or an explicitly external participant.
- The relationship type must allow the participant kinds used.
- The scope of a relationship must include or reference its participants appropriately.
- A relationship's status must not exceed its evidence. For example, an intended integration is not observed integration.
- A state variable must have a subject and a meaning.
- A transition must have declared source and destination conditions.
- A transition guard must refer only to declared state, events, inputs, or assumptions.
- A requirement must not be marked satisfied solely because a design element exists.
- A safety claim must identify its assumptions and evidence.
- A physical effect must not be inferred from a software command or acknowledgment without appropriate observation evidence.

## 5. Cross-cutting concerns

Cross-cutting concerns are overlays over any relevant element, relationship, responsibility, operation, transition, or viewpoint. They are not layers and do not change `primaryLayer`.

Examples:
- identity and trust;
- governance and authority;
- safety, security, and assurance;
- observability and evidence;
- lifecycle and evolution;
- time, uncertainty, and resilience.

A cross-cutting concern assignment should name the specific subject and describe its impact.

## 6. Consistency review outcome

A description may be:
- **Well-formed:** passes the applicable structural checks.
- **Well-formed with warnings:** passes mandatory checks but contains unresolved assumptions, unmapped areas, or incomplete evidence.
- **Ill-formed:** violates a mandatory structural rule.
- **Not assessable:** missing required scope or source information.

These labels assess the description, not the quality or safety of the real system.
