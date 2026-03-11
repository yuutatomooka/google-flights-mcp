#!/usr/bin/env python3
"""Legacy entrypoint kept for backward compatibility.

Use `google-flights-mcp` or `python -m google_flights_mcp` for normal operation.
"""

from google_flights_mcp import main


if __name__ == "__main__":
    main()
