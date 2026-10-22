# Deploy a subgraph: index ERC-20 Transfer events

Task: index every `Transfer` event for an ERC-20 token (USDC on Ethereum
mainnet) and deploy the subgraph to Goldsky.

Status: **tested**. `graph codegen` and `graph build` run clean in this
folder. The `goldsky subgraph deploy` step is untested; it needs a Goldsky
API key.

## Prerequisites

- Node.js 18+.
- The Goldsky CLI: `curl https://goldsky.com | sh` (macOS/Linux) or
  `npm install -g @goldskycom/cli` (Windows).
- A Goldsky account. Run `goldsky login`.

## Files

- `subgraph.yaml`: manifest. Source is the USDC contract
  (`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`), start block `6082465`.
- `schema.graphql`: one entity, `Transfer`.
- `abis/ERC20.json`: minimal ABI with only the `Transfer` event.
- `src/mapping.ts`: the event handler. It writes one `Transfer` entity per
  log, keyed by transaction hash plus log index.

## Commands

Install the subgraph toolchain and generate types from the ABI and schema:

```bash
npm install
npm run codegen
```

Compile the subgraph to WASM:

```bash
npm run build
```

Deploy to Goldsky:

```bash
goldsky subgraph deploy erc20-transfers/1.0.0 --path .
```

## Expected output

`npm run codegen` prints:

```
Types generated successfully
```

`npm run build` prints:

```
Build completed: build/subgraph.yaml
```

`goldsky subgraph deploy` prints a progress bar while it packages and
uploads the build, then a dashboard URL for the deployed subgraph.

## What a Goldsky API key unlocks

- Running `goldsky subgraph deploy` and getting a hosted GraphQL endpoint.
- `goldsky subgraph log erc20-transfers/1.0.0` to tail indexing progress.
- Querying the live `Transfer` entities over GraphQL.

## Docs

- https://docs.goldsky.com/subgraphs/deploying-subgraphs
- https://docs.goldsky.com/reference/cli
