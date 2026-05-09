# Global configuration for Yahoo Finance data fetching

# Stock tickers to fetch data for
TICKERS = ["WOW.AX", "^AXJO"]

# ── Price Data Configuration ───────────────────────────────────────────────────
# Choose ONE of the following date options:
# Option A — relative period: 1d 5d 1mo 3mo 6mo 1y 2y 5y 10y ytd max
PRICE_PERIOD = "5y"

# Option B — explicit date range (set PRICE_PERIOD = None to use these)
PRICE_START_DATE = None  # e.g., "2024-01-01"
PRICE_END_DATE = None    # None = today

# Data frequency: 1d (daily), 1wk (weekly), 1mo (monthly), or intraday (1h, 15m, 5m, 1m)
PRICE_INTERVAL = "1mo"

# ── Dividend Data Configuration ────────────────────────────────────────────────
# Optional: Filter dividends by date range (None = all available)
DIVIDEND_START_DATE = "2021-06-01"  # e.g., "2020-01-01"
DIVIDEND_END_DATE = None    # e.g., "2026-12-31"

# ── Output Configuration ──────────────────────────────────────────────────────
OUTPUT_FILE = "output.xlsx"
