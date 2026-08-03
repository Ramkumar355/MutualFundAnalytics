import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")
print(df.head())

df.info()

print(df.shape)

print(df.columns)
print(df["transaction_type"].unique())
invalid_amount = df[df["amount_inr"] <= 0]

print("Invalid amounts:", len(invalid_amount))
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
print(df["kyc_status"].unique())
print("Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()
print(df.dtypes)
df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned successfully!")