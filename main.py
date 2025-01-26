from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/binance")
def get_binance_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from Binance"}
