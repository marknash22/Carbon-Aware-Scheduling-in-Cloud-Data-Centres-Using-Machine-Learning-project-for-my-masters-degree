import pandas as pd
from pathlib import Path

cloudsim = pd.read_csv("../results/cloudsim_energy_summary.csv")

baseline_kwh = cloudsim.loc[0, "energy_kwh"]

norm = pd.DataFrame({
    "model": ["CloudSim"],
    "energy_kwh": [baseline_kwh],
    "normalized_energy": [1.0]
})

out = Path("../results/cloudsim_energy_normalized.csv")
norm.to_csv(out, index=False)

print(norm)
print(f"\nSaved: {out.resolve()}")
