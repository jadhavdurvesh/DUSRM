# Validation

DUSRM must be evaluated against systems with different characteristics. Case studies should test whether the model can describe structure, behavior, state, resources, interfaces, constraints, failures, and lifecycle without forcing product-specific abstractions.

## Current structural validation

See [DUSRM 0.3 Structural Validation Matrix](STRUCTURE-VALIDATION-MATRIX.md), which contains preliminary mappings for:
- A small standalone application.
- ANANTA, with unknown internal details explicitly marked.
- FireBot, with planned capabilities distinguished from implemented and verified behavior.

These mappings are exploratory and are not evidence of conformance or safety.

## General case-study method

For each case study, record:
- system of interest and boundary;
- model mapping;
- known, planned, inferred, unknown, and not-applicable claims;
- unmapped concepts and ambiguities;
- assumptions and evidence;
- proposed changes to DUSRM.

Do not infer unverified implementation details from project names or high-level descriptions.
