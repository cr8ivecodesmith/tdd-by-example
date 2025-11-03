"""Currency module defining different currency classes."""
from __future__ import annotations

from abc import ABC, abstractmethod


class Pair:
    """Currency pair used for rate lookup"""

    from_currency: str
    to_currency: str

    def __repr__(self):  # pragma: no cover
        return (
            f"{type(self).__name__}({self.from_currency}, {self.to_currency})"
        )

    def __init__(self, from_currency: str, to_currency: str):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def __eq__(self, other):
        return (
            self.from_currency == other.from_currency
            and self.to_currency == other.to_currency
        )

    def __hash__(self):
        return hash((self.from_currency, self.to_currency))


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

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str) -> Money:
        rate: int = bank.rate(self._currency, to)
        return Money(self._amount // rate, to)


class Expression(Money):
    """
    An Expression is Money resulting from an Operation between two
    money objects.

    """

    def reduce(self, bank: Bank, to: str) -> Money: pass

    def plus(self, addend: Expression) -> Expression: pass


class Bank:
    """
    A Bank reduces an Expression object back to single currency
    given a set of exchange rates.

    """

    rates: dict = {}

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, from_currency: str, to_currency: str, rate: int) -> None:
        self.rates[Pair(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        if from_currency == to_currency: return 1
        pair = Pair(from_currency, to_currency)
        return self.rates.get(pair)


class Sum(Expression):
    """
    A Sum is a resulf from a `plus` Expression.

    """
    augend: Expression
    addend: Expression

    @classmethod
    def from_expression(cls, expr: Expression) -> Sum:
        return cls(expr.augend, expr.addend)

    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to: str) -> Money:
        amount: int = (
            self.augend.reduce(bank, to)._amount
            + self.addend.reduce(bank, to)._amount
        )
        return Money(amount, to)

    def plus(self, addend: Expression) -> Expression: pass
