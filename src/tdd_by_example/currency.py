"""Currency module defining different currency classes."""
from __future__ import annotations

from abc import ABC, abstractmethod


class Money(ABC):

    _amount: int

    @staticmethod
    def dollar(amount: int) -> Money:
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Franc(amount, "CHF")

    @abstractmethod
    def currency(self) -> str: pass

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def equals(self, other: Money) -> bool:
        return (
            self._amount == other._amount
            and isinstance(other, type(self))
        )

    def __eq__(self, other: Money) -> bool:
        return self.equals(other)

    def __repr__(self) -> str:  # pragma: no cover
        return f"{type(self).__name__}({self._amount})"


class Dollar(Money):

    __currency: str

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount)
        self.__currency = currency

    def times(self, multiplier: int) -> Money:
        return Money.dollar(self._amount * multiplier)

    def currency(self):
        return self.__currency


class Franc(Money):

    __currency: str

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount)
        self.__currency = currency

    def times(self, multiplier: int) -> Money:
        return Money.franc(self._amount * multiplier)

    def currency(self):
        return self.__currency
