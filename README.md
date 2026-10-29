# Nairobi Supermarket Transaction Trends

## Project overview
This project generates 18 months of realistic daily supermarket transaction counts, adds weekday and seasonal variation, summarizes monthly totals, and plots the monthly trend alongside a 30-day rolling average of daily transactions.

## Files
- `supermarket_trend.py` — reproducible Python analysis and chart generation.
- `monthly_transaction_trend.png` — chart for a non-technical audience.
- `daily_transactions.csv` — generated daily transaction counts.
- `monthly_totals.csv` — resampled monthly transaction totals.

## Trend to report to the client
The simulated data shows an overall gradual increase in customer transactions, with a clear seasonal lift in December and a noticeable dip in February. The 30-day average helps distinguish the underlying gradual movement from day-to-day noise, but the December and February pattern should be checked against actual historical data before making staffing or stock decisions.

## Run locally
Install dependencies with `pip install numpy pandas matplotlib`, then run `python supermarket_trend.py`.
