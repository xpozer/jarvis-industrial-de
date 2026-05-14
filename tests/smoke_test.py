"""Basic smoke tests for all skill modules."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
REQUIRED_FIELDS = ["schema_version", "id", "name", "version", "description", "permissions", "risk_level", "entry"]

failures = []

for manifest_path in ROOT.rglob("manifest.json"):
    if ".git" in str(manifest_path):
        continue
    with open(manifest_path) as f:
        manifest = json.load(f)

    for field in REQUIRED_FIELDS:
        if field not in manifest:
            failures.append(f"{manifest_path}: missing field '{field}'")

    if manifest.get("risk_level") not in ("low", "medium", "high"):
        failures.append(f"{manifest_path}: invalid risk_level")

    entry = ROOT / manifest_path.parent / manifest.get("entry", "")
    if not entry.exists():
        failures.append(f"{manifest_path}: entry point '{manifest.get('entry')}' not found")

    compliance = manifest.get("compliance_notice", "")
    if not compliance:
        failures.append(f"{manifest_path}: missing compliance_notice")

print(f"Smoke tests: {len(failures)} failures")
for f in failures:
    print(f"  FAIL: {f}")

if failures:
    sys.exit(1)
else:
    print("All smoke tests passed.")
