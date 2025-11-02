import pytest


class Dollar:

    amount: int

    def __init__(self, amount: int) -> None:

        self.amount = 10

    def times(self, multiplier: int) -> None:
        pass



def test_multiplication() -> None:
    five = Dollar(5)
    five.times(2)
    assert five.amount == 10
