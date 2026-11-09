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
| R-01 | Display and input presentation | L7 | Task-list UI capability |
| R-02 | User task-management workflow | L8 | Create/complete task outcome |
| R-03 | Validate task operation | L5 | Task rules |
| R-04 | Update task state | L4 | Task state store |
| R-05 | Dispatch UI events and operation execution | L3 | Application event loop |
| R-06 | Expose internal UI/model interface | L6 | In-process interface |
| R-07 | Manage local memory and file resource use | L2 | Host/application resource management |
| R-08 | Use host display, CPU, filesystem and storage | L1 | External host platform |

## 3. Element realization

The same application process may realize R-03, R-04, R-05, and R-06. DUSRM records those responsibilities separately rather than assigning the process to a single layer.

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

- L8 outcome depends on L7 task-management capability.
- L7 capability interacts through L6 UI/internal interfaces.
- L6 requests trigger L3 execution.
- L3 execution invokes L5 task validation/computation.
- L5 operation reads and changes L4 task state.
- L3/L4 activities consume L2 resources.
- L1 host platform enables the application to run.

These relations do not imply a single mandatory sequence for every implementation.

## 7. Result

The model describes a small local application without requiring a network, database server, distributed coordination, or hardware-specific control. This is a conceptual scale-down result, not implementation validation.
