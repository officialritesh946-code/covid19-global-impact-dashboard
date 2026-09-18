import os
import numpy as np
import pandas as pd

RAW = "raw_data"
OUT = "outputs"
os.makedirs(OUT, exist_ok=True)

daily = pd.read_csv(os.path.join(RAW, "day_wise.csv"), parse_dates=["Date"])
country = pd.read_csv(os.path.join(RAW, "country_wise_latest.csv"))

daily["7D Avg New Cases"] = daily["New cases"].rolling(7).mean()
daily["7D Avg New Deaths"] = daily["New deaths"].rolling(7).mean()
daily["Case Fatality Rate (%)"] = np.where(
    daily["Confirmed"] > 0, daily["Deaths"] / daily["Confirmed"] * 100, np.nan
)

prev7 = daily["Confirmed"].shift(7)
ratio = daily["Confirmed"] / prev7
daily["Doubling Time (days)"] = np.where(
    (prev7 > 0) & (ratio > 1),
    7 * np.log(2) / np.log(ratio),
    np.nan
)

country["Case Fatality Rate (%)"] = np.where(
    country["Confirmed"] > 0, country["Deaths"] / country["Confirmed"] * 100, np.nan
)
country["Recovery Rate (%)"] = np.where(
    country["Confirmed"] > 0, country["Recovered"] / country["Confirmed"] * 100, np.nan
)

region = country.groupby("WHO Region", as_index=False)[
    ["Confirmed","Deaths","Recovered","Active","New cases","New deaths"]
].sum()
region["Case Fatality Rate (%)"] = region["Deaths"] / region["Confirmed"] * 100
region = region.sort_values("Confirmed", ascending=False)

daily.to_csv(os.path.join(OUT, "COVID19_Cleaned_Daily.csv"), index=False)
country.to_csv(os.path.join(OUT, "COVID19_Cleaned_Country.csv"), index=False)
region.to_csv(os.path.join(OUT, "COVID19_Region_Summary.csv"), index=False)

print("Analysis complete.")
print("Date range:", daily["Date"].min().date(), "to", daily["Date"].max().date())
print("Final confirmed:", f'{daily.iloc[-1]["Confirmed"]:,}')
print("Final deaths:", f'{daily.iloc[-1]["Deaths"]:,}')
print("Peak daily new cases:", f'{daily["New cases"].max():,}')
