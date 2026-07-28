import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("=" * 50)

if len(missing_codes) == 0:
    print("All AMFI codes in fund_master exist in nav_history.")
else:
    print("Missing AMFI Codes:")
    print(missing_codes)

print("=" * 50)
print("Total Fund Codes:", len(fund_codes))
print("Total NAV Codes:", len(nav_codes))