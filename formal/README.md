# DUSRM Formal Methods

This directory contains external formal-methods model pilots. TLA+ is used as an analysis notation/tool, not as a replacement for DUSRM's ontology or operational semantics.

## Pilot

- [Task completion TLA+ model](tla/TaskCompletion.tla)
- [TLC configuration](tla/TaskCompletion.cfg)
- [DUSRM-to-TLA+ mapping and assumptions](tla/MAPPING.md)

## Boundary

The pilot is manually authored and traceable to one DUSRM example. There is no automatic translation from arbitrary DUSRM descriptions or natural-language guards into TLA+. A successful model-checking run applies only to the formal model and assumptions supplied.
