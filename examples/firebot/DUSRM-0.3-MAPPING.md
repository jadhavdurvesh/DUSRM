# FireBot — DUSRM 0.3 Exploratory Mapping

**Status:** Preliminary; planned capabilities must not be mistaken for implemented features  
**Purpose:** Test DUSRM against an integrated autonomous firefighting and human-rescue robot.

## 1. System of interest

FireBot is treated as an integrated cyber-physical system that includes robot hardware, embedded and higher-level software, sensors, actuators, power systems, communications, autonomy, operator interaction, and planned multi-robot coordination.

The exact system boundary must be reviewed against the latest FireBot hardware and software specifications. Planned, selected, experimental, and implemented features must be recorded separately.

## 2. Candidate layer mapping

| Layer | FireBot concern | Initial status |
|---|---|---|
| L8 — Application & Mission Outcomes | Firefighting, human search/rescue, operator awareness, mission success criteria | Planned |
| L7 — Capabilities & Services | Navigation, mapping, perception, rescue support, fire response, diagnostics, fleet-level capabilities | Planned |
| L6 — Interaction & Coordination | Sensor/actuator interfaces, operator commands, internal subsystem interactions, robot-to-robot coordination | Planned; exact interface contracts required |
| L5 — Computation & Transformation | Computer vision, thermal interpretation, 3D mapping, sensor fusion, prioritization, navigation computations | Planned |
| L4 — Information & State | Sensor observations, maps, telemetry, mission state, robot health, power and thermal state, fleet state | Planned |
| L3 — Execution & Control | Motor and actuator execution, motion control, supervisory sequencing, manual override, safety interlocks | Planned; safety-critical design and verification required |
| L2 — Resource & Abstraction | Battery allocation, power distribution, compute, memory, communications capacity, thermal capacity | Planned |
| L1 — Physical & Infrastructure | Chassis, motors, wheels, cameras, thermal cameras, LiDAR, batteries, power electronics, compute hardware | Planned/selected hardware elements; verify against current design |

## 3. Cross-cutting concerns

These concerns apply across more than one layer and must not be treated as isolated features:

- **Safety and assurance:** emergency stop, hazard controls, fail-safe behavior, safe degraded modes, independent verification of safety-critical control paths.
- **Governance and authority:** operator override, command authority, mission constraints, permission to actuate.
- **Identity and trust:** robot identity, operator identity, authenticated peers, trust boundaries.
- **Observability and evidence:** telemetry, logs, sensor status, diagnostic evidence, mission event history.
- **Lifecycle and resilience:** startup checks, fault detection, recovery, maintenance, battery health, configuration and updates.
- **Time and uncertainty:** timestamps, sensor synchronization, localization uncertainty, perception confidence, communications delay.

DUSRM structures these concerns and supports traceability. It does not replace hazard analysis, safety engineering, functional safety standards, or independent safety verification.

## 4. Candidate integration of existing DMJ technologies

These placements are provisional and must be checked against each technology's actual specification and FireBot integration design:

| Technology | Candidate DUSRM relationship | Verification needed |
|---|---|---|
| ANANTA | Information/state responsibilities and possibly data-related computation | Inspect engine semantics, data model, persistence, and FireBot integration |
| Relay | AI capability selection and orchestration | Inspect current provider routing and runtime boundaries |
| CONTRACT | Service/API boundary and application interaction | Inspect contract and routing semantics |
| CALLGRAPH | Remote operation invocation and interaction | Inspect invocation, error, and lifecycle semantics |
| OCTET | Binary representation/encoding at information exchange boundaries | Inspect format, schema, versioning, and compatibility rules |
| DATAGRAM | Transport envelopes, sessions, sequencing, and distributed communication | Inspect transport specification and network integration |
| Telegraph | Unassigned until its complete specification is reviewed | Retrieve the current project specification |
| MAINTAIN.ai / DeviceOS | Potential device monitoring, hardware-facing operation, and maintenance boundaries | Inspect actual deployed responsibilities and integration |

The table is a mapping hypothesis, not a claim that every technology is already integrated or that any one technology implements an entire DUSRM layer.

## 5. Critical architectural rule

Safety-critical control must not depend on the uninterrupted availability of a remote model, database, or non-safety communication path. FireBot's emergency-stop and safe-state behavior must be designed, implemented, and verified as explicit safety requirements with appropriate independent mechanisms.

## 6. DUSRM questions raised by FireBot

- Can the model describe a physical device and its digital representation without conflating them?
- Can resource allocation and power management be represented separately from control execution?
- Can AI inference be represented as computation while preserving independent authority over actuation?
- Can the model express a Hive Mind relationship without requiring centralized control?
- Can safety and governance constraints apply to all relevant layers?
- Can communications delay, uncertainty, partial failure, and local autonomy be represented?
- Can the model distinguish a capability that is planned from one that is implemented and verified?

## 7. Outcome

FireBot is a strong candidate for testing DUSRM's cyber-physical and cross-cutting concepts. The current mapping is architectural planning material, not a validated design or safety case.
