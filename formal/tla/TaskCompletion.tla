---------------- MODULE TaskCompletion ----------------
EXTENDS Naturals

CONSTANT Authorized

VARIABLES taskState, requestPending

vars == <<taskState, requestPending>>

Init ==
    /\ taskState = "active"
    /\ requestPending = TRUE

CompleteTask ==
    /\ requestPending
    /\ Authorized
    /\ taskState = "active"
    /\ taskState' = "completed"
    /\ requestPending' = FALSE

Next ==
    CompleteTask
    \/ UNCHANGED vars

TypeOK ==
    /\ taskState \in {"active", "completed"}
    /\ requestPending \in BOOLEAN

CompletionSafety ==
    taskState = "completed" => Authorized

CompletionTerminates ==
    <> (requestPending = FALSE)

Spec ==
    Init
    /\ [][Next]_vars
    /\ WF_vars(CompleteTask)

====
