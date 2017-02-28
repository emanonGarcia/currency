#!/usr/bin/env python3
from currency import Currency

class DifferentCurrencyCodeError(Exception):
    pass


class UnknownCurrencyCodeError(Exception):
    pass


class CurrencyConverter(Currency):

    def __init__(self, currency_convertions={'USD': 1.0, 'EUR': 0.74}, **kwargs):
        if isinstance(currency_convertions, dict):
            self.conversion_dict = currency_convertions
        else:
            raise ValueError
        for key, value in kwargs.items():
            self.conversion_dict[key] = value

    def convert(self, currency, conversion_unit):
        pass

    def __str__():
        pass
