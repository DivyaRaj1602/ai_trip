import requests

class CurrencyConverter:
    def __init__(self, api_key: str):
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
    
    def convert(self, amount:float, from_currency:str, to_currency:str):
        """Convert the amount from one currency to another"""
        if not self.base_url or "your_" in self.base_url:
            return f"Currency conversion not available (API key not configured). Estimated: {amount} {from_currency} ≈ {amount} {to_currency}"
        try:
            url = f"{self.base_url}/{from_currency}"
            response = requests.get(url)
            if response.status_code != 200:
                return f"Currency conversion failed. Estimated: {amount} {from_currency} ≈ {amount} {to_currency}"
            rates = response.json()["conversion_rates"]
            if to_currency not in rates:
                return f"Currency {to_currency} not found. Estimated: {amount} {from_currency} ≈ {amount} {to_currency}"
            return amount * rates[to_currency]
        except Exception as e:
            return f"Currency conversion error. Estimated: {amount} {from_currency} ≈ {amount} {to_currency}"