"""Currency module defining different currency classes."""
from __future__ import annotations

from abc import ABC, abstractmethod


class Money(ABC):

    _amount: int

    @property
    def amount(self) -> int:
        return self._amount

    @staticmethod
    def dollar(amount: int) -> Dollar:
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Franc:
        return Franc(amount)

    @abstractmethod
    def currency(self): pass

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def equals(self, other: Money) -> bool:
        return (
            self.amount == other.amount
            and isinstance(other, type(self))
        )

    def __eq__(self, other: Money) -> bool:
        return self.equals(other)

    def __repr__(self) -> str:  # pragma: no cover
        return f"{type(self).__name__}({self.amount})"


class Dollar(Money):

    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)

    def currency(self):
        return "USD"


class Franc(Money):

    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)

    def currency(self):
        return "CHF"
