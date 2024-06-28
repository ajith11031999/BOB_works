import streamlit as st
import pandas as pd
import yfinance as yf

def fetch_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

def main():
    st.title('Financial Data Viewer')
    st.write('Enter a stock symbol and date range to view historical data.')

    symbol = st.text_input('Stock Symbol (e.g., AAPL)', 'AAPL')
    start_date = st.date_input('Start Date', value=pd.to_datetime('2020-01-01'))
    end_date = st.date_input('End Date', value=pd.to_datetime('2021-01-01'))

    if st.button('Fetch Data'):
        st.write(f'Fetching data for {symbol} from {start_date} to {end_date}...')
        try:
            data = fetch_stock_data(symbol, start_date, end_date)
            st.write(data)
        except Exception as e:
            st.error(f"Error fetching data: {str(e)}")

if __name__ == '__main__':
    main()
