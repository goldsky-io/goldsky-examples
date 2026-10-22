#!/usr/bin/env python3
"""List every chain Goldsky Edge RPC supports, with live health status.

No API key needed: https://edge.goldsky.com is a public, unauthenticated
catalog endpoint.
"""
import json
import sys
import urllib.request

CATALOG_URL = "https://edge.goldsky.com/"


def fetch_catalog() -> dict:
    req = urllib.request.Request(
        CATALOG_URL, headers={"User-Agent": "goldsky-examples/1.0"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main() -> int:
    catalog = fetch_catalog()
    standard = catalog.get("standard", [])
    unhealthy = [c for c in standard if c.get("state") != "OK"]

    print(f"{len(standard)} chains in the 'standard' tier")
    print(f"{len(unhealthy)} not reporting state=OK")

    for chain in standard[:10]:
        block_time = chain.get("blockTimeMs", "n/a")
        print(f"  {chain['alias']:<28} id={chain['id']:<20} "
              f"block_time_ms={block_time:<8} state={chain['state']}")

    if len(standard) > 10:
        print(f"  ... and {len(standard) - 10} more")

    return 0


if __name__ == "__main__":
    sys.exit(main())
