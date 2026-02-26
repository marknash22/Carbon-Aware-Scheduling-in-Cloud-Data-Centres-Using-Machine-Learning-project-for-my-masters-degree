import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed/cleaned_dataset.csv")

df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["workload"])
plt.title("Global Workload Proxy Over Time")
plt.xlabel("Date")
plt.ylabel("Workload (Confirmed Change)")
plt.tight_layout()
plt.savefig("../results/workload_over_time.png", dpi=300)
plt.close()

