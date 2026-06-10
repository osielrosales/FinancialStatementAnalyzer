from data_fetcher import get_all_financials

# CALCULATE METRICS
# This function will calculate the key factors that most impact a stock
def calculate_metrics(ticker):
    data = get_all_financials(ticker)
    
    if data is None:
        return None

    income_list = data.get("income", [])
    if not income_list or len(income_list) < 2:
        return None
    
    latest_income = income_list[0]
    previous_income = income_list[1]

    balance = data["balance"]
    cash = data["cash"]

    return {
        "date": latest_income["date"],
        "profit_margin": get_profit_margin(latest_income),
        "roe": get_roe(latest_income, balance),
        "revenue_growth": get_revenue_growth(latest_income, previous_income),
        "free_cash_flow": get_free_cash_flow(cash),
        "debt_to_equity": get_debt_to_equity(balance),
    }
    
# GET PROFIT MARGIN
# The profit margin indicates what percentage of a company's revenue it retains as earnings after deducting all expenses
def get_profit_margin(income):
    return safe_division(income["netIncome"], income["revenue"])

# GET ROE
# The ROE measures how effectively a company utilizes its shareholders' equity to generate profits
def get_roe(income, balance):
    return safe_division(income["netIncome"], balance["totalStockholdersEquity"])

# GET REVENUE GROWTH
# Revenue growth is the percentage increase or decrease in a company's sales over a specific period, such as quarter-over-quarter or year-over-year.
def get_revenue_growth(current, previous):
    return safe_division(current["revenue"] - previous["revenue"], previous["revenue"])

# GET FREE CASH FLOW
# Free cash flow is the cash a company generates after covering its operating expenses and capital expenditures
def get_free_cash_flow(cash):
    if cash is None:
        return None
    return cash["freeCashFlow"]

# GET DEBT TO EQUITY
# The debt to equity compares a company's total liabilities to its shareholders' equity
def get_debt_to_equity(balance):
    return safe_division(balance["totalLiabilities"], balance["totalStockholdersEquity"])

# SAFE DIVISION
# Only divides if it is safe to do so 
def safe_division(x, y):
    return x / y if y else None

