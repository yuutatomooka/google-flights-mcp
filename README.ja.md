# Google Flights MCP Server

[![スター](https://img.shields.io/github/stars/yuutatomooka/google-flights-mcp?style=social)](https://github.com/yuutatomooka/google-flights-mcp)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
<br>
`fast-flights` ベースで作られたフライト検索向け MCP サーバです。`fetch_mode="local"` で Google Flights をスクレイピングし、Claude／Msty／Codex 向けのガイドも同梱しています。

英語版は [README.md](./README.md) を確認してください。

## ⭐ クイックアクション

1. `uv run google-flights-mcp` で FastMCP を起動、空港データをキャッシュ。
2. `uv run playwright install chromium` を先に実行すると検索が失敗しません。
3. Codex では [CODEX_GUIDE.md](./CODEX_GUIDE.md) のプロンプトを貼って導入。

## 目次

- [機能](#機能)
- [動作要件](#動作要件)
- [クイックスタート](#クイックスタート)
- [連携](#連携)
- [Tools/Resources/Prompts](#toolsresources--prompts)
- [互換エントリポイント](#互換エントリポイント)
- [謝辞](#謝辞)
- [ライセンス](#ライセンス)

## 機能

- 片道／往復検索で `BEST OPTION` ラベル付きの結果を返す。
- 空港コード・都市検索をローカルキャッシュ(`airports_cache.json`)で高速化。
- `get_travel_dates` による出発/帰着日の自動提案。
- `update_airports_database` でCSVから最新データを定期取得可能。

## 動作要件

- Python 3.11+
- `uv`（推奨）または `pip`
- Playwright Chromium (`playwright install chromium`)：ローカルで Google Flights を取得するため必須です。

## クイックスタート

```bash
cd /path/to/google-flights-mcp
uv sync
uv run playwright install chromium
uv run google-flights-mcp
```

`pip` を使う場合:

```bash
cd /path/to/google-flights-mcp
python -m pip install -e .
python -m playwright install chromium
google-flights-mcp
```

`google-flights-mcp` は `python -m google_flights_mcp` をラップし、空港データの読み込みと FastMCP サーバの起動を行います。

## 連携

### Claude Desktop

`~/Library/Application Support/Claude/claude_desktop_config.json` に以下を追加してください:

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

保存後に Claude Desktop を再起動します。

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

[CODEX_GUIDE.md](./CODEX_GUIDE.md) にあるプロンプトを使うと、クローン＆セットアップが自動化されます。

## Tools/Resources & Prompts

- Tools: `search_flights`, `airport_search`, `get_travel_dates`, `update_airports_database`
- Resources: `airports://all`, `airports://{code}`
- Prompts: `plan_trip`, `compare_destinations`

## 互換エントリポイント

`src/flights-mcp-server.py` は互換性維持のため残し、`google_flights_mcp.main()` を呼び出します。

## 謝辞

このプロジェクトは `salamentic` 氏の Flight Planner MCP サーバを基に構築しました。オリジナル実装への感謝を記します。

## ライセンス

MIT
