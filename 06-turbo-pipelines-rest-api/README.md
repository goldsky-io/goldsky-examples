# Turbo Pipelines REST API: list pipelines from a script

Task: call the Goldsky REST API to list the Turbo Pipelines in a
project, without the CLI.

Status: **tested**, live, for the parts that do not need a key.
`check_spec.py` passes against the real `api.goldsky.com`: it confirms
the public OpenAPI spec documents `/pipelines`, and that an
unauthenticated call to `/pipelines` returns 401. `list_pipelines.py`
exits cleanly with a clear message when no key is set; the authenticated
call itself is untested.

## Prerequisites

- Python 3.8+, standard library only (no `pip install`).
- A Goldsky API key, from https://app.goldsky.com/dashboard/settings, to
  run `list_pipelines.py` for real.

## Files

- `list_pipelines.py`: sends `GET /pipelines` with a Bearer token from
  `GOLDSKY_API_KEY` and prints the JSON response.
- `check_spec.py`: no-key checks. Fetches the public OpenAPI spec at
  `/docs/openapi.json` and confirms it documents `/pipelines`. Then sends
  an unauthenticated request to `/pipelines` and confirms the API
  returns 401, not a different error or a redirect.

## Commands

No key needed:

```bash
python3 check_spec.py
```

With a Goldsky API key:

```bash
export GOLDSKY_API_KEY=your_key_here
python3 list_pipelines.py
```

## Expected output

`check_spec.py`:

```
OK: OpenAPI spec documents 53 paths, including /pipelines
OK: unauthenticated request to /pipelines returns 401, as documented
```

`list_pipelines.py` without a key:

```
GOLDSKY_API_KEY not set. Create one at https://app.goldsky.com/dashboard/settings
```

(exit code 1)

`list_pipelines.py` with a real key prints a JSON array of pipeline
objects (name, status, resource size, and so on).

## What a Goldsky API key unlocks

- Running `list_pipelines.py` for real, and the rest of the REST API:
  creating, deploying, pausing, and deleting Turbo Pipelines, plus
  subgraph and Edge endpoint management.
- The interactive API explorer at https://api.goldsky.com/api/v1/docs,
  which calls the API with your key from the browser.

## Docs

- https://docs.goldsky.com/api-reference/overview
- https://api.goldsky.com/api/v1/docs/openapi.json
