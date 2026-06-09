#!/usr/bin/env python3
"""Fetch end-of-day semiconductor stock prices and write to _data/stocks.json"""

import json
import os
from datetime import datetime

try:
    import yfinance as yf
    YF_AVAILABLE = True
except ImportError:
    YF_AVAILABLE = False
    print("yfinance not available, using cached data")

STOCKS = [
    {"ticker": "TSM",       "symbol": "TSM",     "name": "TSMC",             "currency": "USD"},
    {"ticker": "NVDA",      "symbol": "NVDA",    "name": "Nvidia",           "currency": "USD"},
    {"ticker": "ASML",      "symbol": "ASML",    "name": "ASML",             "currency": "USD"},
    {"ticker": "AMD",       "symbol": "AMD",     "name": "AMD",              "currency": "USD"},
    {"ticker": "AMAT",      "symbol": "AMAT",    "name": "Applied Materials","currency": "USD"},
    {"ticker": "MU",        "symbol": "MU",      "name": "Micron",           "currency": "USD"},
    {"ticker": "INTC",      "symbol": "INTC",    "name": "Intel",            "currency": "USD"},
    {"ticker": "LRCX",      "symbol": "LRCX",    "name": "Lam Research",     "currency": "USD"},
    {"ticker": "005930.KS", "symbol": "SAMSUNG", "name": "Samsung",          "currency": "KRW"},
    {"ticker": "000660.KS", "symbol": "SKHYNIX", "name": "SK Hynix",         "currency": "KRW"},
]


def fetch_prices():
    results = []
    if not YF_AVAILABLE:
        return results

    for stock in STOCKS:
        try:
            t = yf.Ticker(stock["ticker"])
            hist = t.history(period="5d")

            if len(hist) < 1:
                print(f"  No data for {stock['ticker']}")
                continue

            curr = float(hist["Close"].iloc[-1])
            prev = float(hist["Close"].iloc[-2]) if len(hist) >= 2 else curr
            change_pct = ((curr - prev) / prev) * 100 if prev else 0
            direction = "up" if change_pct >= 0 else "down"

            if stock["currency"] == "KRW":
                price_str = f"₩{curr:,.0f}"
            else:
                price_str = f"${curr:.2f}"

            change_str = f"{abs(change_pct):.2f}%"

            results.append({
                "symbol":    stock["symbol"],
                "name":      stock["name"],
                "price":     price_str,
                "change":    change_str,
                "direction": direction,
            })
            arrow = "▲" if direction == "up" else "▼"
            print(f"  ✓ {stock['symbol']}: {price_str} ({arrow} {change_str})")

        except Exception as e:
            print(f"  ✗ {stock['ticker']}: {e}")

    return results


def main():
    print("Fetching stock prices...")
    stocks = fetch_prices()

    data_path = "_data/stocks.json"
    existing = {}
    if os.path.exists(data_path):
        with open(data_path) as f:
            existing = json.load(f)

    if stocks:
        output = {
            "updated": datetime.utcnow().strftime("%b %d, %Y"),
            "stocks":  stocks,
        }
    else:
        print("No data fetched -- keeping cached data")
        output = existing if existing else {"updated": "N/A", "stocks": []}

    os.makedirs("_data", exist_ok=True)
    with open(data_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Saved {len(output.get('stocks', []))} stocks to {data_path}")


if __name__ == "__main__":
    main()
