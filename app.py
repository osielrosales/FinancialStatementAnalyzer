import streamlit as st
import pandas as pd

from data_fetcher import get_company_name
from calculator import calculate_metrics
from scoring import get_financial_score

# PAGE SETUP
st.set_page_config(page_title="Financial Statement Analyzer", layout="wide" )

# Header
st.title("Financial Statement Analyzer") 
st.caption( "Compare the financial strength of publicly traded companies using " 
           "profitability, growth, cash flow, and leverage metrics.")

st.divider()

# PAGE SIDEBAR
with st.sidebar: 
    st.header("About") 
    st.write( "This program analyzes financial statements and computes a custom financial score from 0–100." ) 
    st.markdown("---") 
    st.subheader("Metrics Used") 
    st.write("• Profit Margin") 
    st.write("• Return on Equity (ROE)") 
    st.write("• Revenue Growth") 
    st.write("• Free Cash Flow") 
    st.write("• Debt to Equity") 
    st.markdown("---") 
    st.caption( "Scores are intended for educational purposes only." )

# USER INPUT
ticker_input = st.text_input(
   "Enter tickers (comma separated):",
   placeholder="AAPL, MSFT, TSLA"
)

# BUTTON PRESSED
if st.button("Analyze"):
    
    if not ticker_input.strip():
        st.warning("Please enter at least one ticker.")
    else:
        ticker_list = [
            ticker.strip().upper()
            for ticker in ticker_input.split(",")
            if ticker.strip()
        ]
        results = []

        with st.spinner("Fetching financial data..."):

            for symbol in ticker_list:
                metrics = calculate_metrics(symbol)

                if metrics is None:
                    continue

                results.append({
                    "ticker": symbol,
                    "name": get_company_name(symbol),
                    "metrics": metrics,
                    "score": get_financial_score(metrics)
                })

        if not results:
            st.error("No valid financial data could be retrieved.")
        else:

            st.divider()

            # COMPANY CARDS
            cards_per_row = 3

            for i in range(0, len(results), cards_per_row):

                row = results[i:i + cards_per_row]
                cols = st.columns(cards_per_row)

                for col, company in zip(cols, row):

                    with col:
                        with st.container(border=True):
                            st.subheader(company["ticker"])

                            if company["name"]:
                                st.caption(company["name"])

                            st.metric(
                                "Financial Score",
                                f"{company['score']:.1f}/100"
                            )

                            score = company["score"]

                            if score >= 80:
                                st.success("Excellent")
                            elif score >= 60:
                                st.info("Good")
                            elif score >= 40:
                                st.warning("Average")
                            else:
                                st.error("Weak")

                            st.caption(f"Financials as of: " f"{company['metrics']['date']}")

                            st.divider()

                            metrics = company["metrics"]

                            metric_table = pd.DataFrame({
                                "Metric": [
                                    "Profit Margin",
                                    "ROE",
                                    "Revenue Growth",
                                    "Free Cash Flow",
                                    "Debt / Equity"
                                ],
                                "Value": [
                                    f"{metrics['profit_margin']:.2%}",
                                    f"{metrics['roe']:.2%}",
                                    f"{metrics['revenue_growth']:.2%}",
                                    f"${metrics['free_cash_flow']/1e9:.1f}B",
                                    f"{metrics['debt_to_equity']:.2f}"
                                ]
                            })

                            st.table(metric_table)

            # SCORE COMPARISON CHART
            if len(results) > 1:
                st.divider()
                chart_df = pd.DataFrame({
                    "Company": [c["ticker"] for c in results],
                    "Score": [c["score"] for c in results]
                })

                st.subheader("Financial Score Comparison")
                st.bar_chart(chart_df.set_index("Company"))

            # FOOTER
            st.divider()
            st.caption(
                "Data provided by the Financial Modeling Prep API. "
            )





