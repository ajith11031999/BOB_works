import streamlit as st

# Streamlit interface for financial advisory
st.title("Personalized Financial Advisory")

# Collect customer data
age = st.number_input("Age")
investment_amount = st.number_input("Investment Amount")
risk_tolerance = st.selectbox("Risk Tolerance", ["low", "moderate", "high"])

if st.button("Get Advice"):
    customer_data = {
        "age": age,
        "investment_amount": investment_amount,
        "risk_tolerance": risk_tolerance
    }
    advice, explanation = generate_advisory(customer_data)
    st.write("Advice:", advice)
    st.write("Explanation:", explanation)
