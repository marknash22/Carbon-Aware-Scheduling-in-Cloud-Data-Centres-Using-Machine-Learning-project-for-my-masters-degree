import pandas as pd
from pathlib import Path

PLAN_PATH = Path("../data/processed/carbon_aware_scheduling_plan.csv")
CLOUDSIM_PATH = Path("../results/cloudsim_energy_summary.csv")

plan = pd.read_csv(PLAN_PATH)
cloudsim = pd.read_csv(CLOUDSIM_PATH)

# Python model total energy
python_total_kwh = float(plan["energy_kwh"].sum())

# CloudSim energy (single run value)
cloudsim_kwh = float(cloudsim.loc[0, "energy_kwh"])

# Comparisons
abs_diff = python_total_kwh - cloudsim_kwh
pct_diff = (abs_diff / cloudsim_kwh) * 100 if cloudsim_kwh != 0 else float("nan")

summary_lines = [
    "Energy Model Comparison (Python vs CloudSim)",
    f"Python total energy (kWh): {python_total_kwh:.6f}",
    f"CloudSim energy (kWh):      {cloudsim_kwh:.6f}",
    f"Absolute difference (kWh):  {abs_diff:.6f}",
    f"Percent difference (%):     {pct_diff:.2f}",
]

out_path = Path("../results/step9_energy_comparison.txt")
out_path.write_text("\n".join(summary_lines) + "\n")

print("\n".join(summary_lines))
print(f"\nSaved: {out_path.resolve()}")
