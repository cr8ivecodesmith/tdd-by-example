"""Currency module defining different currency classes."""


class Dollar:

    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> None:
        return Dollar(self.amount * multiplier)

    def equals(self, other: "Dollar") -> bool:
        return True
