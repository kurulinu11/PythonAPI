import requests
from pprint import pprint

# protocol = "https://"
# domain_name = "www.alphavantage.co"
function = "TIME_SERIES_INTRADAY"
symbol = input('Podaj nazwę spółki: ')
interval = "15min"
api_key = "6YMFGU47AXLMNQD5"

response = requests.get('https://www.alphavantage.co/query?', 
                        params = {
                            "function": function,
                            "symbol": symbol,
                            "interval": interval,
                            "apikey": api_key
                        })
# response = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={api_key}')

# def query_alphavantage(params):
#     return requests.get('https://www.alphavantage.co/query?', params = params)

data = response.json()
# prices = data.get('Time Series(15min)')
# volume = [int(price.get('5. volume')) for date, price in prices.items()]
pprint(data)