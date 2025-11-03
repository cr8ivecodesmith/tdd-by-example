"""Currency module defining different currency classes."""
from __future__ import annotations


class Money:

    _amount: int
    _currency: str

    @staticmethod
    def dollar(amount: int) -> Money:
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Franc(amount, "CHF")

    def currency(self) -> str:
        return self._currency

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def equals(self, other: Money) -> bool:
        return (
            self._amount == other._amount
            and self.currency() == other.currency()
        )

    def __eq__(self, other: Money) -> bool:
        return self.equals(other)

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def __repr__(self) -> str:  # pragma: no cover
        return f"{type(self).__name__}({self._amount} {self._currency})"


class Dollar(Money):

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)

    def dollar(self, amount: int) -> Money:
        return Money(amount, "USD")


class Franc(Money):

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)

    def franc(self, amount: int) -> Money:
        return Money(amount, "CHF")
