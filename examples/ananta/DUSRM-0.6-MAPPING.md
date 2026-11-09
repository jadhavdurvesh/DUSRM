# ANANTA — DUSRM 0.6 Validation Mapping

**SOI:** Native ANANTA engine and embedded database platform  
**Profile:** DUSRM-PROFILE-DBMS-0.1  
**Status:** Repository-informed mapping; implementation was not executed as part of this DUSRM exercise

## 1. Evidence baseline

Primary repository: https://github.com/jadhavdurvesh/Ananta

Inspected documents:
- README.md
- docs/architecture/native-engine.md
- docs/specifications/transaction-concurrency-m6-v0.1.md
- docs/specifications/wal-recovery-v0.1.md
- docs/specifications/embedded-api-m7-v0.1.md
- workloads/firebot/README.md

Exact file revisions are listed in the DUSRM 0.6 evidence register.

## 2. System boundary

The SOI is the native ANANTA Rust engine and embedded API. Host filesystem/device I/O are external platform services. External reference databases are not engine dependencies. Studio is a planned client of a future versioned server/management API. FireBot is an optional workload producer, not part of ANANTA engine core.

## 3. Responsibility-to-layer mapping

| Responsibility | Layer | Repository evidence | Status |
|---|---|---|---|
| Native database lifecycle and host integration | L1/L3 | Native architecture; embedded engine docs | Documented |
| Execution budgets, bounded result batches, row/cell/working-set limits | L2 | README and embedded API contract | Repository-reported implemented/documented |
| Exclusive writer and shared-reference readers on one handle | L2/L3 | Transaction/concurrency scope | Documented; guarantees limited to that contract |
| Pull-based vector operators and AQL result iteration | L3 | README and embedded API contract | Repository-reported implemented |
| Typed values, schemas, catalog identity and immutable snapshots | L4 | README and native architecture | Repository-reported implemented |
| ANF, Chronicle, Capsule, Navigation Map and WAL/checkpoint artifacts | L4 | Native specifications and WAL recovery | Repository-reported implemented/documented with artifact-specific boundaries |
| AQL parsing, AST, planning, name/type resolution, optimization | L5 | README and native architecture | Repository-reported implemented with feature limitations |
| Vectorized execution, analytics and time-series operations | L5 | README | Repository-reported implemented with feature limitations |
| Embedded API and AQL client interaction | L6 | Embedded API contract | API v0.1 status: M7.1 in progress |
| Database operations and analytical capabilities | L7 | README and embedded API contract | Repository-reported implemented with stated limitations |
| Independent native DBMS and optional data platform workloads | L8 | README and product vision | Product objective documented |

## 4. Operational behavior mapped to DUSRM

### Query execution

The embedded API contract describes AQL execution returning a lazy `AqlResultIter` yielding owned result batches. Dropping the iterator releases its owned scan/execution state. This maps to:
- L5: query meaning, plan and computation;
- L3: execution occurrence and iterator lifecycle;
- L4: data/state read by the query;
- L2: bounded batch/resource options;
- L6/L7: embedded interface and exposed database capability.

### Transactions and concurrency

The inspected transaction/concurrency document describes operation-scoped atomic redo units, one exclusive writer, and shared-reference read operations on the same database handle. It explicitly excludes general multi-operation ACID transactions and MVCC.

DUSRM preserves these constraints rather than collapsing them into an unqualified transaction or concurrency guarantee.

### Recovery

The WAL document describes redo for supported immutable artifacts and specified metadata operations. Recovery validates identity/length/checksum and fails closed for missing or conflicting committed artifacts. These semantics map to L3 execution/recovery, L4 durable state, and cross-cutting integrity/assurance.

They do not establish general undo/redo for arbitrary mutations or physical power-loss immunity on every device/filesystem.

## 5. FireBot data integration mapping

ANANTA's `workloads/firebot/README.md` documents an optional command-line workload:
`python connector.py --file firebot_events.jsonl`
targeting `ananta.firebot_events`.

DUSRM classification:
- The file-based JSONL adapter is documented.
- The adapter is optional to ANANTA engine operation.
- It can be used to exercise telemetry ingestion and analytics.
- It does not establish live FireBot-to-ANANTA networking or production integration.
- An end-to-end integration profile requires an agreed event schema, privacy/minimization policy, provenance, timestamp/freshness rules, retry/deduplication policy, and reproducible workload evidence.

## 6. Model validation result

**Preliminary pass with findings** for descriptive layer coverage.

Findings:
- Responsibility allocation works for a native database engine.
- L3/L4/L5 must remain separate: execution, data state, and computational semantics.
- L2 resource limits should be specified as constraints, not assumed as a universal resource-management subsystem.
- L6 should accommodate an embedded API without requiring a network server.
- The optional FireBot workload proves an offline/file-based integration seam, not live system integration.

## 7. Remaining verification actions

- Run `cargo fmt --all`, `cargo test --workspace`, and `cargo clippy --workspace --all-targets` in the intended ANANTA environment, recording actual outcomes.
- Select and run representative AQL, cancellation, bounded scan, WAL recovery, and crash-boundary tests.
- Inspect the implementation for the relevant API behavior rather than relying only on documentation.
- Run the FireBot JSONL connector with a small deterministic fixture and record the output and schema.
- Verify the current embedded API M7.1 status and version.

No tests were executed in this DUSRM validation exercise.
