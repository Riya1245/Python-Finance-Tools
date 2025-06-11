import json # For potentially saving/loading exchange rates
import requests # If you decide to use a real API

class CurrencyConverter:
    def __init__(self):
        # Option 1: Static/Mocked Exchange Rates (simplest for a demo)
        self.exchange_rates = {
            "USD": {"EUR": 0.92, "GBP": 0.79, "JPY": 156.40, "INR": 83.50},
            "EUR": {"USD": 1.09, "GBP": 0.86, "JPY": 170.00, "INR": 91.00},
            "GBP": {"USD": 1.26, "EUR": 1.16, "JPY": 196.00, "INR": 105.00},
            "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "INR": 0.53},
            "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0095, "JPY": 1.88}
            # Add more currencies as needed
        }
        # Ensure symmetric rates (e.g., if USD->EUR exists, EUR->USD should be 1/rate)
        # Or load from a JSON file to make it configurable

        # Option 2: API Integration (more advanced) - Uncomment and configure if you use an API
        # self.api_base_url = "YOUR_CURRENCY_API_URL" # e.g., exchangerate-api.com, openexchangerates.org
        # self.api_key = "YOUR_API_KEY" # Get one if you use an API

    def get_exchange_rate(self, source_currency, target_currency):
        """Fetches or retrieves the exchange rate between two currencies."""
        if source_currency == target_currency:
            return 1.0

        # Option 1: Static/Mocked
        if source_currency in self.exchange_rates and target_currency in self.exchange_rates[source_currency]:
            return self.exchange_rates[source_currency][target_currency]
        elif target_currency in self.exchange_rates and source_currency in self.exchange_rates[target_currency]:
            # If direct rate not found, try inverse
            return 1 / self.exchange_rates[target_currency][source_currency]
        else:
            print(f"Error: Exchange rate not available for {source_currency} to {target_currency}")
            return None

        # Option 2: Using a real API (Example with a placeholder API)
        # try:
        #     response = requests.get(f"{self.api_base_url}/latest/{source_currency}?apikey={self.api_key}")
        #     data = response.json()
        #     if data and "rates" in data and target_currency in data["rates"]:
        #         return data["rates"][target_currency]
        #     else:
        #         print(f"Error fetching API rate: {data.get('error', 'Unknown error')}")
        #         return None
        # except requests.exceptions.RequestException as e:
        #     print(f"API request failed: {e}")
        #     return None


    def convert(self, amount, source_currency, target_currency):
        """Converts an amount from source to target currency."""
        if not isinstance(amount, (int, float)) or amount < 0:
            print("Invalid amount. Please enter a positive number.")
            return None

        rate = self.get_exchange_rate(source_currency, target_currency)
        if rate is not None:
            return amount * rate
        return None

    def get_available_currencies(self):
        """Returns a list of currencies for which rates are available."""
        return sorted(list(self.exchange_rates.keys()))
        # If using API, you might need an /available-currencies endpoint