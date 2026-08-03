import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("sqlite:///bluestock_mf.db")
fund_df = pd.read_csv("data/raw/01_fund_master.csv")

nav_df = pd.read_csv("data/processed/02_nav_history_clean.csv")

transaction_df = pd.read_csv("data/processed/08_investor_transactions_clean.csv")

performance_df = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

aum_df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)
nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)
transaction_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)
performance_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)
aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)
print("dim_fund:", len(fund_df))

print("fact_nav:", len(nav_df))

print("fact_transactions:", len(transaction_df))

print("fact_performance:", len(performance_df))

print("fact_aum:", len(aum_df))
print("SQLite database created successfully!")
print(pd.read_sql("SELECT COUNT(*) FROM dim_fund;", engine))

print(pd.read_sql("SELECT COUNT(*) FROM fact_nav;", engine))

print(pd.read_sql("SELECT COUNT(*) FROM fact_transactions;", engine))

print(pd.read_sql("SELECT COUNT(*) FROM fact_performance;", engine))

print(pd.read_sql("SELECT COUNT(*) FROM fact_aum;", engine))