"""Load every schema file as a JSON Schema 2020-12 schema and validate the
version manifests against the version schema.

Needs python3 with pyyaml and jsonschema. Exits 0 when every file loads and
validates, and 1 otherwise, naming each failure.

    python3 schemas/load.py
"""
import glob
import os
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
problems = []
schemas = {}

for path in sorted(glob.glob(os.path.join(here, "*.schema.yaml"))):
    name = os.path.basename(path)
    with open(path, encoding="utf-8") as f:
        schema = yaml.safe_load(f)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as e:
        problems.append(f"{name}: {e.message}")
        continue
    if schema.get("$id") != f"tableaux/{name}":
        problems.append(f"{name}: $id is {schema.get('$id')!r}")
    schemas[name] = schema
    print(f"ok: schemas/{name} loads as {schema.get('$schema')}")

if "version.schema.yaml" in schemas:
    validator = Draft202012Validator(schemas["version.schema.yaml"], format_checker=FormatChecker())
    for path in (os.path.join(here, "version.yaml"), os.path.join(root, ".tableaux", "version.yaml")):
        with open(path, encoding="utf-8") as f:
            doc = yaml.safe_load(f)
        try:
            validator.validate(doc)
            print(f"ok: {os.path.relpath(path, root)} validates")
        except ValidationError as e:
            problems.append(f"{os.path.relpath(path, root)}: {e.message}")

for p in problems:
    print("problem:", p)
print(f"{len(schemas)} schema files loaded, {len(problems)} problems")
sys.exit(1 if problems else 0)
