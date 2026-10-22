#!/usr/bin/env bash
# Call Ethereum mainnet eth_blockNumber through Goldsky Edge RPC.
# Uses the shared public "demo" key: rate limited, fine for this example.
# Replace "demo" with your own key from https://app.goldsky.com for real use.
set -euo pipefail

KEY="${GOLDSKY_API_KEY:-demo}"

curl -s "https://edge.goldsky.com/standard/evm/1?key=${KEY}" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 1
  }'
echo
