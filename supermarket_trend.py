"""
Generate realistic daily supermarket transaction data and a trend chart.
Run: python supermarket_trend.py
Dependencies: numpy, pandas, matplotlib
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range("2025-04-01", "2026-09-30", freq="D")
rng = np.random.default_rng(42)
day_num = np.arange(len(dates))
trend = 900 + day_num * 0.12
weekday_effect = np.where(dates.dayofweek < 5, 1.0, 0.82)
month_effect = dates.month.map({
    1: 0.96, 2: 0.78, 3: 0.94, 4: 0.97, 5: 0.98, 6: 1.00,
    7: 1.02, 8: 1.01, 9: 1.00, 10: 1.03, 11: 1.08, 12: 1.35
}).to_numpy()
noise = rng.normal(0, 65, len(dates))
transactions = np.maximum(250, np.round(trend * weekday_effect * month_effect + noise)).astype(int)

daily = pd.DataFrame({"date": dates, "transactions": transactions}).set_index("date")
monthly = daily["transactions"].resample("MS").sum()
rolling_30 = daily["transactions"].rolling("30D").mean()

fig, ax1 = plt.subplots(figsize=(13, 7))
ax1.bar(monthly.index, monthly.values, width=22, label="Monthly transactions", alpha=0.78)
ax1.set_ylabel("Transactions per month")
ax1.set_xlabel("Month")
ax1.ticklabel_format(axis="y", style="plain")
ax1.grid(axis="y", linestyle="--", alpha=0.3)

ax2 = ax1.twinx()
ax2.plot(rolling_30.index, rolling_30.values, linewidth=2.4,
         label="30-day average (daily transactions)")
ax2.set_ylabel("Average transactions per day (30-day rolling average)")
ax2.ticklabel_format(axis="y", style="plain")

ax1.set_title("Nairobi Supermarket Transactions: Monthly Trend and 30-Day Average", pad=16)
ax1.set_xticks(monthly.index)
ax1.set_xticklabels([d.strftime("%b\\n%Y") for d in monthly.index])
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig("monthly_transaction_trend.png", dpi=180, bbox_inches="tight")
plt.close(fig)

daily.reset_index().to_csv("daily_transactions.csv", index=False)
monthly.rename("monthly_transactions").to_csv("monthly_totals.csv")
print("Saved chart and CSV data files.")
