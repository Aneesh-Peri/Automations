import requests

API_KEY = "fca_live_8GkoWgXPkoVETkmSHgIaPQyjdrIICtlBsCP7PJmT"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None


while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break
    amount = int(input("Enter your amount as a integer: "))
    final = input("Enter the currency you want to convert to: ")
    data = convert_currency(base)
    if not data:
        continue
    value = data[final] * amount
    print(f"{amount} {base} dollars in {final} is {value}")
    del data[base]
    print("Below are the exchange rates: ")
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
