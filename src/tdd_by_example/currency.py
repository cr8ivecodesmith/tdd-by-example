"""Currency module defining different currency classes."""


class Dollar:

    _amount: int

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> "Dollar":
        return Dollar(self._amount * multiplier)

    def equals(self, other: "Dollar") -> bool:
        return self._amount == other._amount

    def __eq__(self, other: "Dollar") -> bool:
        return self.equals(other)
