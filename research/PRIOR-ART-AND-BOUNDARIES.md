# DUSRM Prior-Art Review and Scope Boundaries

**Status:** Initial research note  
**Last reviewed:** 2026-11-09  
**Purpose:** Identify neighboring standards and languages so DUSRM does not duplicate their scope or claim unsupported originality.

## 1. Summary

DUSRM is being explored as a cross-domain conceptual reference model for describing systems and their fundamental concepts. This is a broad and crowded research area. The current proposal is not yet proven novel.

The most important neighboring work includes:
- OSI Basic Reference Model: a reference model focused on open-systems interconnection and communication-layer organization.
- ISO/IEC/IEEE 15288: a framework of system life-cycle process descriptions.
- ISO/IEC/IEEE 42010: requirements for architecture descriptions and their frameworks, viewpoints, and model kinds.
- OMG SysML v2: a general-purpose systems modeling language for specifying, analyzing, designing, and verifying complex systems.

DUSRM must define a distinct scope and show practical value beyond a renamed combination of these works.

## 2. Neighboring work

### 2.1 OSI — ISO/IEC 7498-1:1994

Official source: https://www.iso.org/standard/20269.html

The ISO catalogue describes ISO/IEC 7498-1 as the Basic Reference Model for Open Systems Interconnection. Its stated role is to provide a common basis for coordinating standards development for systems interconnection, and it is not intended to be an implementation specification.

**Implication for DUSRM:** OSI demonstrates how a focused reference model can organize one technical domain. DUSRM has a broader intended subject scope, so it must not merely reproduce the seven networking layers under new names. Its own structural form must be justified by its purpose and validation.

### 2.2 ISO/IEC/IEEE 15288:2023

Official source: https://www.iso.org/standard/81702.html

The standard establishes a common framework of process descriptions for the life cycle of human-created systems. It covers processes applicable to systems, system elements, and systems of systems throughout life-cycle stages.

**Implication for DUSRM:** DUSRM should not become a replacement life-cycle process framework. It may describe system concepts and support mappings to life-cycle artifacts, but process requirements and process implementation remain within their appropriate standards and methods.

### 2.3 ISO/IEC/IEEE 42010:2022

Official source: https://www.iso.org/standard/74393.html

The standard specifies requirements for the structure and expression of architecture descriptions. It distinguishes an entity's architecture from an architecture description that expresses it, and addresses architecture-description frameworks, languages, viewpoints, and model kinds.

**Implication for DUSRM:** DUSRM must preserve the distinction between the system being described and the description/model of that system. It should not claim to replace an architecture-description standard. Its ontology may be used within architecture descriptions where appropriate.

### 2.4 OMG SysML v2

Official sources:
- https://www.omg.org/sysml/
- https://www.omg.org/spec/SysML

OMG describes SysML as a general-purpose systems modeling language used to specify, analyze, design, and verify complex systems including hardware, software, information, personnel, procedures, and facilities. The official specification history identifies SysML v2.0 as adopted in September 2025.

**Implication for DUSRM:** DUSRM should not become another general-purpose modeling language. It may define conceptual categories and relationships that can be represented using SysML or other tools. Any proposed DUSRM-specific notation should remain optional until a clear need is demonstrated.

## 3. Preliminary boundary statement

| Area | DUSRM position |
|---|---|
| System concepts and ontology | Primary research scope |
| Cross-domain system reference model | Primary research scope |
| Layered architecture | Candidate structure; not assumed |
| Architecture description framework | Neighboring scope; avoid replacement claims |
| System life-cycle processes | Neighboring scope; map where useful |
| Systems modeling language | Neighboring scope; do not duplicate without a demonstrated gap |
| APIs, protocols, serialization, runtimes | Out of scope; remain separate technologies |
| Implementation guidance | Possible informative application, not the core model |

## 4. Research gaps to investigate

The current research has not yet established a unique gap. Candidate questions:

1. Can one compact ontology describe both software-only and cyber-physical systems without forcing either into domain-specific terms?
2. Can DUSRM provide stable system-level concepts while allowing multiple structural views (layered, graph, hierarchical, federated, or hybrid)?
3. Can the same ontology support both design-time descriptions and runtime observations without confusing the two?
4. Can DUSRM describe systems of systems, partial autonomy, changing boundaries, and uncertain knowledge consistently?
5. Does DUSRM provide a useful bridge between conceptual architecture and practical system validation without duplicating SysML or ISO/IEC/IEEE 42010?

A research gap is established only when supported by a systematic comparison and concrete use cases.

## 5. Sources and review notes

- ISO. ISO/IEC 7498-1:1994, Basic Reference Model: https://www.iso.org/standard/20269.html
- ISO. ISO/IEC/IEEE 15288:2023, System life cycle processes: https://www.iso.org/standard/81702.html
- ISO. ISO/IEC/IEEE 42010:2022, Architecture description: https://www.iso.org/standard/74393.html
- Object Management Group. Systems Modeling Language (SysML): https://www.omg.org/sysml/
- Object Management Group. SysML specification: https://www.omg.org/spec/SysML

Only public scope descriptions and catalogue information were reviewed for this note. This is not a substitute for reviewing the full copyrighted normative texts, nor does it claim a complete literature survey.
