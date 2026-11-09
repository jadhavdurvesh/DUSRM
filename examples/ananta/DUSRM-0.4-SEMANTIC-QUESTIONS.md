# ANANTA — DUSRM 0.4 Operational-Semantics Questions

**Status:** Exploratory mapping; ANANTA repository audit required

This document identifies the questions DUSRM 0.4 raises for ANANTA. It deliberately does not assign transaction, concurrency, recovery, or storage semantics without evidence from ANANTA's actual specifications and implementation.

## 1. Operation specifications

For each ANANTA operation or query-language construct, determine:
- operation identity and version;
- inputs and type/validity requirements;
- preconditions;
- expected result and side effects;
- postconditions;
- resource requirements;
- timing expectations, if any;
- cancellation and interruption behavior;
- failure and retry behavior.

## 2. Execution occurrences

Determine how ANANTA currently represents or exposes:
- request acceptance;
- parsing or validation progress, if applicable;
- execution start and completion;
- execution identity and correlation;
- partial results or partial effects;
- cancellation;
- failures and diagnostics.

Do not assume those phases exist or map them to particular modules until verified.

## 3. State and transitions

Audit which state belongs to:
- database contents;
- schema and metadata;
- active operations;
- engine configuration;
- transaction or session state, if implemented;
- persistent state versus in-memory state.

Identify the actual state transition and consistency rules. Do not infer a transaction model from the phrase "database engine."

## 4. Concurrency and time

Questions for repository inspection:
- Are operations concurrent?
- What ordering guarantees are provided?
- Are there isolation or atomicity guarantees?
- How are conflicting updates handled?
- Are timeouts and cancellation supported?
- Is query or operation execution deterministic under declared conditions?

If a feature is absent or undocumented, record it as unknown rather than inventing semantics.

## 5. Failure and recovery

Determine actual behavior for:
- malformed input;
- resource exhaustion;
- storage or filesystem errors;
- interrupted execution;
- process crash and restart;
- partial writes or effects;
- uncertain client acknowledgment;
- recovery and consistency checks.

Do not claim WAL, MVCC, rollback, snapshotting, replication, or durability behavior unless directly supported by the repository or specification.

## 6. Layer relationships

Candidate conceptual relationships:
- L5: query/computation meaning;
- L3: execution occurrence and progression;
- L4: data/state meaning and lifecycle;
- L2: resource needs and allocation;
- L6: interaction with clients and other components;
- L7: externally available database capabilities.

These are DUSRM mapping hypotheses, not an assertion about ANANTA's internal decomposition.

## 7. Evidence needed

Before this mapping can be marked verified, inspect:
- current ANANTA README and architecture;
- query language specification and examples;
- engine entry points and operation definitions;
- data and schema model;
- persistence implementation and documented guarantees;
- concurrency and transaction code, if present;
- tests for interruption, errors, and recovery;
- resource management and deployment requirements.

## 8. Result

DUSRM 0.4 provides a checklist for describing ANANTA's behavior precisely. Its usefulness will be tested only after these actual semantics are audited.
