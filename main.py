import os
from fastapi import FastAPI, HTTPException
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

app = FastAPI()

API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")

trading_client = TradingClient(API_KEY, API_SECRET, paper=True)

@app.get("/")
def read_root():
    return {"message": "Alpaca Trading Bridge is Live!"}

@app.get("/account")
def get_account():
    try:
        account = trading_client.get_account()
        return {
            "status": account.status,
            "cash": account.cash,
            "portfolio_value": account.portfolio_value,
            "buying_power": account.buying_power
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/trade/buy")
def buy_stock(symbol: str, qty: float):
    try:
        order_data = MarketOrderRequest(
            symbol=symbol.upper(),
            qty=qty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        order = trading_client.submit_order(order_data=order_data)
        return {
            "status": "success",
            "order_id": str(order.id),
            "symbol": order.symbol,
            "qty": order.qty,
            "side": order.side
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
