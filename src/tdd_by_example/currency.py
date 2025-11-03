"""Currency module defining different currency classes."""
from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, runtime_checkable


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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pair):  # pragma: no cover
            return NotImplemented
        return (
            self.from_currency == other.from_currency
            and self.to_currency == other.to_currency
        )

    def __hash__(self):
        return hash((self.from_currency, self.to_currency))


@runtime_checkable
class Expression(Protocol):
    """
    An Expression is Money resulting from an Operation between two
    money objects.

    """

    @abstractmethod
    def reduce(self, bank: Bank, to: str) -> Money: pass

    @abstractmethod
    def plus(self, addend: Expression) -> Expression: pass

    @abstractmethod
    def times(self, multiplier: int) -> Expression: pass


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

    @property
    def amount(self):
        return self._amount

    def currency(self) -> str:
        return self._currency

    def equals(self, other: Money) -> bool:
        return (
            self._amount == other._amount
            and self.currency() == other.currency()
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):  # pragma: no cover
            return NotImplemented
        return self.equals(other)

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str) -> Money:
        rate: int = bank.rate(self._currency, to)
        return Money(self._amount // rate, to)


class Bank:
    """
    A Bank reduces an Expression object back to single currency
    given a set of exchange rates.

    """

    def __init__(self) -> None:
        self.rates: dict[Pair, int] = {}

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, from_currency: str, to_currency: str, rate: int) -> None:
        self.rates[Pair(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str) -> int:
        if from_currency == to_currency:
            return 1
        return self.rates.get(Pair(from_currency, to_currency), 1)


class Sum:
    """
    A Sum is a resulf from a `plus` Expression.

    """

    @classmethod
    def from_expression(cls, expr: Expression) -> Sum:
        if not isinstance(expr, Sum):  # pragma: no cover
            raise TypeError(f"Expecting Sum, got {type(expr).__name__}.")
        return cls(expr.augend, expr.addend)

    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to: str) -> Money:
        amount: int = (
            self.augend.reduce(bank, to).amount
            + self.addend.reduce(bank, to).amount
        )
        return Money(amount, to)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        return Sum(
            self.augend.times(multiplier),
            self.addend.times(multiplier)
        )
