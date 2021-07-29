import requests
import json
from config import keys


class ConversionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException(f'Выбраны две одинаковые валюты: {quote}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}')

        try:
            amount != float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количетсво {amount}')

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/6abc60cfa9152c9ede480636/pair/{quote_ticker}/{base_ticker}/{amount}'
        )
        total_base = json.loads(r.content)['conversion_result']

        return total_base
