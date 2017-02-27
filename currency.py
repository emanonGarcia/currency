#!/usr/bin/env python3
class DifferentCurrencyCodeError(Exception):
        pass


class Currency:
    """docstring for ."""
    # Belongs to the class no the instance
    CURRENCY_CODE = {'USD': '$', 'EUR': '€', 'JPY': '¥', 'GBP': '£'}

    def __init__(self, amount, code=''):
        if code:
            self.code = code
            self.amount = amount
        else:
            for currency, symbol in self.CURRENCY_CODE.items():
                if amount[0] == symbol:
                    self.code = currency
                    self.amount = amount[1:]
        try:
            self.amount = float(self.amount)
        except ValueError:
            print("Can not convert str to float")

    def __add__(self, other):
        if self.code == other.code:
            new_amount = self.amount + other.amount
            return Currency(new_amount, self.code)
        else:
            raise DifferentCurrencyCodeError("Currency codes do not match")

    def __sub__(self, other):
        if self.code == other.code:
            new_amount = self.amount - other.amount
            return Currency(new_amount, self.code)
        else:
            raise DifferentCurrencyCodeError("Currency codes do not match")

    def __mul__(self, other):
        if self.code == other.code:
            new_amount = self.amount * other.amount
            return Currency(new_amount, self.code)
        else:
            raise DifferentCurrencyCodeError("Currency codes do not match")

    def __eq__(self, other):
        return self.code == other.code and self.amount == other.amount

    def __ne__(self, other):
        return self.code != other.code or self.amount != other.amount

    def __str__(self):
        try:
            return "{0}{1:0.2f}".format(self.CURRENCY_CODE[self.code], self.amount)
        except:
            return "{0}{1:0.2f}".format(self.code, self.amount)


money = Currency('5.90', 'USD')
print(money)

other_money = Currency('$5')
print(other_money)

print(money + other_money)
print(money - other_money)
print(money != other_money)
print(money == other_money)
print(money * other_money)
