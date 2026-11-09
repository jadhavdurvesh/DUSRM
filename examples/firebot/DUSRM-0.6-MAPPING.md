# FireBot — DUSRM 0.6 Validation Mapping

**SOI:** Integrated FireBot software-first robot system and its planned physical realization  
**Profile:** DUSRM-PROFILE-CPS-ROBOT-0.1  
**Status:** Repository-informed; simulation and plans distinguished from physical implementation

## 1. Evidence baseline

Core repository: https://github.com/jadhavdurvesh/firebot-core

Subsystem repositories inspected include:
- firebot-vision
- firebot-firmware
- firebot-hardware
- firebot-hive-mind
- firebot-power-management
- firebot-mapping
- firebot-simulation

Exact source references and blob identifiers are recorded in the DUSRM 0.6 evidence register.

## 2. System boundary

For the present validation, the SOI is the integrated FireBot project as documented: core architecture, dashboard/simulation software and planned subsystem interfaces. The intended physical robot is a future realization within the same project scope.

External context includes the environment/fire scene, operator, host/development platform, and future robot peers.

## 3. Responsibility-to-layer mapping

| Responsibility | Layer | Evidence | Status |
|---|---|---|---|
| Physical robot platform, chassis, motors, sensors, power electronics | L1 | Hardware repository README and power worksheet | Planned; no connected physical hardware reported |
| Compute/power resource allocation | L2 | Power policy and power budget | Policy is simulated; electrical parameters unresolved |
| Simulation engine actions, mission state progression, command guards | L3 | Core interface contract and simulation docs; firmware command contract | Simulation behavior documented; physical control unimplemented |
| Robot, mission, detection, mapping, power and fleet state | L4 | INTERFACES.md and subsystem contracts | Software contract/simulation data |
| Route planning and rule-based situational awareness | L5 | Core architecture/current-state documents | Simulation code reported; not a validated robotics navigation stack |
| Person/fire detection, real mapping and sensor fusion | L5 | Vision and mapping contracts | Planned/unverified |
| Module, operator, fleet, and DMJ technology interfaces | L6 | INTERFACES.md and integration plans | Contracts/proposals; no live robot networking |
| Dashboard, simulation, diagnostic and coordination capabilities | L7 | Core and subsystem repositories | Software/simulation only |
| People-first rescue and firefighting mission outcomes | L8 | Core architecture and vision/Hive Mind contracts | Mission goals documented; real-world success not established |

## 4. Cross-cutting constraints

- The simulation and dashboard must label synthetic readings and detections as simulated.
- Stale, missing, invalid, or low-confidence observations must not be promoted to confirmed findings.
- Person evidence has priority over fire-only evidence in the stated mission policy, subject to operator control and safety constraints.
- Manual override and emergency-stop authority must take precedence over autonomous commands.
- Local safety and time-sensitive control must not depend on network response, database availability, or AI model availability.
- Fleet messages may be stale, lost, duplicated, or reordered; absence of a message is not evidence that a sector is clear.
- A command or acknowledgment is not proof of physical actuation.
- Physical safety requires independent hazard analysis, electrical/mechanical design, implementation, and verification.

These are documented design requirements/contracts. Their physical implementation and safety effectiveness are not verified by this profile.

## 5. DMJ technology mapping

| Technology | DUSRM responsibility area | Current integration evidence |
|---|---|---|
| CONTRACT | L6/L7 operator, dashboard and mission API boundaries | Proposed in DMJ_SYSTEMS_INTEGRATION.md; live integration not established |
| OCTET | L4/L6 typed message representation and exchange | Proposed; no live robot message path established |
| DATAGRAM | L6 robot/station/fleet transport | Proposed; no live inter-robot network established |
| CALLGRAPH | L6/L7 non-time-critical supervisory operations | Proposed; must remain outside high-frequency control loops |
| ANANTA | L4/L5 persistence and analysis of telemetry/event data | Separate DBMS; optional file-based JSONL FireBot workload documented; live database integration not established |
| Relay | Potential AI model selection/orchestration | Not evidenced in the inspected FireBot integration baseline; map only after reviewing current Relay and FireBot specs |
| Telegraph | Unassigned | Complete specification required before mapping |

DUSRM describes the integration architecture. Each technology's own specification governs its API, protocol, engine, data format, and runtime behavior.

## 6. Model validation result

**Preliminary pass with findings** for descriptive coverage of the intended system and current software prototype.

Findings:
- The eight layers can describe software simulation and future physical realization in one scope if maturity and boundary are explicit.
- L1 must remain marked planned for physical hardware.
- L2 power policy is simulated and electrical design is unresolved.
- L3 simulation control must not be mistaken for physical actuator control.
- L4 provenance and source status are important to prevent synthetic data from becoming apparent telemetry.
- L6 custom technology integration is documented as proposed, not implemented.
- Safety, authority, time, and uncertainty must be modeled as cross-cutting concerns.

## 7. Remaining verification actions

- Run the current FireBot simulation and core Node.js test suites and preserve results.
- Verify CI status and hosted deployment separately.
- Execute deterministic scenarios for stale vision, low power, cooling failure, emergency override, and fleet link loss.
- Validate all simulation outputs preserve `simulated` status.
- Review and implement the ANANTA file-based telemetry workload using a privacy-minimized, allow-listed fixture.
- Keep all physical actuation disconnected during communication fault-injection tests.
- Perform hardware-in-the-loop and physical safety validation only after separately approved design and review.

No code tests, physical tests, or safety verification were executed as part of this DUSRM validation exercise.
