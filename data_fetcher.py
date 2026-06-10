import requests
import streamlit as st
import os

API_KEY = os.getenv("API_KEY") or st.secrets["API_KEY"]

@st.cache_data(ttl=60 * 60 * 24)
def get_company_name(ticker):
    url = f"https://financialmodelingprep.com/stable/search-symbol?query={ticker}&apikey={API_KEY}"
    data = safe_url_fetch(url)

    if not data or len(data) == 0:
        return None

    return data[0].get("name")


# INCOME STATEMENT
# Makes an API call to get the income statement of the inputted ticker
@st.cache_data(ttl=86400)
def get_income_statement(ticker):
    url = f"https://financialmodelingprep.com/stable/income-statement?symbol={ticker}&apikey={API_KEY}"
    return safe_url_fetch(url)

# BALANCE SHEET
# Makes an API call to get the balance sheet of the inputted ticker
@st.cache_data(ttl=86400)
def get_balance_sheet(ticker):
    url = f"https://financialmodelingprep.com/stable/balance-sheet-statement?symbol={ticker}&apikey={API_KEY}"
    return safe_url_fetch(url)

# CASH FLOW STATEMENT
# Makes an API call to get the cash flow of the inputted ticker
@st.cache_data(ttl=86400)
def get_cash_flow(ticker):
    url = f"https://financialmodelingprep.com/stable/cash-flow-statement?symbol={ticker}&apikey={API_KEY}"
    return safe_url_fetch(url)

# GET LATEST
# If the newest dataset exists, it is returned
def get_latest(data):
    if isinstance(data, list) and len(data) > 0:
        return data[0]
    return None

# GET ALL FINANCIALS
# Returns the three financial statements from the given tickr
# In the case of the income statement, the entire list is sent back instead of the latest as 2 statements are
#   needed for a calculation
@st.cache_data(ttl=86400)
def get_all_financials(ticker):
    income = get_income_statement(ticker)
    balance = get_latest(get_balance_sheet(ticker))
    cash = get_latest(get_cash_flow(ticker))

    if income is None or balance is None or cash is None:
        return None

    return {
        "income": income,
        "balance": balance,
        "cash": cash
    }

# SAFE URL FETCH
# Try/catch in case the API fails to work
def safe_url_fetch(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # catches HTTP errors (404, 500, etc.)
        return response.json()

    except requests.exceptions.Timeout:
        print(f"[TIMEOUT] Request timed out: {url}")
        return None

    except requests.exceptions.HTTPError as e:
        print(f"[HTTP ERROR] {e} for URL: {url}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"[REQUEST ERROR] {e} for URL: {url}")
        return None

    except ValueError:
        print(f"[JSON ERROR] Invalid JSON response: {url}")
        return None
    