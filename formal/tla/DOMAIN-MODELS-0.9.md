# DUSRM 0.9 — Domain Formal-Methods Models

**Status:** Finite formal-methods pilots; non-normative  
**TLA+ tools:** TLA+ tools v1.7.4 / TLC 2.19

## 1. Purpose

DUSRM 0.9 adds three small formal models to exercise concepts that are not captured by the original task-completion example:
- distributed coordination under partition;
- emergency-stop precedence in a cyber-physical controller;
- single-writer, write-ahead-log and crash-recovery ordering.

Each model is intentionally narrower than the corresponding real system.

## 2. DistributedTaskArbitration

### DUSRM mapping

| DUSRM concept | TLA+ representation |
|---|---|
| Robot participants | `Robots` |
| Mission tasks | `Tasks` |
| Local task claims | `localClaims` |
| Authoritative accepted assignments | `assignments` |
| Network reachability | `connectedRobots` |
| Coordinator availability | `coordinatorAvailable` |
| Coordinator acceptance operation | `AcceptClaim(robot, task)` |
| Safety invariant | `AtMostOneAuthoritativeOwner` |

### Property

`AtMostOneAuthoritativeOwner` states that each task has at most one authoritative assigned robot.

Local claims may conflict while robots are disconnected. They do not become authoritative assignments until the coordinator accepts one claim while the robot is connected and the coordinator is available.

### Assumptions and limits

- One abstract coordinator serializes acceptance.
- The model does not prove consensus, leader election, quorum safety, Byzantine fault tolerance, or network liveness.
- Local claims are not authoritative assignments.
- The model does not specify mission suitability, robot capability matching, geospatial conflict resolution, or human approval.

## 3. FireBotEmergencyStop

### DUSRM mapping

| DUSRM concept | TLA+ representation |
|---|---|
| Emergency-stop latch | `emergencyStop` |
| Manual override mode | `manualOverride` |
| Actuator enable state | `actuatorEnabled` |
| Accepted command source | `acceptedSource` |
| Autonomous command action | `AutonomousCommand` |
| Manual command action | `ManualCommand` |
| Emergency-stop action | `TripEmergencyStop` |
| Safety invariant | `EmergencyStopDominates` |

### Properties

- When emergency stop is latched, actuator enable is false and no command source remains accepted.
- Manual override prevents autonomous command acceptance.
- Actuator enable and accepted command source remain consistent.

### Assumptions and limits

- The model is a discrete logical controller abstraction.
- It assumes the emergency-stop transition is processed atomically at this abstraction level.
- It does not model electrical relay behavior, contactor weld faults, braking distance, actuator inertia, thermal effects, wiring faults, independent safety circuits, or certified safety integrity.
- It is not a physical emergency-stop design or safety case. FireBot requires separate hazard analysis and hardware verification.

## 4. AnantaWalRecovery

### DUSRM mapping

| DUSRM concept | TLA+ representation |
|---|---|
| Single-writer ownership | `writerOwners` |
| Operation lifecycle | `phase` |
| Durable write-ahead record | `walDurable` |
| Durable commit record | `commitDurable` |
| Published artifact | `artifactPublished` |
| Process availability | `running` |
| Recovery requirement | `recoveryNeeded` |
| Crash / restart | `Crash`, `Recover` |
| Redo after durable commit | `RedoCommittedArtifact` |

### Properties

- At most one writer owns the modeled database at a time.
- A commit record cannot exist without a durable WAL record.
- An artifact cannot be published without a durable commit record and WAL record.
- Recovery after a committed-but-unpublished operation restores the committed phase and permits redo.
- Recovery after an uncommitted operation discards the uncommitted WAL state in this abstraction.

### Assumptions and limits

- The model covers one logical operation at a time and a finite writer set.
- It abstracts filesystem ordering and durability into Boolean state variables.
- It does not model checksums, filesystem semantics, device caches, flush/barrier behavior, torn writes, multiple artifact types, log truncation, checkpointing, corruption, or multi-process OS locking details.
- This model is consistent with an operation-scoped redo boundary and single-writer scope; it does not establish general ACID or MVCC behavior.
- The model must be compared with ANANTA's current transaction and recovery specifications before being treated as an implementation-level assurance model.

## 5. Execution

Each model has its own TLC configuration. CI checks its declared invariants over the finite state space configured in the corresponding `.cfg` file.

A TLC pass means only that no counterexample was found in that finite model under its declared constants and assumptions. It does not prove the real distributed system, robot, or database implementation correct.
