# Edge RPC: a JSON-RPC call in under 2 minutes

Task: call `eth_blockNumber` on Ethereum mainnet through Goldsky Edge RPC,
with curl and with a JavaScript client (viem).

Status: **tested**, live, against the real Goldsky Edge RPC endpoint.
Both scripts ran against `https://edge.goldsky.com` with the shared public
`demo` key (see below) and returned the current block number.

## Prerequisites

- None, for the demo key. For real use, a Goldsky account
  (https://app.goldsky.com) and your own API key.
- Node.js 18+ for the viem script.

## Files

- `call.sh`: curl request to `edge.goldsky.com`.
- `call.mjs` + `package.json`: the same call with viem's
  `createPublicClient`.

## Commands

```bash
bash call.sh
```

```bash
npm install
node call.mjs
```

Both read `GOLDSKY_API_KEY` from the environment and fall back to the
public `demo` key, which every Edge RPC doc example uses. `demo` is rate
limited and for testing only.

## Expected output

`call.sh`:

```json
{"jsonrpc":"2.0","id":1,"result":"0x19084f5"}
```

`call.mjs`:

```
Block number: 26248437n
```

(the actual block number changes every call, since it is live mainnet
data)

## What a Goldsky API key unlocks

- A private rate limit instead of the shared `demo` key's limit.
- Access to Edge features beyond the `demo` tier: Boost caching, Fanout
  quorum reads, and usage metrics in the dashboard.

## Docs

- https://docs.goldsky.com/edge-rpc/quickstart
- https://docs.goldsky.com/edge-rpc/introduction
