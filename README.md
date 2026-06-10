# Financial Statement Analyzer

This project is a Python application that uses the Financial Modeling Prep API to pull company financial statement data and calculate a custom financial health score. It also includes a simple Streamlit interface that lets users compare multiple companies side-by-side.

I built this project to get more experience working with APIs, data processing, and Python application development while combining my interests in computer science and finance.

## Features

* Search for one or more stock tickers at the same time
* Pull income statements, balance sheets, and cash flow statements from the FMP API
* Calculate several common financial metrics:

  * Profit Margin
  * Return on Equity (ROE)
  * Revenue Growth
  * Free Cash Flow
  * Debt-to-Equity Ratio
* Generate a weighted financial score from 0–100 based on those metrics
* Display the latest reporting date for the financial statements used
* Cache API responses to reduce unnecessary API calls and improve load times

## Tech Stack

* Python
* Streamlit
* Requests
* python-dotenv
* Financial Modeling Prep API

## Project Structure

FinancialStatementAnalyzer/
│
├── app.py               # Streamlit interface
├── data_fetcher.py      # API requests and data retrieval
├── calculator.py        # Financial metric calculations
├── scoring.py           # Financial scoring model
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

## Financial Score

The overall score is based on five metrics:

| Metric               | Weight |
| -------------------- | :----: |
| Profit Margin        |   25%  |
| Return on Equity     |   15%  |
| Revenue Growth       |   20%  |
| Free Cash Flow       |   20%  |
| Debt-to-Equity Ratio |   20%  |

Each metric is normalized to a common scale before being combined into a final score between 0 and 100.

## Setup

Clone the repository:

git clone https://github.com/yourusername/FinancialStatementAnalyzer.git
cd FinancialStatementAnalyzer

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Create a `.env` file in the project folder and add your Financial Modeling Prep API key:

API_KEY=your_api_key_here

## Running the App

Start the Streamlit app with:

streamlit run app.py

Then open the local address shown in your terminal (usually `http://localhost:8501`).

## Example

Enter one or more tickers separated by commas:

AAPL, MSFT, TSLA

The application will display each company's:

* Financial score
* Reporting date
* Profit Margin
* Return on Equity
* Revenue Growth
* Free Cash Flow
* Debt-to-Equity Ratio

## Future Improvements

Some features I'd like to add in the future:

* Historical charts and trend analysis
* More financial ratios
* Sector-relative comparisons
* Portfolio analysis
* Exporting results to CSV

## Author

Osiel Rosales
B.S. Computer Science, University of Illinois Chicago (Expected May 2027)
