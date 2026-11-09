# DUSRM 0.3 — Structural Candidate Evaluation

**Document ID:** DUSRM-ARCH-001  
**Status:** Research draft; non-normative  
**Version:** 0.3-draft  
**Date:** 2026-11-09

## 1. Purpose

This document compares candidate ways to organize the DUSRM ontology into a usable reference structure. The objective is not to copy OSI's seven-layer stack. The objective is to choose a structure that supports multiple engineering domains while remaining understandable, traceable, and useful in real projects.

The candidates are evaluated against the DUSRM 0.2 ontology and three different application scales:
- a small standalone application;
- ANANTA as a custom database and computational engine;
- FireBot as an integrated cyber-physical robotics system.

## 2. Design requirements

A candidate structure should:

1. Be understandable without requiring a particular implementation technology.
2. Represent both static structure and dynamic behavior.
3. Support clear responsibility boundaries.
4. Allow relationships between non-adjacent concerns.
5. Represent cross-cutting concerns such as safety, trust, governance, observability, and lifecycle.
6. Work for software-only and cyber-physical systems.
7. Support system decomposition and systems-of-systems.
8. Provide enough consistency to guide architecture descriptions and reviews.
9. Avoid duplicating APIs, protocols, modeling languages, or lifecycle standards.
10. Be testable through independent case studies.

## 3. Candidate structures

### Candidate A — Strict linear layered stack

A fixed sequence of layers is used for every system. Each layer has a well-defined responsibility and normally depends on the layer below.

**Strengths**
- Easy to explain and visualize.
- Makes responsibility boundaries visible.
- Encourages explicit interfaces between adjacent layers.
- Can guide implementation decomposition where the domain naturally has a stack.

**Weaknesses**
- May force unrelated domains into an artificial sequence.
- Cross-cutting concerns do not fit cleanly into one layer.
- Real systems often have feedback and non-adjacent dependencies.
- Components may perform responsibilities associated with several layers.
- A single universal order may conceal domain-specific differences.

**Assessment:** A useful view, but too restrictive as the only structure for a universal model.

### Candidate B — Multiple viewpoints or dimensions

The system is described through several related viewpoints, such as purpose/context, information, computation, engineering realization, behavior, or assurance. Viewpoints are not necessarily ordered as layers.

**Strengths**
- Separates concerns without implying a universal processing sequence.
- Supports independent reasoning about different aspects of a system.
- Can represent concerns that span multiple components or layers.
- Has a precedent in the Reference Model of Open Distributed Processing (RM-ODP), whose viewpoints are related but do not form a fixed sequence like protocol layers.

**Weaknesses**
- Can be less intuitive for engineers seeking a clear structural stack.
- Viewpoints may overlap unless their scope is carefully defined.
- A viewpoint set alone may not show which responsibilities provide support to others.

**Assessment:** Strong for analysis and cross-cutting concerns, but insufficient as the only organizing structure.

### Candidate C — Graph or ontology as the whole architecture

All modeled elements are nodes, and all structural, behavioral, dependency, and traceability relations are typed edges.

**Strengths**
- Expresses non-hierarchical and non-adjacent relationships.
- Supports traceability and machine-assisted validation.
- Does not force components into a single parent-child hierarchy.
- Can represent many different system domains.

**Weaknesses**
- A graph alone may not guide engineers in grouping responsibilities.
- Large graphs can become difficult to read.
- Without viewpoints or constraints, different authors may produce incompatible descriptions.

**Assessment:** Strong semantic foundation, but weak as the only human-facing reference structure.

### Candidate D — Hierarchical decomposition

A system is represented as a tree or hierarchy of systems, subsystems, components, and elements.

**Strengths**
- Intuitive for decomposition and ownership.
- Useful for systems-of-systems and hardware/software breakdowns.
- Supports allocation of requirements and responsibilities.

**Weaknesses**
- A strict tree does not naturally represent shared services, feedback, peer coordination, or many-to-many dependencies.
- Cross-cutting concerns become duplicated or hidden.
- Behavioral and temporal relationships require additional structures.

**Assessment:** Necessary as one structural view, but incomplete as the universal structure.

### Candidate E — Hybrid reference structure

A coordinated model combines:
1. A context frame for purpose, scope, boundary, and environment.
2. A graph-based ontology for elements and typed relationships.
3. A layered responsibility view for the primary architectural organization.
4. Cross-cutting concern views that apply across layers and relationships.
5. Multiple viewpoints for structural, behavioral, information, resource, interaction, and assurance analysis.

