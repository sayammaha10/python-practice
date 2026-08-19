from requests import get

BASE_URL = "https://api.frankfurter.dev/v1/"


def get_currencies():
    url = BASE_URL + "currencies"

    response = get(url)
    data = response.json()

    currencies = list(data.items())
    currencies.sort()

    return currencies


def print_currencies(currencies):
    print("\nAvailable Currencies")
    print("-" * 40)

    for code, name in currencies:
        print(f"{code} - {name}")

    print("-" * 40)


def exchange_rate(currency1, currency2):
    url = f"{BASE_URL}latest?base={currency1}&symbols={currency2}"

    response = get(url)
    data = response.json()

    if "rates" not in data or currency2 not in data["rates"]:
        print("\nInvalid currency code.")
        return None

    rate = data["rates"][currency2]

    print("\nExchange Rate")
    print("-" * 40)
    print(f"1 {currency1} = {rate} {currency2}")

    return rate


def convert_currency(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)

    if rate is None:
        return

    try:
        amount = float(amount)
    except ValueError:
        print("\nInvalid amount. Please enter a number.")
        return

    converted_amount = rate * amount

    print("\nConversion Result")
    print("-" * 40)
    print(f"{amount:.2f} {currency1} = {converted_amount:.2f} {currency2}")

    return converted_amount


def main():
    currencies = get_currencies()

    print("=" * 40)
    print("Currency Converter")
    print("=" * 40)
    print("Available commands:")
    print("  list     - List currencies")
    print("  convert  - Convert currency")
    print("  rate     - Get exchange rate")
    print("  q        - Quit")
    print("=" * 40)

    while True:
        command = input("\nEnter a command: ").lower()

        if command == "q":
            print("\nThank you for using the Currency Converter.")
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            print("\nCurrency Conversion")

            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()

            convert_currency(currency1, currency2, amount)
        elif command == "rate":
            print("\nExchange Rate Lookup")

            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()

            exchange_rate(currency1, currency2)
        else:
            print("\nInvalid command. Please choose from the available commands.")


if __name__ == "__main__":
    main()
