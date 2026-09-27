import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

API_KEY = "PKUQFLJNKYWFTJTKVVRZOVE56J"
API_SECRET = "JBMK6uo7WY1pC2PoxHfDatctJfHJLoQ3FgVxf2XhM54"
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
