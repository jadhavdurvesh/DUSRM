# DUSRM 1.0 Preparation — WP5 Evidence Snapshot

**Status:** Read-only repository evidence snapshot  
**Inspection date:** 2026-11-11  
**Purpose:** Support profile reconciliation; not independent implementation verification

## 1. DUSRM snapshot

- Repository: `jadhavdurvesh/DUSRM`
- Branch: `main`
- Tree snapshot before WP5 profile fixture additions: `221d36f53248bdff0d28204bce2a7ebb629fbf5e`
- Schema: `schema/dusrm-description-0.2.schema.json`
- Semantic validator: `scripts/validate_semantics_0_2.py`
- Profile registry: `profiles/registry.json`

## 2. ANANTA snapshot

- Repository: `jadhavdurvesh/Ananta`
- Default branch: `main`
- Tree snapshot: `4a46151f4b60aa8a2a9c455ed6f3418c9d2c97ef`

| Source | Blob SHA | Used for | Limitation |
|---|---|---|---|
| [README.md](https://github.com/jadhavdurvesh/Ananta/blob/main/README.md) | `ca138eee12f6bb55de058378c96f2c1396503b66` | Native Rust DBMS scope, feature maturity and explicit unsupported guarantees | Repository report; not independently built/tested by WP5 |
| [native-engine.md](https://github.com/jadhavdurvesh/Ananta/blob/main/docs/architecture/native-engine.md) | `64d1768f89593c5090e6e087cdbb9a103ce64b3c` | Engine subsystem ownership and host/database boundaries | Architecture description, not proof every capability is complete |
| [transaction-concurrency-m6-v0.1.md](https://github.com/jadhavdurvesh/Ananta/blob/main/docs/specifications/transaction-concurrency-m6-v0.1.md) | `0d16617ba745609407224668ed68bfb68fb891fc` | Exclusive writer, same-handle readers, operation-scoped atomic redo units, no general ACID/MVCC | Conflicts with newer README on Windows checkpoint rotation |
| [wal-recovery-v0.1.md](https://github.com/jadhavdurvesh/Ananta/blob/main/docs/specifications/wal-recovery-v0.1.md) | `c0b024cdc427d0a9cb010b29ff2d3ea7522079f1` | Supported redo/recovery boundary and fail-closed rules | Contains older Unix-only checkpoint rotation wording |
| [embedded-api-m7-v0.1.md](https://github.com/jadhavdurvesh/Ananta/blob/main/docs/specifications/embedded-api-m7-v0.1.md) | `0719b79f17ccdcc11932402ba2059020b817a2b4` | Embedded API v0.1, lazy result iterator, owned batches, typed errors, budgets/cancellation | M7.1 remains in progress; not a stable network API |
| [workloads/firebot/README.md](https://github.com/jadhavdurvesh/Ananta/blob/main/workloads/firebot/README.md) | `dd3a35c7c71e58dda49876b00fb95838e41668e8` | File-based JSONL FireBot workload to `ananta.firebot_events` | No live FireBot network/database integration implied |

### ANANTA conflict

The inspected README states Windows checkpoint replacement uses `MoveFileExW(REPLACE_EXISTING | WRITE_THROUGH)` and a targeted Windows CI job. The transaction/concurrency specification states checkpoint rotation is Unix-only, while the WAL specification says atomic replacement is unsupported on non-Unix platforms. This discrepancy remains open until ANANTA's authoritative source documents are reconciled. No DUSRM compatibility decision depends on guessing the answer.

## 3. FireBot snapshot

- Repository: `jadhavdurvesh/firebot-core`
- Default branch: `main`
- Tree snapshot: `c99fc963057393f3ed14060a9294c719910087de`

| Source | Blob SHA | Used for | Limitation |
|---|---|---|---|
| [README.md](https://github.com/jadhavdurvesh/firebot-core/blob/main/README.md) | `bce2a47acea1c98f972aaba039f2c8201259f2e7` | System intent and software-first development principle | Project intentions, not hardware implementation |
| [CURRENT_STATE.md](https://github.com/jadhavdurvesh/firebot-core/blob/main/CURRENT_STATE.md) | `a5ff1a658cb025c38d88e33d24b5d669f4dc659e` | Snapshot dated 2026-10-11; physical hardware, tests and deployment maturity boundaries | Snapshot may be superseded; refresh before compatibility approval |
| [ARCHITECTURE.md](https://github.com/jadhavdurvesh/firebot-core/blob/main/ARCHITECTURE.md) | `b4044ffa60ed2f18cd7f6acb17bfad0454f29dfb` | Software/simulation/physical platform separation and people-first intent | Intended architecture; no physical safety proof |
| [STATUS.md](https://github.com/jadhavdurvesh/firebot-core/blob/main/STATUS.md) | `834d2b20e3457a0649f212800f257b2cd74e7a48` | Code-present, simulated, planned and unverified status language | Repository status record, not independent execution |
| [INTERFACES.md](https://github.com/jadhavdurvesh/firebot-core/blob/main/INTERFACES.md) | `953989c71eedb7bf2ff321305fd2667bfe8243f3` | Message contracts and provenance/freshness conventions | Does not prove live physical connectivity |
| [DMJ_SYSTEMS_INTEGRATION.md](https://github.com/jadhavdurvesh/firebot-core/blob/main/DMJ_SYSTEMS_INTEGRATION.md) | `175eb0a6e1cc6f25a24a800318a0d06c37ec31cd` | Proposed CONTRACT/OCTET/DATAGRAM/CALLGRAPH placement and local safety independence | Proposed/documentation-only integration |
| [TECHNOLOGY_INTEGRATION.md](https://github.com/jadhavdurvesh/firebot-core/blob/main/TECHNOLOGY_INTEGRATION.md) | `a05311fb2604bd0463d3d09db9847e3cea524478` | Proposed candidate technology boundaries and safety constraints | Not approved as implementation baseline |

## 4. Standalone application basis

The standalone task-list profile is an illustrative architecture exercise from the DUSRM 0.6 profile. It is not derived from a specific deployed application or independent test result. The WP5 schema fixture is intended to test scale-down behavior only.

## 5. Evidence handling rules

- A Git tree SHA and file blob SHA identify what was inspected; they do not prove execution.
- Repository documentation is project-reported evidence and must be qualified as such.
- Do not infer physical implementation, deployment, safety, or performance from a design/contract file.
- Re-inspect source repositories before any future compatibility decision.
- If source revisions change, update the profile evidence links and repeat affected review cases.
