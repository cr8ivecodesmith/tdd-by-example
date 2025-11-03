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
        return Sum(self, addend)

    def reduce(self, to: str) -> Money:
        return self


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
        if isinstance(source, Money):
            return source.reduce(to)
        sum_: Sum = Sum.from_expression(source)
        return sum_.reduce(to)


class Sum(Expression):
    """
    A Sum is a resulf from a `plus` Expression.

    """
    augend: Money
    addend: Money

    @classmethod
    def from_expression(cls, expr: Expression):
        return cls(expr.augend, expr.addend)

    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> Money:
        amount: int = self.augend._amount + self.addend._amount
        return Money(amount, to)
