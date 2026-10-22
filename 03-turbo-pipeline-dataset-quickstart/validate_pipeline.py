#!/usr/bin/env python3
"""Offline structural check for a Turbo pipeline YAML.

This does not call the Goldsky API. It checks the shape that
`goldsky turbo validate` expects, so a syntax error is caught before you
spend a round trip on the real CLI or a Goldsky API key.
"""
import sys

import yaml

REQUIRED_TOP_LEVEL = ("name", "resource_size", "sources", "sinks")
REQUIRED_SOURCE_FIELDS = ("type",)
REQUIRED_SINK_FIELDS = ("type", "from")


def check(path: str) -> int:
    with open(path) as f:
        config = yaml.safe_load(f)

    errors = []
    for key in REQUIRED_TOP_LEVEL:
        if key not in config:
            errors.append(f"missing top-level key: {key}")

    for name, source in config.get("sources", {}).items():
        for field in REQUIRED_SOURCE_FIELDS:
            if field not in source:
                errors.append(f"source '{name}' missing field: {field}")

    for name, sink in config.get("sinks", {}).items():
        for field in REQUIRED_SINK_FIELDS:
            if field not in sink:
                errors.append(f"sink '{name}' missing field: {field}")
        from_ref = sink.get("from")
        known = set(config.get("sources", {})) | set(config.get("transforms", {}) or {})
        if from_ref and from_ref not in known:
            errors.append(f"sink '{name}' references unknown step: {from_ref}")

    if errors:
        print(f"FAIL: {path}")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {path} is structurally valid YAML for a Turbo pipeline")
    return 0


if __name__ == "__main__":
    sys.exit(check(sys.argv[1] if len(sys.argv) > 1 else "erc20-pipeline.yaml"))
