from currency import Currency, DifferentCurrencyCodeError

from nose.tools import raises


@raises(DifferentCurrencyCodeError)
def test_different_currency_code_error():
    Currency(5, "USD") + Currency(5, "JPY")


@raises(DifferentCurrencyCodeError)
def test_different_currency_code_error():
    Currency(5, "GBP") - Currency(5, "EUR")


@raises(DifferentCurrencyCodeError)
def test_different_currency_code_error():
    Currency(5, "USD") * Currency(5, "JPY")


def test_are_ne():
    Currency(5, "USD") != Currency(5, "JPY") == True


def test_are_eq_same_style():
    Currency(5, "EUR") == Currency(5, "EUR") == True


def test_are_eq_diff_style():
    Currency(5, "JPY") == Currency('¥5') == True


def test_add_instances():
    Currency(15, "USD") + Currency(5, "USD") == Currency('$20')


def test_sub_instances():
    Currency(5, "USD") + Currency(15, "USD") == Currency('$-10')
