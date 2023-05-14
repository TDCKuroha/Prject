from requests import get
from pprint import PrettyPrinter
from requests.structures import CaseInsensitiveDict

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "9vDqwB7aWVD3WxBMQWVf93xwYhcF2qoKa4lnx3zW"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"v1/currencies?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['data']
    data = list(data.items())
    data.sort()
    return data
    
    
def print_currencies(currencies):
        for name, currency in currencies:
            name = currency['name']
            _id = currency['code']
            symbol = currency.get("symbol_native", "")
            print(f"{_id} - {name} - {symbol}")


def exchange_rate(base_currency, currencies):
    endpoint = f"v1/latest?base_currency={base_currency}&currencies={currencies}&apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    
    if "data" in data:
        exchange_rates = data["data"]
        for currency, rate in exchange_rates.items():
            print(f"The exchange rate from {base_currency} to {currency} is: {rate}")
    else:
        print("Unable to retrieve exchange rates.")
    
    return rate

def convert(base_currency, currencies, amount):
    rate = exchange_rate(base_currency, currencies)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        
    
    converted_amount = rate * amount
    print(f"{amount} {base_currency} is equal to {converted_amount} {currencies}")
    return converted_amount

def main():
    currencies = get_currencies()
    
    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()
    
    while True:
        command = input("Enter a command (q to quit): ").lower()
        
        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            base_currency = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {base_currency}: ")
            currencies = input("Enter a currency to convert to: ").upper()
            convert(base_currency,currencies,amount)
        elif command == "rate":
            base_currency = input("Enter a base currency: ").upper()
            currency = input("Enter a currency to convert to: ").upper()
            exchange_rate(base_currency,currency)
        else:
            print("Unrecognized command!")
            
main()