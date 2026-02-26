import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("../data/processed/cleaned_dataset.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
df["dayofweek"] = df["date"].dt.dayofweek
df["month"] = df["date"].dt.month
df["dayofmonth"] = df["date"].dt.day
df["weekofyear"] = df["date"].dt.isocalendar().week.astype(int)

df["roll7_mean"] = df["workload"].rolling(7).mean()
df["roll14_mean"] = df["workload"].rolling(14).mean()
df["roll7_std"] = df["workload"].rolling(7).std()
df["lag1"] = df["workload"].shift(1)
df["lag7"] = df["workload"].shift(7)

df = df.dropna().reset_index(drop=True)

FEATURES = [
    "dayofweek", "month", "dayofmonth", "weekofyear",
    "roll7_mean", "roll14_mean", "roll7_std",
    "lag1", "lag7"
]
TARGET = "workload"

X = df[FEATURES]
y = df[TARGET]

split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)
pred = model.predict(X_test)
mae = mean_absolute_error(y_test, pred)
mse = mean_squared_error(y_test, pred)
rmse = mse ** 0.5

print("Random Forest Baseline (Time Features)")
print("Train rows:", len(X_train), "Test rows:", len(X_test))
print("MAE:", mae)
print("RMSE:", rmse)

importances = pd.Series(model.feature_importances_, index=FEATURES).sort_values(ascending=False)
print("\nFeature importance:")
print(importances)

out_path = "../results/ml_baseline_results.txt"
with open(out_path, "w") as f:
    f.write("Random Forest Baseline (Time Features)\n")
    f.write(f"Train rows: {len(X_train)}  Test rows: {len(X_test)}\n")
    f.write(f"MAE: {mae}\n")
    f.write(f"RMSE: {rmse}\n\n")
    f.write("Feature importance:\n")
    f.write(importances.to_string())
print("\nSaved:", out_path)
