# Turbo pipeline: decode contract events into Postgres

Task: stream every event the Bored Ape Yacht Club contract emits on
Ethereum into a Postgres table, decoded by event name and parameters.

Status: **partly tested**. `validate_pipeline.py` checks the YAML
structure offline and passes. `goldsky turbo validate` and
`goldsky turbo apply` are untested; they need a Goldsky API key and a
Postgres connection string.

## Prerequisites

- The Goldsky CLI with the Turbo extension:
  https://docs.goldsky.com/turbo-pipelines/cli#installation
- A Goldsky account. Run `goldsky login`.
- A Postgres database (for example a free Neon instance).
- An Etherscan API key, to fetch the BAYC ABI at pipeline run time.

## Files

- `bored-ape-events.yaml`: the pipeline. Source is `ethereum.raw_logs`
  (every log on Ethereum). Two SQL transforms decode BAYC logs with
  `_gs_log_decode` and `_gs_fetch_abi`, then flatten the decoded event
  into columns. The sink writes to `public.bored_ape_events`.
- `validate_pipeline.py`: an offline check (no API key) that the YAML has
  the required `name`, `resource_size`, `sources`, and `sinks` keys, and
  that each sink's `from` points at a real source or transform.

## Commands

Offline check, no Goldsky account needed:

```bash
pip install pyyaml
python3 validate_pipeline.py bored-ape-events.yaml
```

With a Goldsky account and CLI:

```bash
goldsky secret create BAYC_POSTGRES
# paste: postgres://username:password@host:port/database

goldsky turbo validate bored-ape-events.yaml
goldsky turbo apply bored-ape-events.yaml
```

Replace `YOUR_KEY` in the SQL transform with a real Etherscan API key
before you deploy.

## Expected output

`validate_pipeline.py` prints:

```
OK: bored-ape-events.yaml is structurally valid YAML for a Turbo pipeline
```

`goldsky turbo apply` prints `Pipeline 'bored-ape-events' applied
successfully`. Once it runs, query Postgres:

```sql
SELECT event_signature, count(*)
FROM public.bored_ape_events
GROUP BY event_signature
ORDER BY count(*) DESC;
```

## What a Goldsky API key unlocks

- Running `goldsky turbo apply` against the real Goldsky backend.
- `goldsky turbo inspect bored-ape-events -n bayc_events` to watch
  decoded events live before they land in Postgres.
- `goldsky turbo logs bored-ape-events -f` to tail runtime logs.

## Docs

- https://docs.goldsky.com/turbo-pipelines/guides/export-events-to-database
- https://docs.goldsky.com/turbo-pipelines/pipeline-config
