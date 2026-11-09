# ANANTA — DUSRM 0.3 Exploratory Mapping

**Status:** Preliminary; repository audit required  
**Purpose:** Test DUSRM's structure against an independently developed database and computational engine.

## 1. Scope

ANANTA is treated as a system of interest in its own right. This mapping does not assume the same scope as an application that embeds or accesses ANANTA.

Known project-level context: ANANTA is being developed as a custom database/data engine with its own engine and query language. This document does not infer its internal storage model, transaction semantics, execution pipeline, or resource manager.

## 2. Candidate layer mapping

| Layer | Candidate ANANTA concern | Status |
|---|---|---|
| L8 — Application & Mission Outcomes | Database use cases, user workflows, workloads, and desired outcomes | Broad purpose known; exact workflows need audit |
| L7 — Capabilities & Services | Database operations and capabilities ANANTA exposes | Needs specification audit |
| L6 — Interaction & Coordination | Client, engine, subsystem, and external integration interfaces | Needs repository/specification audit |
| L5 — Computation & Transformation | Query-language semantics and computational operations | Custom engine and query language known; implementation details need audit |
| L4 — Information & State | Data identity, schema, values, state, persistence semantics | Needs specification audit |
| L3 — Execution & Control | Operation lifecycle, scheduling, concurrency, transactions, recovery | Unknown until inspected |
| L2 — Resource & Abstraction | Memory, storage, CPU, caching, resource allocation | Unknown until inspected |
| L1 — Physical & Infrastructure | Supported host platforms and physical/virtual deployment resources | Deployment-specific; needs audit |

## 3. DUSRM questions raised by ANANTA

- Does the model distinguish query semantics (L5) from execution behavior (L3)?
- Does it distinguish the meaning of data and database state (L4) from physical storage (L1/L2)?
- Can an engine component implement responsibilities in more than one layer?
- Can client interfaces be described at L6 while exposed capabilities are described at L7?
- Can DUSRM describe ANANTA without requiring any particular API, protocol, storage engine, or query language?

## 4. DMJ ecosystem boundary

ANANTA may be integrated with other DMJ technologies in other systems, including FireBot. DUSRM must describe the integration relationships without redefining those technologies.

Before marking mappings as verified, inspect:
- ANANTA's current README and architecture documentation;
- query language specification;
- engine module boundaries;
- persistence and data model documentation;
- transaction/concurrency/recovery documentation, if present;
- resource and deployment requirements;
- existing integration specifications.

## 5. Unknowns that must remain unknown

Do not claim that ANANTA uses a particular WAL, B-tree, LSM-tree, MVCC model, lock manager, transaction isolation level, query optimizer, scheduler, or storage format unless the current repository or specification proves it.

## 6. Outcome

ANANTA appears to be a useful software-engine case study for separating computation, state, execution, resources, and service boundaries. The structural fit remains provisional until repository-level evidence is collected.
