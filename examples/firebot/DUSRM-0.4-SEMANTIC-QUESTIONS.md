# FireBot — DUSRM 0.4 Operational-Semantics Questions

**Status:** Exploratory mapping; planned behavior must not be treated as implemented or verified

## 1. Purpose

This document identifies operational-semantic questions for FireBot. It is not a control design, safety case, verified state machine, or statement that the listed capabilities are implemented.

## 2. Candidate operational areas

### 2.1 Sensing and observation

For each sensor observation, specify:
- source device and sensor identity;
- event/sample time and observation time;
- coordinate frame, units, calibration, and uncertainty where relevant;
- quality/freshness conditions;
- behavior on missing, delayed, duplicated, or invalid observations.

### 2.2 Perception and computation

For each perception or mapping operation, specify:
- inputs and provenance;
- preconditions and quality gates;
- output and confidence/uncertainty;
- computational resource requirements;
- execution lifecycle;
- timeout and failure behavior;
- effect on mission and robot state.

A model output is information for a decision process; it is not by itself authorization to actuate.

### 2.3 Mission and task execution

For each mission activity, define:
- mission state and permitted transitions;
- start conditions and authority;
- completion criteria;
- abort, pause, resume, and cancel behavior;
- dependency and resource requirements;
- operator notification and override;
- failure and degraded modes.

### 2.4 Motion and actuation

For each actuation operation, define:
- initiating authority;
- preconditions and safety interlocks;
- bounds and operating constraints;
- expected physical effect;
- feedback evidence;
- timeout and mismatch behavior;
- independent stop or safe-state path;
- verification requirements.

A command sent to a motor driver is not proof that a wheel moved as intended.

### 2.5 Power and thermal management

For power-state transitions, describe:
- measured voltage/current/temperature and source;
- limits and uncertainty;
- resource allocation decision;
- conditions for load shedding or power diversion;
- transition effects;
- recovery and restart conditions;
- behavior when sensors disagree or become unavailable.

Values and control policies must come from validated electrical, thermal, and safety engineering; DUSRM does not invent them.

### 2.6 Fleet coordination / Hive Mind

For each robot participant, define:
- identity and membership status;
- locally known state and remote observations;
- communication uncertainty;
- task authority and assignment;
- conflict resolution and duplicate assignments;
- behavior during disconnection or stale information;
- rejoin and state reconciliation.

Do not assume a global shared state or perfect event ordering.

## 3. Candidate state domains

Potential state domains include:
- robot operational state;
- mission/task state;
- motion/control state;
- power state;
- thermal state;
- sensor health and observation quality;
- communications/connectivity state;
- fleet membership and coordination state.

These should not be collapsed into a single state machine if they evolve independently. Their synchronization and constraints must be explicitly modeled.

## 4. Cross-cutting safety constraints

The following require independent safety-engineering treatment:
- emergency stop and safe-state behavior;
- manual override and authority arbitration;
- loss or corruption of sensor data;
- communications loss or delay;
- overheating and power failure;
- unexpected motion or actuator disagreement;
- software crash or reset;
- unsafe interactions between autonomous and manual control.

DUSRM can organize hazards, constraints, safety controls, state transitions, and evidence. It cannot establish safety or replace hazard analysis and verification.

## 5. Relationship to DMJ technologies

The actual operational behavior of ANANTA, Relay, CONTRACT, CALLGRAPH, OCTET, DATAGRAM, Telegraph, MAINTAIN.ai, and DeviceOS must be taken from their individual specifications and implementations.

DUSRM describes how their behavior participates in FireBot's system. It does not redefine their contracts, message formats, or communication behavior.

## 6. Evidence required

For every behavior, record whether it is:
- proposed;
- specified;
- implemented;
- tested;
- observed;
- verified;
- unknown.

A planned state diagram is not evidence that the physical robot implements or safely enforces those transitions.

## 7. Result

DUSRM 0.4 provides a language for describing the dynamics of FireBot. A real FireBot operational model requires verified subsystem requirements, interface specifications, hazards, control logic, and test evidence.
