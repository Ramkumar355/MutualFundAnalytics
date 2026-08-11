import pandas as pd

# Load fund performance data
fund_scorecard = pd.read_csv("outputs/fund_scorecard.csv")
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# Combine Sharpe ratio with risk category
recommender_df = fund_scorecard[
    ["amfi_code", "scheme_name", "Sharpe_Ratio"]
].merge(
    fund_master[
        ["amfi_code", "risk_category"]
    ],
    on="amfi_code",
    how="left"
)


def recommend_funds(risk_appetite):
    matching_funds = recommender_df[
        recommender_df["risk_category"].str.lower()
        == risk_appetite.lower()
    ]

    recommendations = (
        matching_funds
        .sort_values("Sharpe_Ratio", ascending=False)
        .head(3)
    )

    return recommendations[
        ["scheme_name", "risk_category", "Sharpe_Ratio"]
    ]


# Example
risk = input("Enter risk appetite (Low/Moderate/High): ")

print("\nTop 3 Fund Recommendations:")
print(recommend_funds(risk).to_string(index=False))