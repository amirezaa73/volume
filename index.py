from flask import Flask, jsonify
from binance.client import Client

app = Flask(__name__)

# توکن API خود را وارد کنید
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
client = Client(api_key, api_secret)

@app.route('/')
def home():
    return jsonify({"message": "API is running on Vercel!"})

@app.route('/binance', methods=['GET'])
def get_binance_price():
    try:
        # گرفتن قیمت بیت‌کوین به تتر (BTC/USDT)
        price = client.get_symbol_ticker(symbol="BTCUSDT")
        return jsonify(price)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch data from Binance: {str(e)}"}), 500
