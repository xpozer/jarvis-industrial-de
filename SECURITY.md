# Security Policy

`jarvis-industrial-de` contains specialist skill modules that may influence real workflows. Security and compliance therefore matter even when a module only drafts or calculates.

## Supported Versions

| Version | Support status |
|---|---|
| Current `main` branch | supported |
| Older snapshots | best effort only |

## Reporting a Vulnerability

Please do not open public issues for vulnerabilities.

Use GitHub private vulnerability reporting or contact the repository maintainer privately.

Please include:

- affected skill
- affected version or commit
- reproduction steps
- expected impact
- whether the issue affects JARVIS-native use, OpenJarvis-compatible use, or both

## Security Principles

- Permissions must be declared honestly in every manifest.
- Skills must not conceal network access, shell execution, or filesystem writes.
- Medium-risk actions should remain reviewable before side effects occur.
- No protected VDE, DIN, Beuth, or DGUV content may be copied into the repository.
- No real customer data, SAP order data, credentials, or private operating context may appear in examples or fixtures.
- Generated outputs are drafts or aids, not automatic legal or compliance decisions.

## Compliance-sensitive Modules

Modules that touch standards, offers, work proofs, or regulated calculations need extra review for:

- source attribution
- wording that could overstate authority
- protected text reuse
- unsafe assumptions
- hidden write paths

See `compliance/COMPLIANCE_POLICY.md` for the repository's handling rules.
