import pandas as pd

DATA_PATH = "../data/raw/bing_covid-19_data.csv"

df = pd.read_csv(DATA_PATH, nrows=200000)

print("\n=== BASIC INFO ===")
print("Rows read:", len(df))
print("Columns:", len(df.columns))

print("\n=== COLUMN NAMES ===")
for c in df.columns:
    print("-", c)

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES (TOP 20) ===")
print(df.isna().sum().sort_values(ascending=False).head(20))

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== NUMERIC SUMMARY (TOP 20) ===")
print(df.select_dtypes(include='number').describe().T.head(20))
