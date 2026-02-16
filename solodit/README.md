# Solodit Move Findings Exporter

This utility walks the Solodit Findings API for every Move-language report and writes each finding to an `audit/issue_XXXXX.md` file. The exporter mirrors the numbering scheme shown in the prompt, so you can re-run it to append newly discovered reports without reprocessing existing ones.

## Prerequisites

- Python 3.9+
- A Solodit API key stored in a local `.env` file or exported as `SOLODIT_API_KEY`

```
SOLODIT_API_KEY=sk_your_key_here
```

## Setup

```bash
cd solodit
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py --page-size 100 --output-dir audit
```

Helpful flags:

- `--dry-run` — list the numbered findings without writing files.
- `--max-pages` — stop after a certain number of API pages (useful during testing).
- `--start-index` — override the automatic `issue_XXXXX` numbering if you need a custom starting point.

Each generated markdown file includes a YAML-style front matter block with metadata (impact, protocol, finder handles, etc.) followed by the summary and full report body from Solodit.

## Notes

- The script automatically backs off when the API rate limit (`429`) is hit.
- Existing `issue_XXXXX.md` files are detected so numbering continues from the highest existing index.
- Keep your API key private and never commit your `.env` file.
