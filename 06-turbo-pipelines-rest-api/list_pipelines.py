#!/usr/bin/env python3
"""List Turbo Pipelines via the Goldsky REST API.

Base URL and auth: https://docs.goldsky.com/api-reference/overview
"""
import os
import sys
import urllib.request
import urllib.error
import json

BASE_URL = "https://api.goldsky.com/api/v1"


def list_pipelines(api_key: str) -> dict:
    req = urllib.request.Request(
        f"{BASE_URL}/pipelines",
        headers={
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "goldsky-examples/1.0",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


if __name__ == "__main__":
    key = os.environ.get("GOLDSKY_API_KEY")
    if not key:
        print(
            "GOLDSKY_API_KEY not set. Create one at "
            "https://app.goldsky.com/dashboard/settings",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        pipelines = list_pipelines(key)
        print(json.dumps(pipelines, indent=2))
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
