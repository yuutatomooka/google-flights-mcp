# Google Flights MCP Server

`fast-flights` を使ってフライト検索を行う MCP サーバです。

## Features

- One-way / Round-trip flight search
- Airport code search
- Suggested travel dates
- Airport DB update (CSV fetch + local cache)

## Requirements

- Python 3.11+
- `uv` (recommended) or `pip`
- Playwright Chromium browser (required for `fetch_mode="local"`)

## Quick Start (Local)

```bash
cd /path/to/google-flights-mcp
uv sync
uv run playwright install chromium
uv run google-flights-mcp
```

`pip` の場合:

```bash
cd /path/to/google-flights-mcp
python -m pip install -e .
python -m playwright install chromium
google-flights-mcp
```

## Why Playwright Is Required

このサーバーは `fetch_mode="local"` で Google Flights を取得します。  
そのため `playwright` と `chromium` が未インストールだと検索が失敗します。

## Claude Desktop Integration

`~/Library/Application Support/Claude/claude_desktop_config.json`:

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

設定後に Claude Desktop を再起動してください。

## Codex Integration

Codex config (`~/.codex/config.toml`) 例:

```toml
[mcp_servers.google-flights]
command = "uv"
args = ["--directory", "/ABSOLUTE/PATH/google-flights-mcp", "run", "google-flights-mcp"]
```

または PATH に入っている場合:

```toml
[mcp_servers.google-flights]
command = "google-flights-mcp"
```

## Msty Studio Integration (STDIO / JSON)

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

互換のため `src/flights-mcp-server.py` も残しています（内部的には同じ `google_flights_mcp.main()` を呼び出します）。

## License

MIT
