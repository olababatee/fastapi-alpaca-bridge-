from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()
API_KEY = os.getenv("APCA-API_KEY-ID")
API_SECRET = os.getenv("APCA-API_SECRET-KEY")

BASE_URL = "https://paper-api.alpaca.markets"

class TradeRequest(BaseModel):
    symbol: str
    qty: int
    side: str
    type: str = "market"
    time_in_force: str = "day"

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
def place_trade(order: TradeRequest):
    headers = {
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET,
        "Content-Type": "application/json"
    }
    
    order_data = {
        "symbol": order.symbol.upper(),
        "qty": order.qty,
        "side": order.side.lower(),
        "type": order.type,
        "time_in_force": order.time_in_force
    }
    
    response = requests.post(
        f"{BASE_URL}/v2/orders", 
        json=order_data, 
        headers=headers
    )
    
    return {
        "status_code": response.status_code,
        "alpaca_response": response.json()
    }
