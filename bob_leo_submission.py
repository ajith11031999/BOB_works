# Import necessary libraries
import streamlit as st
import pandas as pd
import yfinance as yf

# Define a function to fetch stock data
def fetch_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# Main Streamlit application code
def main():
    # Title and description for the app
    st.title('Financial Data Viewer')
    st.write('Enter a stock symbol and date range to view historical data.')

    # User input for stock symbol, start date, and end date
    symbol = st.text_input('Stock Symbol (e.g., AAPL)', 'AAPL')
    start_date = st.date_input('Start Date', value=pd.to_datetime('2020-01-01'))
    end_date = st.date_input('End Date', value=pd.to_datetime('2021-01-01'))

    # Fetch data button
    if st.button('Fetch Data'):
        # Fetch and display stock data
        st.write(f'Fetching data for {symbol} from {start_date} to {end_date}...')
        data = fetch_stock_data(symbol, start_date, end_date)
        st.write(data)

# Execute the main function
if __name__ == '__main__':
    main()
