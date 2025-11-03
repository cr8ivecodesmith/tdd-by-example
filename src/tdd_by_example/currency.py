"""Currency module defining different currency classes."""


class Money:

    _amount: int

    @property
    def amount(self) -> int:
        return self._amount

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def equals(self, other: "Money") -> bool:
        other = Money(other.amount)
        return self.amount == other.amount

    def __eq__(self, other: "Money") -> bool:
        return self.equals(other)


class Dollar(Money):

    _amount: int

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> "Dollar":
        return Dollar(self._amount * multiplier)


class Franc:

    _amount: int

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> "Franc":
        return Franc(self._amount * multiplier)

    def equals(self, other: "Franc") -> bool:
        return self._amount == other._amount

    def __eq__(self, other: "Franc") -> bool:
        return self.equals(other)
