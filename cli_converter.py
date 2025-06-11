from currency_converter import CurrencyConverter

def main_cli():
    converter = CurrencyConverter()
    print("--- currency Converter (CLI) ---")

    currencies = converter.get_available_currencies()
    if not currencies:
        print("No currencies available for conversion. Exiting.")
        return

    print(f"Available currencies: {', '.join(currencies)}")

    while True:
        try:
            amount_str = input("Enter amount to convert (e.g., 100): ")
            amount = float(amount_str)
            if amount < 0:
                print("Amount cannot be negative.")
                continue

            source = input("Enter source currency (e.g., USD): ").upper()
            target = input("Enter target currency (e.g., EUR): ").upper()

            if source not in currencies or target not in currencies:
                print("Invalid currency code(s). Please use one of the available currencies.")
                continue

            converted_amount = converter.convert(amount, source, target)

            if converted_amount is not None:
                print(f"{amount} {source} = {converted_amount:.2f} {target}")

            another_conversion = input("Convert another amount? (yes/no): ").lower()
            if another_conversion != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter a number for the amount.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_cli()