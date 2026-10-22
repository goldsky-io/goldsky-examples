# Turbo pipeline: filter a curated dataset

Task: read the `base.erc20_transfers` dataset and keep only USDC
transfers, using a SQL transform. This is the fastest path to a working
Turbo pipeline: no ABI decoding, no custom contract.

Status: **partly tested**. `validate_pipeline.py` checks the YAML
structure offline and passes. `goldsky turbo apply` and `goldsky turbo
inspect` are untested; they need a Goldsky API key.

## Prerequisites

- The Goldsky CLI with the Turbo extension:
  https://docs.goldsky.com/turbo-pipelines/cli#installation
- A Goldsky account. Run `goldsky login`.

## Files

- `erc20-pipeline.yaml`: the pipeline. Source is the curated
  `base.erc20_transfers` dataset (version `1.2.0`), starting from
  `latest`. A SQL transform filters to the USDC contract on Base and
  projects 5 columns. The sink is `blackhole`, which discards output; it
  is for testing a pipeline shape before wiring a real sink.
- `validate_pipeline.py`: an offline check (no API key) that the YAML has
  the required keys and that the sink's `from` points at a real step.

## Commands

Offline check, no Goldsky account needed:

```bash
pip install pyyaml
python3 validate_pipeline.py erc20-pipeline.yaml
```

With a Goldsky account and CLI:

```bash
goldsky turbo apply erc20-pipeline.yaml
goldsky turbo inspect erc20-pipeline.yaml
goldsky turbo logs erc20-pipeline.yaml
```

## Expected output

`validate_pipeline.py` prints:

```
OK: erc20-pipeline.yaml is structurally valid YAML for a Turbo pipeline
```

`goldsky turbo apply` prints:

```
✓ Pipeline 'erc20-transfers' applied successfully
```

`goldsky turbo inspect` opens a terminal UI that shows USDC transfers
flowing through the `usdc_transfers` step in real time.

## What a Goldsky API key unlocks

- Running the pipeline against live Base data.
- `goldsky turbo inspect` live records at any step.
- Swapping the `blackhole_sink` for a real Postgres, ClickHouse, Kafka,
  webhook, or S3 sink.

## Docs

- https://docs.goldsky.com/turbo-pipelines/quickstart
- https://docs.goldsky.com/turbo-pipelines/pipeline-config
