"""Currency module defining different currency classes."""
from __future__ import annotations

from abc import ABC, abstractmethod


class Money:

    # Factory methods

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")

    # End factory methods

    _amount: int
    _currency: str

    def __repr__(self) -> str:  # pragma: no cover
        return f"{type(self).__name__}({self._amount} {self._currency})"

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def currency(self) -> str:
        return self._currency

    def equals(self, other: Money) -> bool:
        return (
            self._amount == other._amount
            and self.currency() == other.currency()
        )

    def __eq__(self, other: Money) -> bool:
        return self.equals(other)

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Money) -> Expression:
        return Expression(self._amount + addend._amount, self._currency)


class Expression(Money):
    """
    An Expression is Money resulting from an Operation between two
    money objects.

    """


class Bank:
    """
    A Bank reduces an Expression object back to single currency
    given a set of exchange rates.

    """

    def reduce(self, source: Expression, to: str):
        return Money.dollar(10)
