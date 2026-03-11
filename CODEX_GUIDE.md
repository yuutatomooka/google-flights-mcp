# Codex Guide

This guide is intentionally prompt-first.

## Use This Flow

1. Clone this repository.
2. Add the cloned path to your Codex workspace context.
3. Paste the prompt below into Codex.

## Codex Auto-Setup Prompt

```text
Set up this repository as a working Google Flights MCP server in my current environment.

Goals:
- Install project dependencies.
- Ensure Playwright Chromium is installed.
- Install the package in editable mode.
- Verify the Python package imports cleanly.
- Update my Codex MCP config so I can call this server as `google-flights`.

Requirements:
- Use this repository path as-is (do not ask me to move files).
- Prefer `uv` if available; otherwise use `python -m pip`.
- Use a Codex MCP config entry that launches:
  command = "uv"
  args = ["--directory", "<THIS_REPO_ABSOLUTE_PATH>", "run", "google-flights-mcp"]
- Keep any existing MCP servers in my config intact.
- If `google-flights` already exists, update it safely instead of duplicating.

Validation:
- Show me what changed in config files.
- Confirm that `google-flights-mcp` starts without import errors.
- Summarize any warnings and how to fix them.
```

## Notes

- The server uses `fetch_mode="local"`, so Playwright Chromium is required.
- If your environment has multiple Python installations, ensure Codex and this project use the same one.
