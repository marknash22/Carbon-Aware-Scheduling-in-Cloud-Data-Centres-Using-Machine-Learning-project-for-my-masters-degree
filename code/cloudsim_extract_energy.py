import re
from pathlib import Path
import pandas as pd

SOURCE = Path("../cloudsim/cloudsim-7.0.1/modules/cloudsim-examples/carbonaware/log/random_dvfs.txt")

text = SOURCE.read_text(errors="ignore")

m = re.search(r"Energy consumption:\s*([0-9.]+)\s*kWh", text)
if not m:
    raise SystemExit("Could not find total energy line.")

energy_kwh = float(m.group(1))

out = pd.DataFrame([{
    "run_name": "random_dvfs",
    "energy_kwh": energy_kwh
}])

out_path = Path("../results/cloudsim_energy_summary.csv")
out.to_csv(out_path, index=False)

print("Source:", SOURCE.resolve())
print("Saved :", out_path.resolve())
print(out)
