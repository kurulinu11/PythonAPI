import requests
from pprint import pprint

params1 = {
    "function" : "TIME_SERIES_INTRADAY",
    "symbol" : "AAPL",
    "interval" : "15min",
    "apikey" : "E5M4M0UIPVQEG7XG"
    }

params2 = {
    "function" : "INCOME_STATEMENT",
    "symbol" : "AAPL",
    "apikey" : "E5M4M0UIPVQEG7XG"
    }

def query_alphavantage(params):
    return requests.get('https://www.alphavantage.co/query?', params=params)

response1 = query_alphavantage(params1)
response2 = query_alphavantage(params2)
# data = response1.json()
data = response2.json()
pprint(data)