# Google Flights MCP Server

MCP server for flight search and trip-planning workflows powered by `fast-flights`.

For Japanese documentation, see [README.ja.md](./README.ja.md).

## Features

- One-way and round-trip flight search
- Airport code/city lookup
- Suggested travel date helper
- Airport database refresh from a public CSV source

## Requirements

- Python 3.11+
- `uv` (recommended) or `pip`
- Playwright Chromium browser (required because this server uses `fetch_mode="local"`)

## Quick Start

```bash
cd /path/to/google-flights-mcp
uv sync
uv run playwright install chromium
uv run google-flights-mcp
```

Using `pip` instead:

```bash
cd /path/to/google-flights-mcp
python -m pip install -e .
python -m playwright install chromium
google-flights-mcp
```

## Integrations

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

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

Restart Claude Desktop after saving.

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

See [CODEX_GUIDE.md](./CODEX_GUIDE.md).

## Available Tools

- `search_flights`
- `airport_search`
- `get_travel_dates`
- `update_airports_database`

## Available Resources

- `airports://all`
- `airports://{code}`

## Available Prompts

- `plan_trip`
- `compare_destinations`

## Legacy Entrypoint

`src/flights-mcp-server.py` remains for backward compatibility and delegates to `google_flights_mcp.main()`.

## License

MIT
