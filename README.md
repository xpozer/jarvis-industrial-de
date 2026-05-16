# jarvis-industrial-de

**Industrial skill pack for JARVIS.**

`jarvis-industrial-de` adds specialist electrical-planning workflows to the broader JARVIS ecosystem without turning the main product into a niche-only assistant.

It is designed for dual distribution:

- **JARVIS-native plugin** - loads into [`jarvis-windows-standalone`](https://github.com/xpozer/jarvis-windows-standalone)
- **OpenJarvis-compatible skill pack** - can be adapted for compatible skill loaders

## What it adds

| Skill | Purpose | Risk |
|---|---|---:|
| `vde-lookup` | VDE norm metadata lookup and source references | low |
| `sap-offer-builder` | SAP PM offer draft generation | medium |
| `lnw-generator` | Leistungsnachweis draft generation | medium |
| `cable-calc` | Cable cross-section calculations with formulas | low |
| `im-quizmaster` | IHK Industriemeister quiz support | low |

## Why it exists

The main JARVIS product is aimed at everyday Windows use: dictation, document Q&A, research, approvals, and memory control.

This plugin keeps specialist depth available without letting industrial workflows dominate the public product story. It is where domain-specific capability belongs.

## Installation

### As a JARVIS-native plugin

```bash
jarvis skills install https://github.com/xpozer/jarvis-industrial-de
```

### As an OpenJarvis-compatible skill pack

Copy `openjarvis-skillpack/` into the target assistant's skill directory.

## Compliance

This repository contains no protected VDE, DIN, Beuth, or DGUV text.

Norm-related modules should use metadata and source references only. See `compliance/COMPLIANCE_POLICY.md`.

## Relationship to JARVIS

- Main product: [`jarvis-windows-standalone`](https://github.com/xpozer/jarvis-windows-standalone)
- This repository: specialist industrial extension
- Design principle: useful everyday assistant first, domain plugins second

## License

MIT
