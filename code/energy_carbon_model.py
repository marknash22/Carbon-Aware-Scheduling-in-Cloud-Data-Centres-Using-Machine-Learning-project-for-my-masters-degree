import pandas as pd


df = pd.read_csv("../data/processed/cleaned_dataset.csv")
df["date"] = pd.to_datetime(df["date"])


ENERGY_FACTOR = 0.0005  # kWh per workload unit

CARBON_INTENSITY = {
    "west_us": 400,       # gCO2/kWh
    "west_europe": 250,
    "north_europe": 100
}

df["energy_kwh"] = df["workload"] * ENERGY_FACTOR

for region, intensity in CARBON_INTENSITY.items():
    df[f"carbon_{region}_g"] = df["energy_kwh"] * intensity

output = "../data/processed/workload_energy_carbon.csv"
df.to_csv(output, index=False)

print("Saved:", output)
print(df.head())
