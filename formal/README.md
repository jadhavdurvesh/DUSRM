# DUSRM Formal Methods

This directory contains external formal-methods model pilots. TLA+ is used as an analysis notation/tool, not as a replacement for DUSRM's ontology or operational semantics.

## Models

- [Task completion](tla/TaskCompletion.tla) — authorized task-state transition.
- [Distributed task arbitration](tla/DistributedTaskArbitration.tla) — local claims, partitions, and single-coordinator assignment.
- [FireBot emergency stop](tla/FireBotEmergencyStop.tla) — emergency-stop and manual/autonomous command precedence.
- [ANANTA WAL recovery](tla/AnantaWalRecovery.tla) — single-writer, WAL/commit ordering, crash and redo.

See [DUSRM 0.9 model mappings](tla/DOMAIN-MODELS-0.9.md) for assumptions and traceability.

The models are manually authored finite abstractions. They do not prove real implementations safe or correct, and do not replace hazard analysis, database implementation tests, distributed protocol verification, or hardware-in-the-loop testing.