**Strengths**
- Retains the clarity of an OSI-like layered view.
- Keeps relationships that skip layers or span components explicit.
- Represents cross-cutting concerns without inventing artificial layers for each concern.
- Supports hierarchy and non-hierarchical relations simultaneously.
- Can be applied to small applications, engines, distributed systems, and robotics.

**Weaknesses**
- More complex to define and validate than a simple stack.
- Requires careful rules to prevent duplicate or contradictory descriptions.
- Conformance may be harder to assess until the semantics are formalized.

**Assessment:** Best current candidate for DUSRM, subject to validation. It is not yet approved as a final architecture.

## 4. Comparative assessment

Legend: **Strong** = naturally supported; **Moderate** = supported with extra rules; **Weak** = awkward or incomplete.

| Criterion | Strict layers | Viewpoints | Graph | Hierarchy | Hybrid |
|---|---|---|---|---|---|
| Clear responsibility grouping | Strong | Moderate | Weak | Strong | Strong |
| Non-adjacent relationships | Weak | Moderate | Strong | Weak | Strong |
| Cross-cutting concerns | Weak | Strong | Strong | Weak | Strong |
| Static and behavioral description | Moderate | Strong | Strong | Moderate | Strong |
| System decomposition | Moderate | Moderate | Strong | Strong | Strong |
| Clear human-readable stack | Strong | Weak | Weak | Moderate | Strong |
| Cross-domain flexibility | Weak | Strong | Strong | Moderate | Strong |
| Simplicity | Strong | Moderate | Moderate | Strong | Moderate |
| Potential for traceability and tooling | Moderate | Moderate | Strong | Moderate | Strong |

This is a qualitative design assessment, not a measured benchmark. The ratings are hypotheses to test, not empirical results.

## 5. Prior-art lessons

### 5.1 OSI

ISO/IEC 7498-1 defines the OSI Basic Reference Model as a common basis for coordinating standards development for systems interconnection, and explicitly states that it is not an implementation specification.

**Lesson for DUSRM:** a reference model can organize responsibilities and standards without dictating a concrete implementation. DUSRM should preserve that separation, but its domain is broader than communications.

Source: https://www.iso.org/standard/20269.html

### 5.2 RM-ODP

The RM-ODP reference model uses related viewpoints that are sufficiently independent to support reasoning, but they do not form a fixed sequence like protocol layers.

**Lesson for DUSRM:** multiple views can complement layers and should not be forced into a single ordering.

Source: https://www.itu.int/rec/T-REC-X.901-199708-I/en  
Additional text: https://www.itu.int/rec/dologin_pub.asp?id=T-REC-X.901-199708-I%21%21PDF-E&lang=e&type=items

### 5.3 ISO/IEC/IEEE 42010:2022

This standard specifies requirements for architecture descriptions and distinguishes an entity's architecture from the description expressing it.

**Lesson for DUSRM:** preserve the distinction between the SOI, its architecture, and a model or description of that architecture. DUSRM should not claim to replace an architecture-description standard.

Source: https://www.iso.org/standard/74393.html

### 5.4 ISO/IEC/IEEE 15288:2023

This standard establishes a framework of system life-cycle process descriptions and does not prescribe a specific life-cycle model or systems modeling approach.

**Lesson for DUSRM:** lifecycle processes and conceptual system structure are related but different concerns.

Source: https://www.iso.org/standard/81702.html

### 5.5 OMG SysML v2

SysML v2 is a general-purpose systems modeling language supporting requirements, structure, behavior, analysis, and verification.

**Lesson for DUSRM:** do not create another general-purpose modeling language without a demonstrated gap. DUSRM should define reference concepts and architectural responsibilities that can be represented in existing tools.

Sources:
- https://www.omg.org/sysml/sysmlv2/
- https://www.omg.org/spec/SysML/2.0/

## 6. Current recommendation

Proceed with Candidate E, the **Hybrid Reference Structure**, as the DUSRM 0.3 baseline proposal:

- A context frame defines why and within what boundary the SOI is described.
- A responsibility stack groups the system into eight broad abstraction layers.
- A typed relationship graph links elements within and across layers.
- Cross-cutting concerns apply to any relevant layer, element, relationship, or viewpoint.
- Viewpoints provide focused descriptions without creating additional layers.

The eight candidate layers are documented separately in `DUSRM-REFERENCE-STRUCTURE-0.3.md`.

## 7. Decision status

**Proposed, not frozen.** The structure must be tested against the ontology, ANANTA, FireBot, and at least one small standalone application. Any layer that cannot be mapped consistently or that duplicates another layer must be revised or removed.

A future decision record must include review evidence, unresolved limitations, and the reason for accepting or rejecting alternatives.
