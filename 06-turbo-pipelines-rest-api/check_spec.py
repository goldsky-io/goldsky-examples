#!/usr/bin/env python3
"""No-key checks against the live Goldsky REST API.

1. Fetches the public OpenAPI spec and confirms it documents the
   pipelines endpoints this example script calls.
2. Confirms the API rejects unauthenticated requests with 401, proving
   the base URL and route are correct before you spend a real API key.
"""
import json
import sys
import urllib.error
import urllib.request

BASE_URL = "https://api.goldsky.com/api/v1"


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "goldsky-examples/1.0"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main() -> int:
    spec = fetch_json(f"{BASE_URL}/docs/openapi.json")
    paths = spec.get("paths", {})
    if "/pipelines" not in paths:
        print("FAIL: OpenAPI spec no longer documents /pipelines")
        return 1
    print(f"OK: OpenAPI spec documents {len(paths)} paths, including /pipelines")

    req = urllib.request.Request(
        f"{BASE_URL}/pipelines", headers={"User-Agent": "goldsky-examples/1.0"}
    )
    try:
        urllib.request.urlopen(req)
        print("FAIL: unauthenticated request to /pipelines did not raise")
        return 1
    except urllib.error.HTTPError as e:
        if e.code != 401:
            print(f"FAIL: expected 401 for unauthenticated request, got {e.code}")
            return 1
        print("OK: unauthenticated request to /pipelines returns 401, as documented")

    return 0


if __name__ == "__main__":
    sys.exit(main())
