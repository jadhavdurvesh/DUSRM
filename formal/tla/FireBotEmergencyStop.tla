---------------- MODULE FireBotEmergencyStop ----------------
CONSTANT ResetAuthorized

VARIABLES emergencyStop, manualOverride, actuatorEnabled, acceptedSource

vars == <<emergencyStop, manualOverride, actuatorEnabled, acceptedSource>>

Init ==
    /\ emergencyStop = FALSE
    /\ manualOverride = FALSE
    /\ actuatorEnabled = FALSE
    /\ acceptedSource = "none"

AutonomousCommand ==
    /\ ~emergencyStop
    /\ ~manualOverride
    /\ ~actuatorEnabled
    /\ acceptedSource = "none"
    /\ actuatorEnabled' = TRUE
    /\ acceptedSource' = "autonomous"
    /\ UNCHANGED <<emergencyStop, manualOverride>>

ManualCommand ==
    /\ ~emergencyStop
    /\ manualOverride
    /\ ~actuatorEnabled
    /\ acceptedSource = "none"
    /\ actuatorEnabled' = TRUE
    /\ acceptedSource' = "manual"
    /\ UNCHANGED <<emergencyStop, manualOverride>>

StopActuation ==
    /\ actuatorEnabled
    /\ actuatorEnabled' = FALSE
    /\ acceptedSource' = "none"
    /\ UNCHANGED <<emergencyStop, manualOverride>>

EnableManualOverride ==
    /\ ~emergencyStop
    /\ ~manualOverride
    /\ ~actuatorEnabled
    /\ manualOverride' = TRUE
    /\ UNCHANGED <<emergencyStop, actuatorEnabled, acceptedSource>>

DisableManualOverride ==
    /\ ~emergencyStop
    /\ manualOverride
    /\ ~actuatorEnabled
    /\ manualOverride' = FALSE
    /\ UNCHANGED <<emergencyStop, actuatorEnabled, acceptedSource>>

TripEmergencyStop ==
    /\ ~emergencyStop
    /\ emergencyStop' = TRUE
    /\ actuatorEnabled' = FALSE
    /\ acceptedSource' = "none"
    /\ UNCHANGED manualOverride

ResetEmergencyStop ==
    /\ emergencyStop
    /\ ResetAuthorized
    /\ ~actuatorEnabled
    /\ acceptedSource = "none"
    /\ emergencyStop' = FALSE
    /\ UNCHANGED <<manualOverride, actuatorEnabled, acceptedSource>>

Next ==
    \/ AutonomousCommand
    \/ ManualCommand
    \/ StopActuation
    \/ EnableManualOverride
    \/ DisableManualOverride
    \/ TripEmergencyStop
    \/ ResetEmergencyStop

TypeOK ==
    /\ emergencyStop \in BOOLEAN
    /\ manualOverride \in BOOLEAN
    /\ actuatorEnabled \in BOOLEAN
    /\ acceptedSource \in {"none", "autonomous", "manual"}

EmergencyStopDominates ==
    emergencyStop =>
        /\ ~actuatorEnabled
        /\ acceptedSource = "none"

ManualOverridePrecedence ==
    manualOverride => acceptedSource # "autonomous"

ActuatorSourceConsistency ==
    actuatorEnabled = (acceptedSource # "none")

Spec ==
    Init
    /\ [][Next]_vars

====
