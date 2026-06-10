from calculator import calculate_metrics

# GET FINANCIAL SCORE
# This function will use the metrics and assign weights to them, giving a financial score to a stock
def get_financial_score(metrics):
    
    if not metrics:
        return None
    
    # Profitability (40%)
    profit_score = normalize(metrics["profit_margin"], 0, 0.3) # 25%
    roe_score = normalize(metrics["roe"], 0, 0.5) # 15%

    # Growth (20%)
    growth_score = normalize(metrics["revenue_growth"], -0.2, 0.3)

    # Cash flow (20%) 
    fcf_score = normalize(metrics["free_cash_flow"], 0, 1e11)

    # Debt (20%)
    debt_score = 1 - normalize(metrics["debt_to_equity"], 0, 3)

    score = (
        profit_score * .25 +
        roe_score * .15 +
        growth_score * .2 +
        fcf_score * .2 +
        debt_score * .2
    )

    return score * 100

# NORMALIZE
# Since the values are on different scales, this function will force them into a range between 0-1
# Normalizes based on realistic ranges seen in the real-world
def normalize(x, low, high):
    if x is None:
        return 0

    if high == low:
        return 0

    x = max(min(x, high), low)
    return (x - low) / (high - low)
