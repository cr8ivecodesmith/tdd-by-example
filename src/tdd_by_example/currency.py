"""Currency module defining different currency classes."""
from __future__ import annotations

from abc import ABC, abstractmethod


class Money(ABC):

    _amount: int
    _currency: str

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
            self._amount == other._amount
            and isinstance(other, type(self))
        )

    def __eq__(self, other: Money) -> bool:
        return self.equals(other)

    def __repr__(self) -> str:  # pragma: no cover
        return f"{type(self).__name__}({self._amount})"


class Dollar(Money):

    __currency: str

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self.__currency = "USD"

    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)

    def currency(self):
        return "USD"


class Franc(Money):

    __currency: str

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self.__currency = "CHF"

    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)

    def currency(self):
        return "CHF"
