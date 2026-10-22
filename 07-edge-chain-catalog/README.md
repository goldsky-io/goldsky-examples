# Edge: list supported chains and live health

Task: get a programmatic, up-to-date list of every chain Goldsky Edge RPC
supports, with ID, alias, block time, and health state, so you can check
coverage before you pick a chain.

Status: **tested**, live. `list_chains.py` ran against the real
`edge.goldsky.com` catalog endpoint and returned 239 chains.

## Prerequisites

- Python 3.8+, standard library only. No API key: the catalog endpoint is
  public.

## Files

- `list_chains.py`: fetches `https://edge.goldsky.com/`, which returns a
  JSON object keyed by tier (`standard`, and others as Goldsky adds
  them). Each entry has `id` (`evm:<chainId>`), `alias`, `blockTimeMs`,
  and `state`. The script prints a count, flags anything not reporting
  `state: OK`, and lists the first 10 chains.

## Commands

```bash
python3 list_chains.py
```

## Expected output

```
239 chains in the 'standard' tier
0 not reporting state=OK
  immutable-zkevm-testnet      id=evm:13473            block_time_ms=2000     state=OK
  aurora-mainnet               id=evm:1313161554       block_time_ms=612      state=OK
  ...
  ... and 229 more
```

The exact count and order change as Goldsky adds chains; the shape of
the output does not.

## What a Goldsky API key unlocks

- Nothing extra for this call: the catalog is public by design, so
  agents and scripts can discover coverage without signing up first.
- A key is needed for the next step, calling `edge.goldsky.com/standard/evm/{chainId}?key=...`
  with a JSON-RPC method against one of these chains (see
  `04-edge-rpc-call`).

## Docs

- https://docs.goldsky.com/edge-rpc/quickstart
- https://docs.goldsky.com/chains/supported-networks
