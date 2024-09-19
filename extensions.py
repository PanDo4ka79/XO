import requests
import json


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float) -> float:
        url = f'https://api.exchangerate-api.com/v4/latest/{base}'
        response = requests.get(url)
        if response.status_code != 200:
            raise APIException(f'Error fetching data from API: {response.status_code}')

        data = response.json()
        if quote not in data['rates']:
            raise APIException(f'Invalid quote currency: {quote}')

        rate = data['rates'][quote]
        return round(rate * amount, 2)
