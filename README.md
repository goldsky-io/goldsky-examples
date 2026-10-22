# Goldsky examples

Runnable example code for common tasks on [Goldsky](https://goldsky.com),
the real-time blockchain data and execution platform. Each folder is one
task, with its own README: what it does, what it needs, how to run it,
and what to expect.

Docs: https://docs.goldsky.com

## Examples

| Folder | Task | Status |
|---|---|---|
| [01-deploy-subgraph-from-source](./01-deploy-subgraph-from-source) | Deploy a subgraph that indexes ERC-20 `Transfer` events | tested (codegen + build) |
| [02-turbo-pipeline-contract-events-to-postgres](./02-turbo-pipeline-contract-events-to-postgres) | Turbo pipeline: decode every event a contract emits into Postgres | partly tested (YAML validated offline) |
| [03-turbo-pipeline-dataset-quickstart](./03-turbo-pipeline-dataset-quickstart) | Turbo pipeline: filter a curated dataset (USDC transfers on Base) | partly tested (YAML validated offline) |
| [04-edge-rpc-call](./04-edge-rpc-call) | Call Ethereum mainnet through Edge RPC, with curl and viem | tested (live, demo key) |
| [05-subgraph-webhook-receiver](./05-subgraph-webhook-receiver) | Receive and verify a subgraph-driven webhook | tested (local smoke test) |
| [06-turbo-pipelines-rest-api](./06-turbo-pipelines-rest-api) | List Turbo Pipelines with the REST API | tested (live, no-key checks) |
| [07-edge-chain-catalog](./07-edge-chain-catalog) | List every chain Edge RPC supports, with live health | tested (live) |

"Tested" means the example ran end to end in this repo without a Goldsky
API key, either because the step needs none (Edge RPC's public `demo`
key, the public OpenAPI spec, the public chain catalog, a local webhook
smoke test) or because it only covers build/codegen/validation steps
that do not call the Goldsky backend. "Partly tested" means the code
that needs a Goldsky API key is untested; each of those READMEs says
exactly what a key would let you run and verify.

## Prerequisites common to most examples

- The Goldsky CLI: `curl https://goldsky.com | sh` (macOS/Linux) or
  `npm install -g @goldskycom/cli` (Windows). See
  https://docs.goldsky.com/installation.
- A Goldsky account (https://app.goldsky.com) for any example that calls
  the Goldsky backend. Edge RPC, the public catalog, and the OpenAPI
  spec need no account.

## Source

Every command, YAML shape, and API path in these examples is copied or
adapted from a docs.goldsky.com page; each example's README links its
source page.
