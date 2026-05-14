# Contributing to jarvis-industrial-de

## Skill Contributions

Skills must:
- include a valid manifest (see `schema/skill-manifest.schema.json`)
- declare all permissions honestly
- contain no protected norm text (VDE, DIN, Beuth, DGUV)
- include at least one smoke test
- provide `de` and `en` metadata

## Pull Request Process

1. Fork the repository
2. Create a branch: `feat/skill-name`
3. Add skill to `openjarvis-skillpack/` and `jarvis-native-plugin/`
4. Run `python tests/smoke_test.py`
5. Open a PR with a description of what the skill does

## Compliance

See `compliance/COMPLIANCE_POLICY.md` before contributing norm-adjacent content.
