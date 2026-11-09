# DUSRM Profile — Database Engine (ANANTA)

**Profile ID:** DUSRM-PROFILE-DBMS-0.1  
**Status:** Repository-informed mapping; non-normative  
**SOI:** ANANTA native database engine and embedded data platform  
**Primary source:** https://github.com/jadhavdurvesh/Ananta

## 1. Scope and boundary

ANANTA is documented as an independent native DBMS/data platform implemented in Rust, with its own engine, native storage subsystem/file format, catalog, ingestion path, AQL query language, planner, execution engine, analytics, administration APIs, and planned Studio application.

For this profile, the SOI is the native ANANTA engine and its supported embedded API. The following are treated as external or optional:
- host operating system and filesystem;
- external reference databases retained for comparisons;
- optional workload producers, including the FireBot JSONL workload;
- ANANTA Studio, which the native architecture document describes as planned and dependent on a future versioned server/management API.

## 2. Responsibility mapping

| Layer | ANANTA responsibilities | Evidence status |
|---|---|---|
| L1 Physical & Infrastructure Foundation | Host CPU, memory, filesystem and disk I/O; the architecture explicitly retains OS-provided filesystem/device I/O primitives | Documented |
| L2 Resource & Abstraction | Bounded batch output limits, execution row/cell/working-set limits, single-writer ownership and database lock boundary | Repository-reported implemented/documented; exact guarantees are limited to named APIs and tests |
| L3 Execution & Control | Pull-based vector operators; lazy AQL result iterator; cancellation token; per-operation WAL commit/recovery boundaries | Repository-reported implemented/documented |
| L4 Information & State | Typed values, schemas, stable catalog identities, immutable schema snapshots, ANF/Chronicle/Capsule/Navigation Map artifacts, WAL and checkpoints | Repository-reported implemented/documented; see individual format specifications |
| L5 Computation & Transformation | AQL lexer/parser/AST, logical plans, name/type resolution, optimizer, physical operators, aggregation and time-series analytics | Repository-reported implemented; feature scope remains experimental and incomplete |
| L6 Interaction & Coordination | Embedded Rust API; AQL client interface; database/client error and result contracts | Embedded API v0.1 is in progress; no stable live server protocol is claimed |
| L7 Capabilities & Services | Create tables, schema changes, batch ingestion, bounded scans, supported AQL execution, analytics, backup/restore, and storage inspection | Repository-reported implemented with feature-specific limits |
| L8 Application & Mission Outcomes | Independent native database/data platform; analytical and time-series workloads; optional telemetry ingestion workload | Product goal documented; FireBot connector is optional file-based JSONL |

Layer assignment is to responsibilities, not crates or folders. A Rust crate may realize responsibilities in multiple layers. This profile does not require one crate per layer.

## 3. Operational semantics relevant to this profile

### 3.1 Query and execution

The embedded API contract describes AQL execution as returning a lazy `AqlResultIter` that yields owned result batches. Dropping the iterator releases its owned scan/execution state. The legacy full-result scan remains materialising; batch APIs are the bounded-result approach.

### 3.2 Transaction boundary

The transaction/concurrency scope document describes operation-scoped atomic redo units, not a public general-purpose BEGIN/COMMIT transaction API.

The documented concurrency boundary includes:
- one exclusive writer owner process/handle;
- concurrent shared-reference read operations on the same open handle;
- no concurrent independent database writers;
- no MVCC;
- no arbitrary multi-statement atomicity, savepoints, or general ACID guarantee.

### 3.3 Durability and recovery

The WAL recovery specification describes redo for supported immutable artifact publication and specified metadata operations. It requires checksum/identity validation and fail-closed behavior for missing or conflicting committed artifacts.

This must not be generalized into an unrestricted claim of ACID semantics or universal physical power-loss immunity.

## 4. FireBot relationship

The ANANTA repository documents an optional FireBot telemetry workload that accepts a JSONL file and targets `ananta.firebot_events`.

This establishes a documented workload-adapter concept, not a live database connection or production integration. FireBot's own integration documents retain ANANTA as a separate database project and describe integration proposals separately.

The DUSRM mapping therefore records:
- **Existing documented capability:** optional file-based FireBot JSONL workload connector.
- **Planned system use:** ANANTA may provide persistence and analysis for FireBot telemetry/event data within the integrated architecture.
- **Not established:** live FireBot-to-ANANTA networking, production telemetry ingestion, latency, reliability, or hardware data integration.

## 5. Profile-specific constraints

- Do not infer transaction, isolation, MVCC, or replication guarantees beyond the named ANANTA specifications.
- Do not infer a storage algorithm from the fact that ANANTA has a native format.
- Do not treat future Studio/server capabilities as implemented.
- Do not place the optional FireBot workload inside ANANTA engine core.
- Do not require PostgreSQL or ClickHouse for native engine operation; the architecture identifies them as external reference systems.
- Keep API, AQL, format, WAL, and other ANANTA specifications authoritative for their technical details.

## 6. Validation gaps

- Execute the ANANTA repository's documented build and test procedures independently and attach results.
- Validate resource limits and cancellation behavior under representative workloads.
- Review AQL execution semantics and partial-effect behavior.
- Review recovery crash matrix evidence and platform scope.
- Confirm current status of the M7.1 embedded API contract.
- Define a specific FireBot telemetry ingestion test with representative schemas and privacy-minimized fields.
- Assess whether ANANTA's layer mapping exposes ambiguities between L3 execution, L4 state, and L5 computation.

## 7. Evidence

See [DUSRM 0.6 evidence register](../../validation/0.6-EVIDENCE-REGISTER.md) for source revisions and limitations.
