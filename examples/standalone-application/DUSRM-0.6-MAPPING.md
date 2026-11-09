# DUSRM 0.6 — Standalone Application Mapping

**SOI:** Single-user task-list application  
**Profile:** DUSRM-PROFILE-SWAPP-0.1  
**Status:** Illustrative model exercise, not a test of a real application

## 1. Context

Purpose: help one user create, organize, find, and complete tasks on a single computer.

Boundary: application executable, UI, task logic, and in-process state. Host OS, computer hardware, and user are external environment elements. A local file persistence adapter is optional.

## 2. Responsibility map

| ID | Responsibility | Primary layer | Example realization |
|---|---|---|---|
| R-01 | User interaction through the application interface | L6 | UI events, input and presentation boundary |
| R-02 | Task-management capability | L7 | Create, edit, complete, delete and search tasks |
| R-03 | User task-organization outcome | L8 | Help the user organize and track tasks |
| R-04 | Validate task operation and derive task results | L5 | Task rules, filtering and derived counts |
| R-05 | Maintain task information and state | L4 | Task identity, fields and completion state |
| R-06 | Dispatch and execute application operations | L3 | Application event loop and operation lifecycle |
| R-07 | Manage local memory and file resource use | L2 | Host/application resource management |
| R-08 | Use host display, CPU, filesystem and storage | L1 | External host platform |

## 3. Element realization

The same application process may realize responsibilities in L3, L4, L5, and L6. DUSRM records those responsibilities separately rather than assigning the process to a single layer.

The user is an external actor in this SOI boundary. The host OS and physical computer are external infrastructure elements. They may still appear in the environment and deployment viewpoints and may be linked to application responsibilities by explicit relationships.

## 4. Operation and state

Operation: `CompleteTask(task_id)`

- Input: task identity.
- Preconditions: task exists; actor is authorized to edit it.
- State affected: completion status.
- Effect: completion status changes to completed.
- Failure: task missing, state store unavailable, or precondition not met.
- Concurrency: unspecified for this simple example; a real app must define behavior if multiple writers exist.

## 5. Example trace

```text
Initial state:
  task.status = active

User selects Complete:
  UI emits CompleteRequested(task_id)

Application dispatches:
  execution = CompleteTask(task_id)

Guard:
  task exists AND edit permission is valid

Transition:
  task.status: active -> completed

Result:
  UI renders completed task state
```

## 6. Cross-layer relations

- L8 outcome is supported by the L7 task-management capability.
- L7 capability is accessed through L6 UI interaction.
- L6 interaction triggers L3 execution.
- L3 execution invokes L5 task validation/computation.
- L5 operation reads and changes L4 task state.
- L3/L4 activities consume L2 resources.
- L1 host platform enables the application to run.

These relations do not imply a single mandatory sequence for every implementation.

## 7. Result

The model describes a small local application without requiring a network, database server, distributed coordination, or hardware-specific control. This is a conceptual scale-down result, not implementation validation.
