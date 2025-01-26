from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API is running on Vercel!"})

@app.route('/binance', methods=['GET'])
def get_binance_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return jsonify(response.json())  # Return the JSON response from Binance
    except requests.exceptions.RequestException as e:
        # Return the exact error response from Binance, if available
        if response is not None and response.text:
            return jsonify({"error": "Binance API Error", "details": response.text}), response.status_code
        else:
            return jsonify({"error": "Request failed", "details": str(e)}), 500
