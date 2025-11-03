"""Currency module defining different currency classes."""


class Money:

    _amount: int

    @property
    def amount(self) -> int:
        return self._amount

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def equals(self, other: "Money") -> bool:
        return (
            self.amount == other.amount
            and isinstance(other, type(self))
        )

    def __eq__(self, other: "Money") -> bool:
        return self.equals(other)

    def __repr__(self) -> str:  # pragma: no cover
        return f"{type(self).__name__}({self.amount})"


class Dollar(Money):

    def times(self, multiplier: int) -> "Money":
        return Dollar(self._amount * multiplier)


class Franc(Money):

    def times(self, multiplier: int) -> "Money":
        return Franc(self._amount * multiplier)
