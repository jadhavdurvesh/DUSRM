# DUSRM 0.3 — Structural Validation Matrix

**Status:** Exploratory; non-normative  
**Purpose:** Test whether the proposed eight-layer hybrid structure can describe different system scales without inventing implementation details.

## 1. Validation method

For each case study:
1. Declare the system of interest and boundary.
2. Map known responsibilities to candidate layers.
3. Mark each mapping as known, planned, inferred, or unknown.
4. Record cross-layer relationships and cross-cutting concerns.
5. Identify concepts that do not fit or are duplicated.
6. Propose revisions only when evidence demonstrates a structural problem.

A successful mapping is not proof that DUSRM is complete or that the system is safe, correct, or conformant.

## 2. Evidence-status legend

- **Known:** supported by the project context or an inspected authoritative specification.
- **Planned:** described as an intended capability or design.
- **Inferred:** plausible placement that needs verification.
- **Unknown:** insufficient information to map responsibly.
- **Not applicable:** genuinely outside the declared SOI.

## 3. Cross-domain coverage matrix

| DUSRM layer | Small standalone application | ANANTA | FireBot |
|---|---|---|---|
| L8 Application & Mission Outcomes | Known conceptually | Known at high level; exact user workflows need repository review | Planned mission outcomes |
| L7 Capabilities & Services | Known conceptually | Inferred from database/engine purpose; service catalog needs audit | Planned robot and fleet capabilities |
| L6 Interaction & Coordination | Inferred from user, OS, and external interfaces | Custom integration points require specification audit | Planned subsystem, operator, and fleet interactions |
| L5 Computation & Transformation | Known conceptually | Custom query/computation engine is known at high level; internals need audit | Planned perception, mapping, fusion, and decision workloads |
| L4 Information & State | Known conceptually | Database and data-engine responsibility known; exact semantics need audit | Planned maps, telemetry, mission, robot, and fleet state |
| L3 Execution & Control | Runtime behavior depends on application | Execution semantics and concurrency require repository audit | Planned embedded execution, actuator control, and supervisory control |
| L2 Resource & Abstraction | Host resources apply | Memory, storage, and compute management need audit | Planned energy, compute, bandwidth, and hardware-resource management |
| L1 Physical & Infrastructure Foundation | Host platform applies | Deployment platform must be declared per deployment | Planned robot chassis, sensors, actuators, batteries, and compute hardware |

The table demonstrates broad coverage, not verified implementation. ANANTA details intentionally remain marked for repository review rather than being invented.

## 4. FireBot exploratory mapping

FireBot is a useful cyber-physical case because its scope crosses hardware, software, autonomy, communications, power, operator interaction, and fleet coordination.

| Layer | FireBot responsibilities to describe | Evidence status |
|---|---|---|
| L8 | Firefighting, human search/rescue, operator awareness, mission objectives | Planned |
| L7 | Navigation, mapping, perception, rescue support, fire response, diagnostics, fleet capabilities | Planned |
| L6 | Sensor/actuator interfaces, operator interaction, robot-to-robot coordination, software integration | Planned; interface specifications required |
| L5 | Computer vision, thermal interpretation, 3D mapping, sensor fusion, prioritization, navigation computations | Planned |
| L4 | Sensor observations, maps, telemetry, mission state, battery/thermal state, fleet state | Planned |
| L3 | Motion execution, supervisory control, actuator sequencing, manual override, safety interlocks | Planned; safety engineering required |
| L2 | Battery allocation, power distribution, compute, memory, bandwidth, thermal capacity | Planned |
| L1 | Chassis, motors, wheels, sensors, cameras, LiDAR, batteries, power electronics, compute hardware | Planned/selected design elements; verify against current hardware specification |

### Candidate cross-cutting concerns

- Safety engineering: emergency stop, hazard controls, loss-of-communication behavior, safe degraded modes.
- Governance and authority: operator override, mission permissions, robot/fleet command authority.
- Identity and trust: device identity, operator identity, trusted communication peers.
- Observability and evidence: telemetry, logs, sensor health, fault evidence, mission records.
- Lifecycle and resilience: startup, self-checks, fault recovery, maintenance, battery degradation, configuration.
- Time and uncertainty: sensor timestamps, localization uncertainty, communications delay, confidence in perception.

**Safety boundary:** DUSRM can organize the safety architecture and trace safety requirements. It cannot establish that FireBot is safe. Safety-critical actuation and emergency-stop paths require independent engineering analysis, implementation, and verification.

### Existing DMJ technologies

The following are candidate mappings only. Their exact specification and current FireBot integration must be checked before the assignments become verified:
- ANANTA may support information/state and data-related computation responsibilities.
- Relay may support AI capability selection and orchestration.
- CONTRACT and CALLGRAPH may support service and interaction boundaries.
- OCTET may support representation/encoding at an information or interaction boundary.
- DATAGRAM may support communication between distributed elements.
- Telegraph's placement is deferred until its complete specification is reviewed.
- MAINTAIN.ai and DeviceOS mappings depend on the actual deployed responsibilities and interfaces.

DUSRM must not redefine any of these technologies.

## 5. ANANTA exploratory mapping

The only established project-level facts used here are that ANANTA is a custom database/data engine with its own engine and query language. The following details require direct repository audit.

| Layer | ANANTA questions to answer | Current evidence status |
|---|---|---|
| L8 | What applications, users, and workloads does ANANTA serve? | Broad purpose known; workflows need audit |
| L7 | What database and engine capabilities are exposed? | Needs specification audit |
| L6 | What interfaces connect ANANTA to clients and other components? | Needs repository and protocol audit |
| L5 | How are queries or computational operations interpreted and executed? | Custom engine/query language known; internals need audit |
| L4 | What are the data model, identity, schema, state, and persistence semantics? | Needs technical specification audit |
| L3 | What are execution, scheduling, transaction, concurrency, and recovery semantics? | Unknown until repository audit |
| L2 | How are memory, storage, CPU, and other resources managed? | Unknown until repository audit |
| L1 | What host hardware, operating systems, and storage infrastructure are supported? | Deployment-specific |

The mapping must not invent a transaction model, storage layout, query-planning pipeline, WAL behavior, or consistency guarantee. Those belong to ANANTA's actual specifications and implementation.

## 6. Acceptance questions

The candidate structure should be revised if any of the following cannot be answered consistently:
- Can a small application be mapped without inventing unnecessary layers?
- Can ANANTA's data and computation responsibilities be separated without forcing a specific engine design?
- Can FireBot's physical, computational, and mission responsibilities all be represented?
- Can one component map to more than one layer?
- Can a relationship skip layers without breaking the model?
- Can safety, trust, and governance apply across the stack?
- Can planned, implemented, observed, and verified claims be distinguished?
- Can the model coexist with the existing DMJ technologies without redefining them?

## 7. Result

The initial mappings suggest that the hybrid candidate can express all three system scales at a high conceptual level. This is a preliminary coverage result only. It does not prove completeness, uniqueness, usability, or conformance.

The next validation iteration must inspect the actual ANANTA and FireBot repositories/specifications and test layer boundaries with concrete subsystem examples.
