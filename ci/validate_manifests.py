"""Validates all skill manifests against the JSON schema."""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("jsonschema not installed. Run: pip install jsonschema")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
SCHEMA_PATH = ROOT / "schema" / "skill-manifest.schema.json"

with open(SCHEMA_PATH) as f:
    schema = json.load(f)

errors = []
manifests_found = 0

for manifest_path in ROOT.rglob("manifest.json"):
    if ".git" in str(manifest_path):
        continue
    manifests_found += 1
    with open(manifest_path) as f:
        try:
            manifest = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"{manifest_path}: invalid JSON — {e}")
            continue
    try:
        jsonschema.validate(manifest, schema)
        print(f"OK  {manifest_path.relative_to(ROOT)}")
    except jsonschema.ValidationError as e:
        errors.append(f"{manifest_path}: {e.message}")
        print(f"ERR {manifest_path.relative_to(ROOT)}: {e.message}")

print(f"\n{manifests_found} manifests checked, {len(errors)} errors.")
if errors:
    sys.exit(1)
