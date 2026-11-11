# DUSRM 1.0 Preparation — WP6 Standards Crosswalk

**Purpose:** identify adjacent architecture and systems-engineering standards so DUSRM complements existing practice instead of claiming to replace it.  
**Review date:** 2026-11-11

## 1. Standards and adjacent frameworks

| Reference | Primary concern | Relationship to DUSRM | SAND OS use |
|---|---|---|---|
| ISO/IEC/IEEE 42010:2022 | Structure and expression of architecture descriptions, viewpoints and architecture-description frameworks/languages | DUSRM can supply a reusable responsibility/reference-model view; it should not claim to replace a conforming architecture description framework or viewpoint model | Use SAND documentation and viewpoints as authoritative architecture descriptions; link DUSRM descriptions to them |
| ISO/IEC/IEEE 15288:2023 | System life-cycle process descriptions across conception, development, production, utilization, support and retirement | DUSRM describes architecture responsibilities and relationships; 15288 addresses processes across the system life cycle | Map SAND engineering milestones, verification and maintenance obligations to lifecycle processes where useful |
| OMG SysML v2.0 / KerML 1.0 | Formal systems modeling language and semantic foundation, including structure, behavior, requirements, analysis and verification | SysML v2 is a modeling language; DUSRM is a reference model and architecture-description vocabulary. DUSRM should be mappable to/from modeling artifacts rather than compete as another language | Use SysML/KerML where SAND needs detailed executable/system models; use DUSRM for cross-domain responsibility/layer mapping and evidence traceability |

## 2. Key distinctions

### 2.1 Architecture description is not the architecture itself

ISO/IEC/IEEE 42010:2022 explicitly distinguishes the architecture of an entity of interest from an architecture description that expresses that architecture. DUSRM should retain its own distinction between the system-of-interest and the description object and ensure DUSRM JSON files remain descriptions, not the system.

### 2.2 Lifecycle processes are not architecture layers

ISO/IEC/IEEE 15288:2023 establishes a common framework of system life-cycle process descriptions and does not prescribe one life-cycle model or modeling language. DUSRM responsibility layers must not be presented as a sequence of project phases or a replacement for lifecycle processes.

### 2.3 A modeling language is not a reference model

OMG describes SysML as a general-purpose graphical/textual modeling language for specifying, analyzing, designing and verifying complex systems. SysML v2 is grounded in KerML and has a standardized API/interchange model. DUSRM should not introduce a competing syntax or claim equivalent modeling-language semantics. Its schema 0.2 is a typed interchange description for DUSRM concepts, not a full systems modeling language.

## 3. Crosswalk implications for DUSRM

- Keep the eight layers as responsibility categories; do not equate them with ISO process groups or SysML package/diagram kinds.
- Keep architecture viewpoints and stakeholder concerns explicit; DUSRM's profile and context data should link to the views required by the selected architecture-description approach.
- Keep system life-cycle status/evidence distinct from architectural realization state.
- Provide traceability links to SysML/KerML or other models rather than re-encoding all of their semantics.
- Do not claim conformance to ISO/IEC/IEEE 42010 or 15288 merely because DUSRM includes architecture, lifecycle or evidence fields.

## 4. Primary references

1. [ISO/IEC/IEEE 42010:2022 — Software, systems and enterprise — Architecture description](https://www.iso.org/standard/74393.html). ISO's published summary states that the standard specifies requirements for the structure and expression of architecture descriptions for software, systems, enterprises and other entities, and distinguishes architecture from its description.
2. [ISO/IEC/IEEE 15288:2023 — Systems and software engineering — System life cycle processes](https://www.iso.org/standard/81702.html). ISO's published summary describes a common framework of process descriptions covering full system life cycle; it does not prescribe a specific life-cycle model or modeling language.
3. [OMG SysML v2.0 specification](https://www.omg.org/spec/SysML/2.0). OMG lists the formal SysML 2.0 specification and machine-readable model artifacts, including the SysML abstract-syntax JSON schema.
4. [OMG SysML overview](https://www.omg.org/sysml/). OMG describes SysML as a general-purpose modeling language for complex systems and identifies the SysML v2.0 adoption.

This crosswalk is an initial public-summary review, not a clause-by-clause standards compliance assessment. Full standards texts may be copyrighted and are not reproduced here.
