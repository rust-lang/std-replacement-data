#!/usr/bin/env python3
"""Bundle the per-crate TOML files in `data/` into `build/all.json`."""

import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
BUILD_DIR = ROOT / "build"

REQUIRED_FIELDS = {"description", "url"}


def validate(path, entry):
    """Return a list of problems with the fields of a single entry."""
    fields = set(entry)

    errors = []
    for name in sorted(REQUIRED_FIELDS - fields):
        errors.append(f"{path.name}: missing field: {name}")
    for name in sorted(fields - REQUIRED_FIELDS):
        errors.append(f"{path.name}: unexpected field: {name}")

    return errors


def main():
    crates = {}
    errors = []
    for path in sorted(DATA_DIR.glob("*.toml")):
        try:
            with path.open("rb") as f:
                entry = tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            errors.append(f"{path.name}: invalid TOML: {e}")
            continue

        problems = validate(path, entry)
        if problems:
            errors.extend(problems)
            continue

        crates[path.stem] = {
            "description": entry["description"].strip(),
            "url": entry["url"],
        }

    if errors:
        for error in errors:
            print(error, file=sys.stderr)

        sys.exit(1)

    BUILD_DIR.mkdir(exist_ok=True)
    out = BUILD_DIR / "all.json"
    with out.open("w") as f:
        json.dump(crates, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"Wrote {len(crates)} crates to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
