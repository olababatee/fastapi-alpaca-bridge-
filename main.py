import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

API_KEY = "PK7CPILVBNLWPPWGOBDTP6YPRL"
API_SECRET = "FZhcbFPWc73BJAxoYEPUjE8wh5QSfsLFVjkEmn7CsrAX"
BASE_URL = "https://paper-api.alpaca.markets"

@app.get("/")
def read_root():
    return {"message": "Alpaca Trading Bridge is Live!"}

@app.get("/account")
def get_account():
    headers = {
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET
    }
    response = requests.get(f"{BASE_URL}/v2/account", headers=headers)
    
    return {
        "status_code": response.status_code,
        "alpaca_response": response.json()
    }
@app.post("/trade")
def place_trade(symbol: str, qty: int, side: str):
    headers = {
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET,
        "Content-Type": "application/json"
    }
    
    order_data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,  # "buy" or "sell"
        "type": "market",
        "time_in_force": "day"
    }
    
    response = requests.post(f"{BASE_URL}/v2/orders", json=order_data, headers=headers)
    
    return {
        "status_code": response.status_code,
        "alpaca_response": response.json()
    }
