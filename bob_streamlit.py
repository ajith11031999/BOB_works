# streamlit_app.py

import streamlit as st
from financial_advisor import generate_advisory, get_stock_data

def main():
    st.title("Personalized Financial Advisory")

    # Collect customer data
    age = st.number_input("Age")
    investment_amount = st.number_input("Investment Amount")
    risk_tolerance = st.selectbox("Risk Tolerance", ["low", "moderate", "high"])

    # Input for stock symbol
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL)")

    if st.button("Get Advice"):
        customer_data = {
            "age": age,
            "investment_amount": investment_amount,
            "risk_tolerance": risk_tolerance
        }
        
        # Fetch real-time stock data
        stock_data = get_stock_data(stock_symbol)

        # Generate advisory based on customer and stock data
        advice, explanation = generate_advisory(customer_data, stock_data)
        st.write("Advice:", advice)
        st.write("Explanation:", explanation)

if __name__ == "__main__":
    main()
