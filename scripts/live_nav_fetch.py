import requests
import pandas as pd

schemes = {
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_Large_Cap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

for code, name in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    print("=" * 50)
    print("Scheme:", name)
    print("Latest NAV:", data["data"][0]["nav"])

    df = pd.DataFrame(data["data"])

    filename = f"data/raw/{name}.csv"

    df.to_csv(filename, index=False)

    print("Saved:", filename)