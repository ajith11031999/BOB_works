from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API endpoints for NSE and BSE
NSE_ENDPOINT = 'https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O'
BSE_ENDPOINT = 'https://www.bseindia.com/data/StockReach.aspx'

# Function to fetch real-time stock data from NSE
def fetch_nse_stock_data(stock_name):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f'https://www.nseindia.com/api/quote-equity?symbol={stock_name}', headers=headers)
    data = response.json()
    return data

# Function to fetch real-time stock data from BSE
def fetch_bse_stock_data(stock_name):
    response = requests.get(f'https://api.bseindia.com/BseIndiaAPI/api/StockReachGraph/w?flag=0&quotetype=EQ&scripcode={stock_name}')
    data = response.json()
    return data

# Function to generate investment advice
def generate_advice(customer_details):
    investment_amount = customer_details.get('investment_amount', 0)
    stock_name = customer_details.get('stock_name')
    stock_exchange = customer_details.get('stock_exchange')
    
    if stock_name:
        if stock_exchange == 'NSE':
            stock_data = fetch_nse_stock_data(stock_name)
        elif stock_exchange == 'BSE':
            stock_data = fetch_bse_stock_data(stock_name)
        else:
            return "Invalid stock exchange selected."
        
        # Perform analysis and generate predictions (simplified example)
        advice = f"Based on current data from {stock_exchange}, it's advisable to consider {stock_name}."
    else:
        # Logic to suggest safe stocks based on investment_amount
        advice = f"Considering your investment amount of ${investment_amount}, here are some safe stock suggestions."

    return advice

@app.route('/get_advice', methods=['POST'])
def get_advice():
    data = request.get_json()
    advice = generate_advice(data)
    return jsonify({'advice': advice})

if __name__ == '__main__':
    app.run(debug=True)
