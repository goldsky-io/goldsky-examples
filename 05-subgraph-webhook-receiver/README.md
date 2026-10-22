# Subgraph webhook receiver

Task: receive an HTTP POST from Goldsky every time a subgraph indexes a
matching entity change (for example, a trade event), and check the
`goldsky-webhook-secret` header before trusting the payload.

Status: **tested**, locally. `npm test` starts the server, sends one
request with the correct secret and one with the wrong secret, and checks
the responses (200 and 401).

## Prerequisites

- Node.js 18+.
- A deployed subgraph and a Goldsky webhook, to receive real traffic
  (not needed to run the included test).

## Files

- `src/server.js`: an Express endpoint at `POST /webhooks/goldsky`. It
  checks `goldsky-webhook-secret` against `GOLDSKY_WEBHOOK_SECRET`,
  rejects a mismatch with 401, and logs the entity name, operation, and
  row data on success.
- `src/server.test.js`: a dependency-free smoke test.

## Commands

Run the receiver:

```bash
npm install
GOLDSKY_WEBHOOK_SECRET=whs_your_secret npm start
```

Run the smoke test (starts its own in-process server, no network):

```bash
npm test
```

Create the matching webhook on Goldsky, pointing at your public URL (use
a tunnel such as ngrok for local testing):

```bash
goldsky subgraph webhook create my-subgraph/1.0.0 \
  --name my-trade-webhook \
  --entity Trade \
  --url https://your-host/webhooks/goldsky
```

The command prints the secret to set as `GOLDSKY_WEBHOOK_SECRET`.

## Expected output

`npm test`:

```
[goldsky webhook] entity=Trade op=INSERT { id: '0x1', price: '100' }
OK: webhook receiver accepts correct secret, rejects wrong secret
```

`npm start`, once a real webhook fires:

```
[goldsky webhook] entity=Trade op=INSERT { id: '0x3f2a...', price: '4200000000' }
```

## What a Goldsky API key unlocks

- Nothing extra for receiving webhooks: webhooks are enabled by default
  on every project. A Goldsky account is needed to run
  `goldsky subgraph webhook create` and get a real secret and live
  traffic.

## Docs

- https://docs.goldsky.com/subgraphs/guides/send-subgraph-driven-webhooks
- https://docs.goldsky.com/subgraphs/webhooks
