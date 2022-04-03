import requests
from pprint import pprint

function = "TIME_SERIES_INTRADAY"
symbol = input("Podaj nazwę spółki: ")
interval = "15min"
api_key = "E5M4M0UIPVQEG7XG"

response = requests.get('https://www.alphavantage.co/query?', 
                        params = {
                            "function": function,
                            "symbol": symbol,
                            "interval": interval,
                            "apikey": api_key
                        })

data = response.json()
prices = data.get('Time Series(15min)')
volume = [int(price.get('5. volume')) for date, price in prices.items()]
pprint(sorted(volume))