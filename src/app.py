import json
import requests

from datetime import datetime
#from flask import Flask
from fastapi import FastAPI
from pydantic import BaseModel

date = datetime.now()
date_for_cnb_url = date.year + date.month + date.day

cnb_url = f"https://data.kurzy.cz/json/meny/b[6]den[{date_for_cnb_url}].json"
coinbase_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
 
#app = Flask(__name__)
app = FastAPI()


# Classes for the nested JSON response
class CurencySchema(BaseModel):
    #General contents of a currency

    request_time: str
    response_time: datetime
    EUR: float
    CZK: float

class BTC(BaseModel):
    # BTC schema

    BTC: CurencySchema

 
@app.get('/btc_info', response_model=BTC)
def exchange():
    """
    Gets BTC price from COINBASE, and returns prices in in EUR and CZK
    """

    request_time = datetime.utcnow().isoformat()

    # Gets exchange rate from the Czech National Bank
    rates = requests.get(cnb_url).json()['kurzy']
    rate_eur_to_czk = rates['EUR']['dev_stred']

    bpi = requests.get(coinbase_url).json() 
    bpi_eur_val = bpi['bpi']['EUR']['rate_float']
    
    
    data = {
                "BTC": {
                        "request_time": request_time,
                        "response_time": bpi['time']['updatedISO'],
                        "EUR": bpi_eur_val,
                        "CZK": bpi_eur_val*rate_eur_to_czk
                        }}

        

    return data
 
# main driver function
if __name__ == '__main__':
 
    app.run(debug=True)