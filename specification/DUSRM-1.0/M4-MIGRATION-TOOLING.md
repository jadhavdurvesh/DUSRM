# DUSRM 1.0 Preparation — Schema 0.1 to 0.2 Migration Tooling

**Work package:** WP4 — Schema 0.2 Semantic Validator and Migration Tooling  
**Status:** Implemented draft; non-normative  
**Implementation:** `scripts/migrate_schema_0_1_to_0_2.py`

## 1. Purpose and safety model

The migrator converts a schema 0.1-draft description to a schema 0.2-draft description while producing a separate migration report.

It validates the input against schema 0.1 first. It never edits or overwrites the source file. It does not silently guess missing endpoint kinds, evidence strength, profile compatibility, layer applicability, or event semantics.

Schema 0.1 and schema 0.2 are structurally different; changing only the schema version is not a migration.

## 2. Command

A conservative migration attempt:

```bash
python scripts/migrate_schema_0_1_to_0_2.py \
  path/to/source-0.1.json \
  --output build/description-0.2.json \
  --report build/migration-report.json
```

The default behavior writes the report but refuses to emit a description if ambiguous mappings or review warnings remain.

To deliberately emit a structurally valid review draft with ambiguous/unmappable records omitted and listed in the report:

```bash
python scripts/migrate_schema_0_1_to_0_2.py \
  path/to/source-0.1.json \
  --output build/description-0.2-review-draft.json \
  --report build/migration-report.json \
  --allow-incomplete
```

The `--allow-incomplete` flag does not make the migration complete. It only authorizes a draft output with explicit review findings.

## 3. Exit codes

- **0:** migration has no warnings, blockers or dropped items; output emitted.
- **1:** input or output fails structural schema validation.
- **2:** review is required or input/schema/report processing could not be completed. With `--allow-incomplete`, exit 2 may accompany a deliberately emitted review draft and report.

Always read the migration report before using the output.

## 4. Conversion behavior

The migrator:
- preserves description identity, title and summary where possible;
- creates a stable boundary identifier for the migrated description;
- converts environment participants and elements while marking their missing category/role information for review;
- preserves responsibility primary-layer assignments;
- converts realization records to the schema 0.2 allocation structure;
- creates explicit State records for finite state-variable values and transition endpoints when the legacy mapping is unambiguous;
- converts participant and relationship references only when their target kind is determinable;
- maps the legacy `realizes` relationship to a Realization record only when it clearly connects an Element to a Responsibility;
- carries evidence source URI/revision while deliberately not promoting its legacy status to evidence strength;
- sets all layer applicability to unknown rather than inferring it;
- maps claim records only when a typed subject scope is available;
- preserves namespaced extension data but warns that extension semantics require review.

## 5. Ambiguity handling

The migrator reports:
- unresolved identifiers;
- identifiers that collide across legacy object kinds;
- relationships whose endpoint kinds are not represented in schema 0.1;
- ambiguous legacy `realizes` relationships;
- transitions without a unique state-variable/subject mapping;
- claims without a typed subject scope;
- unsupported relationship types;
- legacy status fields that cannot be mapped to one schema 0.2 status dimension;
- dropped records and the reason each was omitted.

It does not invent an Execution for a legacy `performs` relationship, an Event from an untyped trigger string, or a Requirement/Specification from a name alone.

## 6. Migration report

The JSON report includes:
- source and target description identifiers;
- whether the conversion was complete;
- warning, blocker and dropped-item counts;
- each warning and blocker with a path and explanation;
- every dropped record and why it was omitted;
- a preservation statement confirming the input was not modified.

The output and report must be reviewed together. A schema 0.2 structural pass and semantic-validator pass do not establish semantic equivalence with the original schema 0.1 description.

## 7. Known limitations

- The tool handles the current schema 0.1 object set and the mappings documented in WP3; it is not a universal converter for arbitrary custom extensions.
- Category and role assignments cannot be inferred reliably from legacy free-text kinds.
- The legacy status enum is overloaded; conversion is intentionally conservative and generates review warnings.
- Some relationship types cannot be migrated because schema 0.1 lacks the corresponding typed objects.
- Evidence relevance and sufficiency require human assessment.
- Profile compatibility is not promoted.
- Migration is a draft-generation aid, not approval of DUSRM 1.0 conformance.

## 8. Version isolation

The migrator uses schema 0.1 as input and schema 0.2 as output. It does not change either schema, and it does not modify ANANTA, FireBot, SAND OS, or any other system repository.
