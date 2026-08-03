import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print(df.head())

df.info()

print(df.columns)
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df[return_columns].dtypes)

negative_sharpe = df[df["sharpe_ratio"] < 0]

print("Negative Sharpe Ratios:", len(negative_sharpe))
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratios:", len(invalid_expense))
print("Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()
df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance cleaned successfully!")