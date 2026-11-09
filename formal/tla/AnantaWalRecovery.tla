---------------- MODULE AnantaWalRecovery ----------------
EXTENDS FiniteSets, Naturals

CONSTANTS Writers
ASSUME Writers # {}

VARIABLES running, writerOwners, phase, walDurable, commitDurable,
          artifactPublished, recoveryNeeded

vars ==
    <<running, writerOwners, phase, walDurable, commitDurable,
      artifactPublished, recoveryNeeded>>

Init ==
    /\ running = TRUE
    /\ writerOwners = {}
    /\ phase = "idle"
    /\ walDurable = FALSE
    /\ commitDurable = FALSE
    /\ artifactPublished = FALSE
    /\ recoveryNeeded = FALSE

AcquireWriter(writer) ==
    /\ running
    /\ writer \in Writers
    /\ writerOwners = {}
    /\ writerOwners' = {writer}
    /\ UNCHANGED <<running, phase, walDurable, commitDurable,
                   artifactPublished, recoveryNeeded>>

BeginOperation(writer) ==
    /\ running
    /\ writer \in writerOwners
    /\ phase \in {"idle", "applied"}
    /\ phase' = "preparing"
    /\ walDurable' = FALSE
    /\ commitDurable' = FALSE
    /\ artifactPublished' = FALSE
    /\ UNCHANGED <<running, writerOwners, recoveryNeeded>>

AppendWal(writer) ==
    /\ running
    /\ writer \in writerOwners
    /\ phase = "preparing"
    /\ walDurable' = TRUE
    /\ phase' = "wal-durable"
    /\ UNCHANGED <<running, writerOwners, commitDurable,
                   artifactPublished, recoveryNeeded>>

WriteCommitRecord(writer) ==
    /\ running
    /\ writer \in writerOwners
    /\ phase = "wal-durable"
    /\ walDurable
    /\ commitDurable' = TRUE
    /\ phase' = "committed"
    /\ UNCHANGED <<running, writerOwners, walDurable,
                   artifactPublished, recoveryNeeded>>

PublishArtifact(writer) ==
    /\ running
    /\ writer \in writerOwners
    /\ phase = "committed"
    /\ walDurable
    /\ commitDurable
    /\ artifactPublished' = TRUE
    /\ phase' = "applied"
    /\ UNCHANGED <<running, writerOwners, walDurable,
                   commitDurable, recoveryNeeded>>

ReleaseWriter(writer) ==
    /\ running
    /\ writer \in writerOwners
    /\ phase \in {"idle", "applied"}
    /\ writerOwners' = {}
    /\ UNCHANGED <<running, phase, walDurable, commitDurable,
                   artifactPublished, recoveryNeeded>>

Crash ==
    /\ running
    /\ running' = FALSE
    /\ writerOwners' = {}
    /\ phase' = "crashed"
    /\ recoveryNeeded' = TRUE
    /\ UNCHANGED <<walDurable, commitDurable, artifactPublished>>

Recover ==
    /\ ~running
    /\ recoveryNeeded
    /\ running' = TRUE
    /\ recoveryNeeded' = FALSE
    /\ writerOwners' = {}
    /\ phase' =
        IF commitDurable
        THEN IF artifactPublished THEN "applied" ELSE "committed"
        ELSE "idle"
    /\ walDurable' = IF commitDurable THEN walDurable ELSE FALSE
    /\ UNCHANGED <<commitDurable, artifactPublished>>

RedoCommittedArtifact ==
    /\ running
    /\ phase = "committed"
    /\ walDurable
    /\ commitDurable
    /\ ~artifactPublished
    /\ artifactPublished' = TRUE
    /\ phase' = "applied"
    /\ UNCHANGED <<running, writerOwners, walDurable, commitDurable,
                   recoveryNeeded>>

Next ==
    \/ \E writer \in Writers : AcquireWriter(writer)
    \/ \E writer \in Writers : BeginOperation(writer)
    \/ \E writer \in Writers : AppendWal(writer)
    \/ \E writer \in Writers : WriteCommitRecord(writer)
    \/ \E writer \in Writers : PublishArtifact(writer)
    \/ \E writer \in Writers : ReleaseWriter(writer)
    \/ Crash
    \/ Recover
    \/ RedoCommittedArtifact

TypeOK ==
    /\ running \in BOOLEAN
    /\ writerOwners \subseteq Writers
    /\ phase \in {"idle", "preparing", "wal-durable", "committed",
                   "applied", "crashed"}
    /\ walDurable \in BOOLEAN
    /\ commitDurable \in BOOLEAN
    /\ artifactPublished \in BOOLEAN
    /\ recoveryNeeded \in BOOLEAN

SingleWriter ==
    writerOwners = {}
    \/ \E writer \in Writers : writerOwners = {writer}

CommitRequiresDurableWal ==
    commitDurable => walDurable

PublishedArtifactHasCommit ==
    artifactPublished => commitDurable /\ walDurable

CommittedPhaseConsistent ==
    phase = "committed" =>
        /\ commitDurable
        /\ walDurable
        /\ ~artifactPublished

RecoveryPhaseConsistent ==
    phase = "applied" => artifactPublished

Spec ==
    Init
    /\ [][Next]_vars

====
