---------------- MODULE DistributedTaskArbitration ----------------
EXTENDS FiniteSets

CONSTANTS Robots, Tasks
ASSUME /\ Robots # {}
       /\ Tasks # {}

VARIABLES assignments, localClaims, connectedRobots, coordinatorAvailable

vars == <<assignments, localClaims, connectedRobots, coordinatorAvailable>>

AssignedOwners(task) ==
    {robot \in Robots : <<robot, task>> \in assignments}

Init ==
    /\ assignments = {}
    /\ localClaims = {}
    /\ connectedRobots = Robots
    /\ coordinatorAvailable = TRUE

LocalClaim(robot, task) ==
    /\ robot \in Robots
    /\ task \in Tasks
    /\ <<robot, task>> \notin localClaims
    /\ localClaims' = localClaims \cup {<<robot, task>>}
    /\ UNCHANGED <<assignments, connectedRobots, coordinatorAvailable>>

Disconnect(robot) ==
    /\ robot \in connectedRobots
    /\ connectedRobots' = connectedRobots \ {robot}
    /\ UNCHANGED <<assignments, localClaims, coordinatorAvailable>>

Reconnect(robot) ==
    /\ robot \in Robots \ connectedRobots
    /\ connectedRobots' = connectedRobots \cup {robot}
    /\ UNCHANGED <<assignments, localClaims, coordinatorAvailable>>

CoordinatorDown ==
    /\ coordinatorAvailable
    /\ coordinatorAvailable' = FALSE
    /\ UNCHANGED <<assignments, localClaims, connectedRobots>>

CoordinatorUp ==
    /\ ~coordinatorAvailable
    /\ coordinatorAvailable' = TRUE
    /\ UNCHANGED <<assignments, localClaims, connectedRobots>>

AcceptClaim(robot, task) ==
    /\ robot \in connectedRobots
    /\ coordinatorAvailable
    /\ <<robot, task>> \in localClaims
    /\ AssignedOwners(task) = {}
    /\ assignments' = assignments \cup {<<robot, task>>}
    /\ localClaims' = {claim \in localClaims : claim[2] # task}
    /\ UNCHANGED <<connectedRobots, coordinatorAvailable>>

Next ==
    \/ \E robot \in Robots, task \in Tasks : LocalClaim(robot, task)
    \/ \E robot \in Robots : Disconnect(robot)
    \/ \E robot \in Robots : Reconnect(robot)
    \/ CoordinatorDown
    \/ CoordinatorUp
    \/ \E robot \in Robots, task \in Tasks : AcceptClaim(robot, task)

TypeOK ==
    /\ assignments \subseteq (Robots \X Tasks)
    /\ localClaims \subseteq (Robots \X Tasks)
    /\ connectedRobots \subseteq Robots
    /\ coordinatorAvailable \in BOOLEAN

AtMostOneAuthoritativeOwner ==
    \A task \in Tasks : Cardinality(AssignedOwners(task)) <= 1

AcceptedAssignmentHasKnownOwner ==
    \A pair \in assignments : pair[1] \in Robots /\ pair[2] \in Tasks

Spec ==
    Init
    /\ [][Next]_vars

====
