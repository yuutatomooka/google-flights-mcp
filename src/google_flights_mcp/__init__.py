import asyncio
import sys
import traceback

from .server import initialize_airports, mcp


def main() -> None:
    """Start the Google Flights MCP server."""
    print("Initializing airports database...", file=sys.stderr)
    asyncio.run(initialize_airports())

    print("Starting server - waiting for connections...", file=sys.stderr)
    try:
        mcp.run()
    except Exception as exc:
        print(f"Error running server: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        raise SystemExit(1) from exc
