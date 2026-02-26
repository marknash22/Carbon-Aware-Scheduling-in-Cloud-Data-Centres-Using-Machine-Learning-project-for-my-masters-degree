import pandas as pd

INPUT = "../data/raw/bing_covid-19_data.csv"
OUTPUT = "../data/processed/cleaned_dataset.csv"

df = pd.read_csv(INPUT, low_memory=False)

df["updated"] = pd.to_datetime(df["updated"], errors="coerce")

df = df[[
    "updated",
    "country_region",
    "confirmed_change"
]]

df = df.dropna()

df = df[df["confirmed_change"] >= 0]

df_daily = (
    df
    .groupby(df["updated"].dt.date)["confirmed_change"]
    .sum()
    .reset_index()
)

df_daily.columns = ["date", "workload"]

df_daily.to_csv(OUTPUT, index=False)

print("Cleaned dataset saved to:", OUTPUT)
print("Rows:", len(df_daily))
print(df_daily.head())
