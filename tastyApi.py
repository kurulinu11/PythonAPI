import requests
from pprint import pprint

url = "https://tasty.p.rapidapi.com/recipes/list"

querystring = {"from":"0","size":"20","tags":"under_30_minutes"}

headers = {
	"X-RapidAPI-Host": "tasty.p.rapidapi.com",
	"X-RapidAPI-Key": "c502039ecdmshb0f7431a3a2e412p185106jsn80a388096fcf"
}

response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.text)