# Google Flights MCP Server

Flight search and travel-planning MCP functionality built on top of `fast-flights`. This repo wraps FastMCP to expose tools for searching fares, looking up airports, and generating travel prompts; the underlying Google Flights fetch uses `fetch_mode="local"` to avoid third-party tokens.

Refer to [README.ja.md](./README.ja.md) for the Japanese translation.

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

- One-way and round-trip flight search with prioritised results tagging.
- Airport code / city lookups using the cached database.
- Suggested travel date helper that returns a departure/return range.
- Airport database refresh from the upstream CSV source via `update_airports_database`.

## Requirements

- Python 3.11+
- `uv` (recommended) or `pip`
- Playwright Chromium browser (required because this server scrapes Google Flights locally)

## Quick Start

```bash
cd /path/to/google-flights-mcp
uv sync
uv run playwright install chromium
uv run google-flights-mcp
```

If you prefer plain `pip`:

```bash
cd /path/to/google-flights-mcp
python -m pip install -e .
python -m playwright install chromium
google-flights-mcp
```

`google-flights-mcp` is a console script that launches `python -m google_flights_mcp`, initialises the airport cache, and keeps FastMCP running for incoming tool invocations.

## Integrations

### Claude Desktop

Add this block to `~/Library/Application Support/Claude/claude_desktop_config.json`:

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

Restart Claude Desktop afterwards.

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

See [CODEX_GUIDE.md](./CODEX_GUIDE.md) for the prompt that automates cloning, dependency install, and MCP configuration.

## Tools, Resources & Prompts

- Tools: `search_flights`, `airport_search`, `get_travel_dates`, `update_airports_database`
- Resources: `airports://all`, `airports://{code}`
- Prompts: `plan_trip`, `compare_destinations`

## Legacy Entrypoint

`src/flights-mcp-server.py` remains for backward compatibility and delegates to `google_flights_mcp.main()`.

## Acknowledgments

Thanks to `salamentic` for the original Flight Planner MCP server that made this fork possible.

## License

MIT
