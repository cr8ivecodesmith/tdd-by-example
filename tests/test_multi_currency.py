import pytest


class Dollar:

    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> None:
        self.amount *= multiplier



def test_multiplication() -> None:
    five = Dollar(5)
    five.times(2)
    assert five.amount == 10
