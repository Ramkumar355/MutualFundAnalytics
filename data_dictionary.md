# Mutual Fund Analytics Data Dictionary

## 1. Fund Master (01_fund_master.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| amfi_code | INTEGER | Unique AMFI code identifying the mutual fund | 01_fund_master.csv |
| fund_house | TEXT | Asset Management Company (AMC) | 01_fund_master.csv |
| scheme_name | TEXT | Name of the mutual fund scheme | 01_fund_master.csv |
| category | TEXT | Mutual fund category | 01_fund_master.csv |
| sub_category | TEXT | Sub-category of the scheme | 01_fund_master.csv |
| plan | TEXT | Regular or Direct plan | 01_fund_master.csv |
| launch_date | DATE | Scheme launch date | 01_fund_master.csv |
| benchmark | TEXT | Benchmark index followed by the scheme | 01_fund_master.csv |
| expense_ratio_pct | REAL | Expense ratio charged by the fund (%) | 01_fund_master.csv |
| exit_load_pct | REAL | Exit load percentage | 01_fund_master.csv |
| min_sip_amount | INTEGER | Minimum SIP investment amount | 01_fund_master.csv |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment | 01_fund_master.csv |
| fund_manager | TEXT | Name of the fund manager | 01_fund_master.csv |
| risk_category | TEXT | Risk category of the scheme | 01_fund_master.csv |
| sebi_category_code | TEXT | SEBI classification code | 01_fund_master.csv |

---

## 2. NAV History (02_nav_history.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| amfi_code | INTEGER | Unique AMFI code | 02_nav_history.csv |
| date | DATE | NAV date | 02_nav_history.csv |
| nav | REAL | Net Asset Value of the fund | 02_nav_history.csv |

---

## 3. AUM by Fund House (03_aum_by_fund_house.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| date | DATE | Reporting date | 03_aum_by_fund_house.csv |
| fund_house | TEXT | Asset Management Company | 03_aum_by_fund_house.csv |
| aum_lakh_crore | REAL | Assets Under Management (Lakh Crore) | 03_aum_by_fund_house.csv |
| aum_crore | INTEGER | Assets Under Management (Crore) | 03_aum_by_fund_house.csv |
| num_schemes | INTEGER | Number of schemes managed | 03_aum_by_fund_house.csv |

---

## 4. Monthly SIP Inflows (04_monthly_sip_inflows.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| month | DATE | Reporting month | 04_monthly_sip_inflows.csv |
| sip_inflow_crore | INTEGER | Monthly SIP inflow (₹ Crore) | 04_monthly_sip_inflows.csv |
| active_sip_accounts_crore | REAL | Active SIP accounts (Crore) | 04_monthly_sip_inflows.csv |
| new_sip_accounts_lakh | REAL | Newly registered SIP accounts (Lakh) | 04_monthly_sip_inflows.csv |
| sip_aum_lakh_crore | REAL | SIP Assets Under Management | 04_monthly_sip_inflows.csv |
| yoy_growth_pct | REAL | Year-over-Year SIP growth (%) | 04_monthly_sip_inflows.csv |

---

## 5. Category Inflows (05_category_inflows.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| month | DATE | Reporting month | 05_category_inflows.csv |
| category | TEXT | Mutual fund category | 05_category_inflows.csv |
| net_inflow_crore | REAL | Net inflow amount (₹ Crore) | 05_category_inflows.csv |

---

## 6. Industry Folio Count (06_industry_folio_count.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| month | DATE | Reporting month | 06_industry_folio_count.csv |
| total_folios_crore | REAL | Total folios in the industry | 06_industry_folio_count.csv |
| equity_folios_crore | REAL | Equity fund folios | 06_industry_folio_count.csv |
| debt_folios_crore | REAL | Debt fund folios | 06_industry_folio_count.csv |
| hybrid_folios_crore | REAL | Hybrid fund folios | 06_industry_folio_count.csv |
| others_folios_crore | REAL | Other category folios | 06_industry_folio_count.csv |

---

