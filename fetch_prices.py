import yfinance as yf
import pandas as pd
from datetime import datetime
import sys
import os


def fetch_historical_prices(tickers: list[str], period: str = None, start: str = None, end: str = None, interval: str = "1d") -> dict[str, pd.DataFrame]:
    results = {}
    for symbol in tickers:
        print(f"Fetching {symbol}...")
        ticker = yf.Ticker(symbol)
        if start:
            hist = ticker.history(start=start, end=end, interval=interval)
        else:
            hist = ticker.history(period=period or "1y", interval=interval)

        if hist.empty:
            print(f"  WARNING: No data returned for {symbol}. Check the ticker symbol.")
            continue

        hist.index = hist.index.tz_localize(None)  # strip timezone for Excel compatibility
        hist = hist[["Open", "Close", "High", "Low", "Volume"]]
        hist.index.name = "Date"
        results[symbol] = hist
        print(f"  {len(hist)} rows retrieved ({hist.index[0].date()} to {hist.index[-1].date()})")

    return results


def write_to_excel(data: dict[str, pd.DataFrame], output_path: str):
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for symbol, df in data.items():
            sheet_name = symbol[:31]  # Excel sheet names max 31 chars
            df.to_excel(writer, sheet_name=sheet_name)

            ws = writer.sheets[sheet_name]

            # Column widths
            ws.column_dimensions["A"].width = 18  # Date
            for col in ["B", "C", "D", "E", "F"]:
                ws.column_dimensions[col].width = 14

            # Format numeric columns as 2 decimal places, Volume as integer
            from openpyxl.styles import numbers
            for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
                for cell in row[1:5]:  # Open, Close, High, Low
                    cell.number_format = "#,##0.00"
                row[5].number_format = "#,##0"  # Volume

    print(f"\nSaved to: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    # ── Configuration ──────────────────────────────────────────────────────────
    TICKERS = ["WOW.AX"]

    # Choose ONE of the following date options:
    # Option A — relative period: 1d 5d 1mo 3mo 6mo 1y 2y 5y 10y ytd max
    PERIOD = "5y"

    # Option B — explicit date range (set PERIOD = None to use these)
    START_DATE = "2024-01-01"
    END_DATE   = None  # None = today

    # Data frequency: 1d (daily), 1wk (weekly), 1mo (monthly), or 1h/15m/5m/1m (intraday)
    INTERVAL = "1mo"

    OUTPUT_FILE = "stock_prices.xlsx"
    # ───────────────────────────────────────────────────────────────────────────

    if PERIOD:
        data = fetch_historical_prices(TICKERS, period=PERIOD, interval=INTERVAL)
    else:
        data = fetch_historical_prices(TICKERS, start=START_DATE, end=END_DATE, interval=INTERVAL)

    if not data:
        print("No data fetched. Exiting.")
        sys.exit(1)

    write_to_excel(data, OUTPUT_FILE)
