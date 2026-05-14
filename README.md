# jarvis-industrial-de

Industrial skill pack for JARVIS and OpenJarvis-compatible assistants.

Dual distribution:
- **OpenJarvis skill pack** — compatible with OpenJarvis-style skill loaders
- **JARVIS-native plugin** — loads directly into jarvis-windows-standalone via B8 SkillCompat

## Modules

| Skill | Description | Risk |
|-------|-------------|------|
| `vde-lookup` | VDE norm metadata lookup and source references | low |
| `sap-offer-builder` | SAP PM offer draft generator | medium |
| `lnw-generator` | Leistungsnachweis draft generator | medium |
| `cable-calc` | Cable cross-section calculator with formulas | low |
| `im-quizmaster` | IHK Industriemeister quiz (BwHa, MIKP, ZIB, NTG) | low |

## Installation

### As JARVIS-native plugin (requires B8 SkillCompat)

```
jarvis skills install https://github.com/xpozer/jarvis-industrial-de
```

### As OpenJarvis skill pack

Copy `openjarvis-skillpack/` into your OpenJarvis skills directory.

## Compliance

This plugin contains no protected VDE, DIN, Beuth or DGUV text.
All norm references are metadata and source citations only.
See `compliance/COMPLIANCE_POLICY.md`.

## License

MIT
