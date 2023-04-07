from abc import ABC, abstractmethod
from typing import Union

import pytest

Cur = Union[int, float]


class CentralBank:
    """CentralBank is a class for representing Central Bank."""

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return None

    @classmethod
    def register(cls, money):
        """Register money object."""
        money.cb = cls


class MoneyBase(ABC):
    """MoneyBase is a base class for representing money in a currency."""

    def __init__(self, volume: Cur = 0):
        self.__volume = volume
        self.__cb = None

    @property
    def volume(self) -> Cur:
        return self.__volume

    @volume.setter
    def volume(self, value: Cur) -> None:
        self.__volume = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.volume})"

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    @abstractmethod
    def currency(cls):
        pass

    def _to_usd(self):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        self_currency = self.currency
        if self_currency == 'rub':
            return self.volume
        if self_currency == 'dollar':
            return self.volume * self.cb.rates['rub']
        if self_currency == 'euro':
            return self.volume * self.cb.rates['rub'] * self.cb.rates['euro']

    def __eq__(self, other):
        return abs(self._to_usd() - other._to_usd()) < 0.1

    def __lt__(self, other):
        return self._to_usd() < other._to_usd()


class MoneyR(MoneyBase):
    currency = 'rub'


class MoneyD(MoneyBase):
    currency = 'dollar'


class MoneyE(MoneyBase):
    currency = 'euro'


###################################################


def test_job():
    r = MoneyR(45000)
    d = MoneyD(500)
    CentralBank.register(r)
    CentralBank.register(d)
    assert r.cb is CentralBank
    assert r > d


def test_job1():
    r = MoneyR(20000)
    d = MoneyD(500)
    CentralBank.register(r)
    CentralBank.register(d)
    assert r < d


def test_create_money_class_without_currency_variable():
    class Money(MoneyBase):
        pass
    with pytest.raises(TypeError):
        Money()

if __name__ == '__main__':
    pytest.main([__file__])
