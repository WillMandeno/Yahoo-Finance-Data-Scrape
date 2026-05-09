# Yahoo Finance Data Scrape

Fetch historical stock price data from Yahoo Finance via HTTP and export to Excel spreadsheets — no API key or paid subscription required.

## Features

- Download historical price data for multiple stock tickers
- Configurable date ranges (relative periods or explicit start/end dates)
- Adjustable frequency (daily, weekly, monthly, or intraday)
- Automatic Excel export with clean formatting
- One ticker per sheet for easy organization

## Installation

```bash
pip install yfinance pandas openpyxl
```

## Usage

Edit the configuration in `fetch_prices.py`:

```python
TICKERS = ["AAPL", "MSFT", "GOOGL"]  # Stock symbols
PERIOD = "1y"                         # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
INTERVAL = "1d"                       # 1d, 1wk, 1mo, or intraday (1h, 15m, 5m, 1m)
OUTPUT_FILE = "stock_prices.xlsx"
```

Then run:

```bash
python3 fetch_prices.py
```

## Output

Each stock ticker gets its own sheet containing:
- Date
- Open, Close, High, Low prices
- Volume

## Notes

- No Yahoo Finance Gold subscription required
- Data sourced from Yahoo Finance public API
- Check ticker symbols on Yahoo Finance for availability
