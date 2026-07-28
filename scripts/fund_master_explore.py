import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 50)
print("Unique Fund Houses")
print(df["fund_house"].unique())

print("\n" + "=" * 50)
print("Unique Categories")
print(df["category"].unique())

print("\n" + "=" * 50)
print("Unique Sub-Categories")
print(df["sub_category"].unique())

print("\n" + "=" * 50)
print("Unique Risk Grades")
print(df["risk_category"].unique())