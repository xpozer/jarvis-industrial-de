# Contributing to jarvis-industrial-de

Thank you for contributing specialist modules to the JARVIS ecosystem.

This repository is intentionally narrower than the main product. Contributions should add domain depth without weakening safety, provenance, or compliance discipline.

## What belongs here

Good contributions are industrial skills that:

- solve a concrete workflow problem
- declare permissions honestly
- remain reviewable before side effects
- avoid protected standards text
- work in both the JARVIS-native and compatibility layouts where applicable

## Skill requirements

Every skill must:

- include a valid manifest using `schema/skill-manifest.schema.json`
- declare all permissions explicitly
- include handlers for both supported layouts when relevant
- include at least one smoke test
- provide German and English metadata
- avoid protected VDE, DIN, Beuth, and DGUV text
- avoid real customer data, credentials, or live SAP records

## Pull request flow

1. Fork the repository.
2. Create a focused branch such as `feat/cable-sizing-extension`.
3. Add or update the skill in `openjarvis-skillpack/` and `jarvis-native-plugin/`.
4. Run:

```bash
python tests/smoke_test.py
```

5. Open a pull request that explains:
   - what the skill does
   - which permissions it needs
   - which risk level applies
   - which tests were run
   - whether any compliance-sensitive assumptions are involved

## Review bar

Reviewers will check:

- manifest validity
- permission honesty
- side-effect behavior
- compliance with `compliance/COMPLIANCE_POLICY.md`
- whether the module adds reusable domain value rather than one-off local logic

## Compliance

Read `compliance/COMPLIANCE_POLICY.md` before contributing norm-adjacent content.

If a skill depends on a standard, reference the source and metadata; do not copy protected text into code, examples, or tests.
