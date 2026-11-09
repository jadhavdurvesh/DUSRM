# DUSRM Profile — Cyber-Physical Robotics (FireBot)

**Profile ID:** DUSRM-PROFILE-CPS-ROBOT-0.1  
**Profile version:** 0.1-draft  
**Status:** Repository-informed mapping; non-normative  
**Core compatibility:** Candidate for DUSRM 0.7-draft; not yet assessed  
**SOI:** FireBot integrated firefighting and human-rescue robot system  
**Primary source:** https://github.com/jadhavdurvesh/firebot-core

## 1. Scope and maturity

FireBot is documented as a software-first firefighting robot concept. The repositories include dashboard and simulation work plus separate subsystem contracts and plans for vision, mapping, power management, Hive Mind, firmware, and hardware.

The current status snapshot in `firebot-core/CURRENT_STATE.md` is dated 2026-10-11. It reports that the dashboard and simulation logic are in active development, while no physical sensors, motors, pump, batteries, cooling system, or microphone are connected. It reports vision AI, live mapping, live Hive Mind networking, and physical power/controller failover as pending or unverified.

This DUSRM profile therefore distinguishes:
- the **intended integrated cyber-physical system**;
- the **current software/simulation prototype**;
- the **planned physical robot and live subsystem implementations**.

A planned property must not be presented as an implemented or verified physical capability.

## 2. Responsibility mapping

| Layer | FireBot responsibilities | Evidence status |
|---|---|---|
| L1 Physical & Infrastructure Foundation | Chassis, motors, cameras, thermal cameras, LiDAR, battery and power electronics, compute hardware | Planned; physical hardware not connected according to current-state snapshot |
| L2 Resource & Abstraction | Power-domain budgeting, load priorities, energy reserve, compute and communication resource limits | Power policy is simulated; electrical budget is a planning worksheet; physical values not selected |
| L3 Execution & Control | Simulation engine actions and route progression; future firmware command guards, local motion and safety control | Simulation code/contract documented; physical actuation and firmware safety behavior not implemented |
| L4 Information & State | Robot state, mission state, pose/map data, detection records, power status, fleet status, source/status provenance | Software message contracts and simulation state documented; real sensor/robot state not established |
| L5 Computation & Transformation | Deterministic simulated A* route planning, rule-based situational awareness, future vision, mapping and sensor fusion | A* and rule-based simulation reported in repository; real vision and SLAM unverified/planned |
| L6 Interaction & Coordination | Browser/dashboard and subsystem contracts; proposed CONTRACT/OCTET/DATAGRAM/CALLGRAPH integration; planned Hive Mind | Interface contracts documented; integration plans are proposals; no live robot network |
| L7 Capabilities & Services | Dashboard presentation, simulated navigation, scenario playback, synthetic alerts and fleet visualization | Software/simulation capabilities; not validated physical robot services |
| L8 Application & Mission Outcomes | People-first search/rescue support, firefighting, operator awareness, mission coordination | Project objectives and policies documented; mission success in real environments not established |

## 3. Operational and cross-cutting requirements

### 3.1 People-first decision policy

FireBot documents a people-first objective: unresolved people are selected before fire objectives in the simulation. The vision contract also requires person and fire detections to remain distinguishable and low-confidence/stale/malformed evidence not to be promoted to confirmed findings.

This is a documented project policy and contract. Real person detection performance remains unverified.

### 3.2 Authority and safety

The proposed command contract states that operator emergency stop takes precedence over autonomy and manual override suspends autonomous motion requests. The FireBot integration plan requires local emergency-stop and time-sensitive control paths to remain independent of CONTRACT, CALLGRAPH, and network availability.

These are design requirements/contracts, not verified physical safety mechanisms. Actual emergency-stop, motor inhibit, pump control, and thermal protection require independent hardware and safety verification.

### 3.3 State, time and provenance

FireBot interface contracts define source and status fields such as simulated, implemented, planned, and unverified, plus timestamps and schema versions. Vision and mapping contracts require freshness, coordinate frame, confidence, and uncertainty where relevant.

The DUSRM profile maps these to L4 state/information and cross-cutting time, uncertainty, and observability concerns.

### 3.4 Degraded operation

Optional subsystem failure should reduce only the dependent capability, with explicit health/freshness state. Audio is optional; missing audio is not evidence that a person is absent. Fleet messages that are stale or missing are not proof that a sector is clear.

These are documented contract rules; runtime behavior remains subject to implementation and test evidence.

## 4. Existing and planned DMJ technology integration

The FireBot integration plan identifies:
- CONTRACT for operator/dashboard/mission APIs;
- OCTET for versioned subsystem and fleet message encoding;
- DATAGRAM for robot-to-robot and robot-to-station transport;
- CALLGRAPH for non-time-critical supervisory operations.

The same document explicitly states that this is a proposal and that these technologies are not yet integrated into a live robot/network path.

ANANTA is maintained as a separate native database project. The ANANTA repository includes an optional file-based FireBot JSONL workload connector targeting `ananta.firebot_events`. This is a documented adapter/workload, not evidence of live production integration.

Other candidate integrations such as Relay must be mapped only after their current specifications and the FireBot integration baseline are inspected. Do not infer use from a project name.

## 5. Validation gaps

- Execute the current dashboard/simulation test suite; the FireBot status snapshot says the latest Node.js test execution remains unverified.
- Verify hosted deployment separately from repository code.
- Run deterministic simulation scenarios for stale vision, low battery, primary controller failure, thermal limit, and fleet link loss.
- Verify that all synthetic data remains marked simulated.
- Verify CONTRACT/OCTET/DATAGRAM/CALLGRAPH adapters only after they exist; do not treat integration proposals as tests.
- Define and validate the ANANTA FireBot event schema, offline ingestion procedure, and end-to-end data provenance.
- Complete hazard analysis and physical safety design before connecting any actuation.

## 6. Safety boundary

DUSRM is an architecture reference model. This profile is not a robotics safety case, emergency-stop design, hazard analysis, electrical design, or certification. Physical FireBot requires independent hazard analysis, mechanical/electrical review, controller verification, environmental testing, and hardware-in-the-loop validation.

## 7. Evidence

See [DUSRM 0.6 evidence register](../../validation/0.6-EVIDENCE-REGISTER.md) for inspected sources and revision identifiers.
