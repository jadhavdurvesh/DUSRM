# DUSRM Profile — Standalone Software Application

**Profile ID:** DUSRM-PROFILE-SWAPP-0.1  
**Status:** Illustrative profile; non-normative  
**Based on:** DUSRM 0.5 core draft

## 1. Purpose

This profile applies DUSRM to a small standalone software application. It tests whether the reference model is useful without requiring a database engine, network, distributed system, or physical robotics hardware.

## 2. Scope

Illustrative SOI: a single-user task-list application running on one general-purpose computer.

Inside the SOI:
- application logic;
- local user interface;
- in-process application state;
- local persistence component, if the selected design includes one.

External context:
- user;
- operating system and host hardware;
- optional filesystem service.

The example does not assume cloud services, user accounts, distributed collaboration, or network access.

## 3. Layer responsibilities

| Layer | Profile responsibilities | Applicability |
|---|---|---|
| L1 Physical & Infrastructure | Host computer, processor, memory, display, local storage medium | Applicable through external platform |
| L2 Resource & Abstraction | Process memory, filesystem capacity, CPU time, local resource limits | Applicable |
| L3 Execution & Control | Application startup, event loop, task operations, save/load operations, shutdown | Applicable |
| L4 Information & State | Task identity, task fields, completion state, preferences, persistence representation | Applicable |
| L5 Computation & Transformation | Task filtering, sorting, validation, derived counts, input transformation | Applicable |
| L6 Interaction & Coordination | UI events, user interaction, internal component interfaces | Applicable; external network interaction not required |
| L7 Capabilities & Services | Create, edit, complete, delete, search, and organize tasks | Applicable |
| L8 Application & Mission Outcomes | Help one user organize and track tasks | Applicable |

## 4. Minimal behavior example

Operation: `CompleteTask(task_id)`

- Precondition: task exists and is editable.
- Input: stable task identifier.
- Effect: completion state changes to true.
- Postcondition: task is represented as complete.
- Failure conditions: task identifier is unknown or the task store is unavailable.
- State transition: `ActiveTask → CompletedTask`, when the declared guard holds.

This is a conceptual operation definition. A real application must specify concurrency, persistence and error behavior in its own design.

## 5. Optional layers and omissions

A profile does not require all possible kinds of interaction:
- A network service is not required for L6.
- A database engine is not required for L4.
- The application may persist data through a local file or may be intentionally transient.
- The host hardware and operating system can be external to the application SOI while still being described in its environment and deployment viewpoints.

## 6. Validation questions

- Can the application be mapped without inventing a network layer?
- Are task semantics separate from UI interaction?
- Are application state and host memory distinguished?
- Can the profile describe both transient and persistent variants?
- Can one in-process component realize responsibilities in L3, L4, and L5?

## 7. Status

This profile is illustrative. It is a scale-down test of the DUSRM concepts, not evidence from a specific deployed task-list application.