## 7. Scheme Performance (07_scheme_performance.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| amfi_code | INTEGER | Unique AMFI code | 07_scheme_performance.csv |
| scheme_name | TEXT | Name of the mutual fund scheme | 07_scheme_performance.csv |
| fund_house | TEXT | Asset Management Company | 07_scheme_performance.csv |
| category | TEXT | Mutual fund category | 07_scheme_performance.csv |
| plan | TEXT | Regular or Direct plan | 07_scheme_performance.csv |
| return_1yr_pct | REAL | 1-Year return (%) | 07_scheme_performance.csv |
| return_3yr_pct | REAL | 3-Year return (%) | 07_scheme_performance.csv |
| return_5yr_pct | REAL | 5-Year return (%) | 07_scheme_performance.csv |
| benchmark_3yr_pct | REAL | 3-Year benchmark return (%) | 07_scheme_performance.csv |
| alpha | REAL | Alpha performance metric | 07_scheme_performance.csv |
| beta | REAL | Beta risk metric | 07_scheme_performance.csv |
| sharpe_ratio | REAL | Sharpe Ratio | 07_scheme_performance.csv |
| sortino_ratio | REAL | Sortino Ratio | 07_scheme_performance.csv |
| std_dev_ann_pct | REAL | Annualized standard deviation (%) | 07_scheme_performance.csv |
| max_drawdown_pct | REAL | Maximum drawdown (%) | 07_scheme_performance.csv |
| aum_crore | INTEGER | Assets Under Management (₹ Crore) | 07_scheme_performance.csv |
| expense_ratio_pct | REAL | Expense ratio (%) | 07_scheme_performance.csv |
| morningstar_rating | INTEGER | Morningstar rating (1–5) | 07_scheme_performance.csv |
| risk_grade | TEXT | Overall risk grade | 07_scheme_performance.csv |

---

## 8. Investor Transactions (08_investor_transactions.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| investor_id | TEXT | Unique investor identifier | 08_investor_transactions.csv |
| transaction_date | DATE | Date of transaction | 08_investor_transactions.csv |
| amfi_code | INTEGER | Mutual fund AMFI code | 08_investor_transactions.csv |
| transaction_type | TEXT | SIP, Lumpsum or Redemption | 08_investor_transactions.csv |
| amount_inr | INTEGER | Transaction amount (₹) | 08_investor_transactions.csv |
| state | TEXT | Investor state | 08_investor_transactions.csv |
| city | TEXT | Investor city | 08_investor_transactions.csv |
| city_tier | TEXT | Tier classification of city | 08_investor_transactions.csv |
| age_group | TEXT | Investor age group | 08_investor_transactions.csv |
| gender | TEXT | Investor gender | 08_investor_transactions.csv |
| annual_income_lakh | REAL | Annual income (Lakh ₹) | 08_investor_transactions.csv |
| payment_mode | TEXT | Payment method | 08_investor_transactions.csv |
| kyc_status | TEXT | KYC verification status | 08_investor_transactions.csv |

---

## 9. Portfolio Holdings (09_portfolio_holdings.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| amfi_code | INTEGER | Mutual fund AMFI code | 09_portfolio_holdings.csv |
| stock_symbol | TEXT | Stock ticker symbol | 09_portfolio_holdings.csv |
| stock_name | TEXT | Company name | 09_portfolio_holdings.csv |
| sector | TEXT | Industry sector | 09_portfolio_holdings.csv |
| weight_pct | REAL | Portfolio weight (%) | 09_portfolio_holdings.csv |
| market_value_cr | REAL | Market value (₹ Crore) | 09_portfolio_holdings.csv |
| current_price_inr | REAL | Current stock price (₹) | 09_portfolio_holdings.csv |
| portfolio_date | DATE | Portfolio reporting date | 09_portfolio_holdings.csv |

---

## 10. Benchmark Indices (10_benchmark_indices.csv)

| Column | Data Type | Business Definition | Source |
|--------|-----------|---------------------|--------|
| date | DATE | Trading date | 10_benchmark_indices.csv |
| index_name | TEXT | Benchmark index name | 10_benchmark_indices.csv |
| close_value | REAL | Closing value of the benchmark index | 10_benchmark_indices.csv |