import requests
from requests import get
from pprint import PrettyPrinter
from requests.structures import CaseInsensitiveDict

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "9vDqwB7aWVD3WxBMQWVf93xwYhcF2qoKa4lnx3zW"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['data']
    data = list(data.items())
    data.sort()
    return data
    
data = get_currencies()
printer.pprint(data)