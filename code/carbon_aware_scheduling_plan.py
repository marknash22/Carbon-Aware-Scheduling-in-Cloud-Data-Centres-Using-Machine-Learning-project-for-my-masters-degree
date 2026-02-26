import pandas as pd

INPUT = "../data/processed/workload_energy_carbon.csv"
OUTPUT = "../data/processed/carbon_aware_scheduling_plan.csv"

df = pd.read_csv(INPUT)
df["date"] = pd.to_datetime(df["date"])

regions = ["west_us", "west_europe", "north_europe"]
df["baseline_region"] = "west_europe"
df["baseline_carbon_g"] = df["carbon_west_europe_g"]
carbon_cols = {r: f"carbon_{r}_g" for r in regions}
df["carbon_aware_region"] = df[[carbon_cols[r] for r in regions]].idxmin(axis=1)
df["carbon_aware_region"] = df["carbon_aware_region"].str.replace("carbon_", "").str.replace("_g", "")
df["carbon_aware_carbon_g"] = df.apply(lambda row: row[f"carbon_{row['carbon_aware_region']}_g"], axis=1)

df["carbon_saving_g"] = df["baseline_carbon_g"] - df["carbon_aware_carbon_g"]
df["carbon_saving_pct"] = (df["carbon_saving_g"] / df["baseline_carbon_g"]) * 100

schedule = df[[
    "date",
    "workload",
    "energy_kwh",
    "baseline_region",
    "baseline_carbon_g",
    "carbon_aware_region",
    "carbon_aware_carbon_g",
    "carbon_saving_g",
    "carbon_saving_pct"
]]

schedule.to_csv(OUTPUT, index=False)
print("Saved schedule plan:", OUTPUT)
print(schedule.head())

total_base = schedule["baseline_carbon_g"].sum()
total_aware = schedule["carbon_aware_carbon_g"].sum()
total_save = total_base - total_aware
pct_save = (total_save / total_base) * 100 if total_base != 0 else 0

print("\n=== Overall Summary ===")
print("Total baseline carbon (g):", total_base)
print("Total carbon-aware carbon (g):", total_aware)
print("Total savings (g):", total_save)
print("Savings (%):", pct_save)

out_txt = "../results/step8_scheduling_summary.txt"
with open(out_txt, "w") as f:
    f.write("Step 8 Scheduling Summary\n")
    f.write(f"Total baseline carbon (g): {total_base}\n")
    f.write(f"Total carbon-aware carbon (g): {total_aware}\n")
    f.write(f"Total savings (g): {total_save}\n")
    f.write(f"Savings (%): {pct_save}\n")
print("Saved summary:", out_txt)
