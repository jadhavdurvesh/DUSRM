# WP7 Proposal — SAND OS Host-Side DUSRM CI Adoption

**Status:** Proposed only — not installed in SAND OS  
**Target:** `jadhavdurvesh/sand-os`  
**Required authorization:** explicit owner approval before any SAND repository change

## 1. Recommendation

Adopt DUSRM as an external, host-side architecture-description validation step. Keep the DUSRM JSON description and portable validator as reviewable development artifacts. Do not compile DUSRM into the kernel, run it inside the guest, or make SAND boot/image generation depend on it.

## 2. Proposed location

If approved, copy the reviewed kit into a dedicated location such as:

`tools/dusrm-sand-os/`

This is a proposal; the current SAND OS repository has not been changed.

## 3. Proposed host-side CI commands

After the reviewed kit is copied into SAND OS, a future GitHub Actions job could run:

```yaml
- name: Set up Python for DUSRM architecture validation
  uses: actions/setup-python@v5
  with:
    python-version: "3.13"

- name: Install pinned DUSRM validation dependency
  run: python -m pip install -r tools/dusrm-sand-os/requirements.txt

- name: Verify DUSRM validation bundle
  run: python tools/dusrm-sand-os/verify_bundle.py

- name: Validate SAND OS architecture description
  run: |
    python tools/dusrm-sand-os/validate.py \
      --report build/dusrm-validation-report.json

- name: Upload DUSRM architecture report
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: dusrm-sand-os-architecture-report
    path: build/dusrm-validation-report.json
    if-no-files-found: warn
```

This is a CI proposal only. It has not been committed or tested in the SAND OS workflow.

## 4. Failure policy

- Bundle-integrity mismatch: fail the architecture-validation step.
- JSON Schema error: fail the architecture-validation step.
- DUSRM semantic error: fail the architecture-validation step.
- Compatibility warning: report and retain by default while compatibility remains `not-assessed`.
- Strict release gate: use `--strict-compatibility` only after the profile has an explicit reviewed disposition.
- DUSRM service unavailable: SAND build and boot must remain possible; no network service or online DUSRM API is required at runtime.

The initial recommendation is to keep this as a separate validation job rather than coupling it to the kernel compilation or QEMU boot job. The project owner may later decide whether it is a required check.

## 5. Update policy

- Pin the kit manifest and DUSRM source revision.
- Update the kit only from a reviewed DUSRM commit.
- Verify all recorded Git blob hashes before use.
- Update the SAND architecture description when authoritative SAND documentation or implementation changes.
- Review changes to the schema, semantic validator or profile before accepting updated validation results.
- Never silently promote profile compatibility or subsystem maturity.

## 6. Non-goals

This integration does not:
- add a kernel module or syscall;
- define or change Veyra;
- change SAPP executable format or loader;
- change SANDFS or block-storage semantics;
- change boot stages, scheduler or memory management;
- replace SAND's compiler, build pipeline, QEMU tests or hardware tests;
- provide a production security certification.

## 7. Approval gate

Before implementation, obtain explicit authorization for:
1. adding the kit directory to SAND OS;
2. adding a separate host-side CI workflow or job;
3. selecting whether the job is informational or required;
4. defining who owns updates to the model and evidence;
5. choosing whether the canonical architecture JSON is stored in SAND, DUSRM or mirrored with a pin.

Until that decision is made, leave SAND OS unchanged.
