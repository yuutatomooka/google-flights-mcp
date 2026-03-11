# Google Flights MCP Server

[![Stars](https://img.shields.io/github/stars/yuutatomooka/google-flights-mcp?style=social)](https://github.com/yuutatomooka/google-flights-mcp)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
<br>
Flight search and travel-planning MCP functionality built on `fast-flights`. This project already bundles Claude/Msty/Codex guides, makes `fetch_mode="local"` the default, and keeps a single `uv`/Python entry point for tooling.

日本語ドキュメントは [README.ja.md](./README.ja.md) です。

## ⭐ Quick actions

1. `uv run google-flights-mcp` – launches the FastMCP server after loading the airport cache.
2. `uv run playwright install chromium` – required before the flight search tools work.
3. Use the Codex prompt in [CODEX_GUIDE.md](./CODEX_GUIDE.md) when onboarding this repo for automation tasks.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Integrations](#integrations)
- [Tools, Resources & Prompts](#tools-resources--prompts)
- [Legacy Entrypoint](#legacy-entrypoint)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Features

- One-way and round-trip flight search with best-option tagging.
- Airport/city lookup backed by a local cache (`airports_cache.json`).
- `get_travel_dates` helper for quick date suggestions.
- `update_airports_database` refreshes the cache directly from the upstream CSV.

## Requirements

- Python 3.11+
- `uv` (recommended) or `pip`
- Playwright & Chromium (initialise via `playwright install chromium` before running the server)

## Quick Start

```bash
cd /path/to/google-flights-mcp
uv sync
uv run playwright install chromium
uv run google-flights-mcp
```

Or with direct `pip`:

```bash
cd /path/to/google-flights-mcp
python -m pip install -e .
python -m playwright install chromium
google-flights-mcp
```

The `google-flights-mcp` console script simply runs `python -m google_flights_mcp`, which initialises airports and launches FastMCP for incoming tool calls.

## Integrations

### Claude Desktop

Insert or update this block inside `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "google-flights": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/google-flights-mcp",
        "run",
        "google-flights-mcp"
      ]
    }
  }
}
```

Restart Claude Desktop after editing.

### Msty Studio (STDIO / JSON)

```json
{
  "command": "uv",
  "args": [
    "--directory",
    "/ABSOLUTE/PATH/google-flights-mcp",
    "run",
    "google-flights-mcp"
  ]
}
```

### Codex

See [CODEX_GUIDE.md](./CODEX_GUIDE.md) for the prompt that clones this repo, installs dependencies, and updates your Codex MCP config automatically.

## Tools, Resources & Prompts

- Tools: `search_flights`, `airport_search`, `get_travel_dates`, `update_airports_database`.
- Resources: `airports://all`, `airports://{code}`.
- Prompts: `plan_trip`, `compare_destinations`.

## Legacy Entrypoint

`src/flights-mcp-server.py` is retained for compatibility and delegates to `google_flights_mcp.main()`.

## Acknowledgments

Thanks to `salamentic` for the original Flight Planner MCP server that made this fork possible.

## License

MIT
