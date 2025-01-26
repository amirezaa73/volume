from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API is running on Vercel!"})

@app.route('/bybit', methods=['GET'])
def get_bybit_data():
    url = "https://api.bybit.com/v5/market/kline?category=spot&symbol=BTCUSDT&interval=60"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return jsonify(response.json())  # Return the JSON response from Bybit
    except requests.exceptions.RequestException as e:
        # Return the exact error response from Bybit, if available
        if response is not None and response.text:
            return jsonify({"error": "Bybit API Error", "details": response.text}), response.status_code
        else:
            return jsonify({"error": "Request failed", "details": str(e)}), 500
