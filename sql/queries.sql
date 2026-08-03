-- Query 1: Top 5 Funds by AUM

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- Query 2: Average NAV per Month

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- Query 3: SIP Inflow YoY Growth

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- Query 4: Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- Query 5: Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- Query 6: Category-wise Net Inflows

SELECT
    category,
    SUM(net_inflow_crore) AS total_net_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_net_inflow DESC;


-- Query 7: Industry Folio Count

SELECT
    month,
    total_folios_crore
FROM industry_folio_count
ORDER BY month;


-- Query 8: Top 10 Portfolio Holdings by Weight

SELECT
    stock_name,
    SUM(weight_pct) AS total_weight
FROM portfolio_holdings
GROUP BY stock_name
ORDER BY total_weight DESC
LIMIT 10;


-- Query 9: Highest Closing Value of Each Benchmark

SELECT
    index_name,
    MAX(close_value) AS highest_close
FROM benchmark_indices
GROUP BY index_name;


-- Query 10: Top 10 Funds by Sharpe Ratio

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;