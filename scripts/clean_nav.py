import pandas as pd

df=pd.read_csv("data/raw/02_nav_history.csv")
print(df.head())
print(df.info())
print(df.shape)
df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
print(df.columns)
df = df.sort_values(by=["amfi_code", "date"])
df = df.drop_duplicates()
print("Rows after removing duplicates:", len(df))
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV values:", len(invalid_nav))
df["nav"] = df.groupby("amfi_code")["nav"].ffill()
print("Missing NAV values:", df["nav"].isnull().sum())
df.to_csv("data/processed/02_nav_history_clean.csv", index=False)