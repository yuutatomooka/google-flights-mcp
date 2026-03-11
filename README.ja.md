# Google Flights MCP Server

`fast-flights` を利用した、フライト検索向け MCP サーバです。

英語版ドキュメントは [README.md](./README.md) を参照してください。

## 機能

- 片道 / 往復フライト検索
- 空港コード・都市名検索
- 出発日 / 帰着日の提案
- 公開CSVからの空港データ更新

## 動作要件

- Python 3.11+
- `uv`（推奨）または `pip`
- Playwright Chromium（本サーバは `fetch_mode="local"` を使うため必須）

## クイックスタート

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

## 連携設定

### Claude Desktop

`~/Library/Application Support/Claude/claude_desktop_config.json` に追加:

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

保存後、Claude Desktop を再起動してください。

### Msty Studio（STDIO / JSON）

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

Codexでの利用ガイド（自動セットアップ用プロンプト付き）は [CODEX_GUIDE.md](./CODEX_GUIDE.md) を参照してください。

## 利用可能な Tools

- `search_flights`
- `airport_search`
- `get_travel_dates`
- `update_airports_database`

## 利用可能な Resources

- `airports://all`
- `airports://{code}`

## 利用可能な Prompts

- `plan_trip`
- `compare_destinations`

## 互換エントリポイント

`src/flights-mcp-server.py` は後方互換のため残しています。内部では `google_flights_mcp.main()` を呼び出します。

## ライセンス

MIT
