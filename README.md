# Yahoo Finance Data Scrape

Fetch historical stock price data from Yahoo Finance via HTTP and export to Excel spreadsheets — no API key or paid subscription required.

## Features

- Download historical price data for multiple stock tickers
- Fetch dividend history for stocks
- Configurable date ranges (relative periods or explicit start/end dates)
- Adjustable frequency (daily, weekly, monthly, or intraday)
- Automatic Excel export with clean formatting
- Centralized configuration for all scripts
- Single output file with multiple sheets

## Installation

```bash
pip install yfinance pandas openpyxl
```

## Usage

Edit configuration once in `config.py`:

```python
TICKERS = ["AAPL", "MSFT", "JNJ"]
PRICE_PERIOD = "1y"                    # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
PRICE_INTERVAL = "1d"                  # 1d, 1wk, 1mo, or intraday (1h, 15m, 5m, 1m)
OUTPUT_FILE = "output.xlsx"
```

Run price fetcher:
```bash
python3 fetch_prices.py
```

Run dividend fetcher:
```bash
python3 fetch_dividends.py
```

Both scripts write to the same `output.xlsx` file with separate sheets for prices and dividends.

## Output

Excel file contains:

**Price Sheets** — One sheet per ticker with:
- Date
- Open, Close, High, Low prices
- Volume

**Dividends Sheet** — Combined dividends for all tickers with:
- Ticker symbol
- Payment date
- Dividend per share

## Notes

- No Yahoo Finance Gold subscription required
- Data sourced from Yahoo Finance public API
- Check ticker symbols on Yahoo Finance for availability

## Appendix: Data Source

All market data is fetched from **Yahoo Finance** using the free `yfinance` library, which provides programmatic access to Yahoo Finance's data without requiring a subscription or API key.

### Dividend Data

Dividend information is retrieved from Yahoo Finance's dividend history for each ticker. The `fetch_dividends.py` script collects all historical dividend records available for the specified tickers and exports them with:
- **Ticker**: The stock symbol
- **Date**: The ex-dividend or payment date
- **Dividend**: The dividend amount per share

Note that with intraday or weekly price intervals, dividends may not align with candle dates. Use daily (`1d`) or longer intervals to see dividend dates in price sheets, or use the dedicated `fetch_dividends.py` script for dividend-only analysis.

### Data Availability

- Historical price data typically goes back several years depending on the ticker
- Dividend records span as far back as Yahoo Finance maintains the data
- Real-time data is not available through this tool; prices are delayed by Yahoo Finance's standard delay (typically 15-20 minutes for US stocks)
