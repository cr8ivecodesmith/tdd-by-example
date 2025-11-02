import pytest


class Dollar:

    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> None:
        self.amount *= multiplier



def test_multiplication() -> None:
    five = Dollar(5)

    product = five.times(2)
    assert product.amount == 10

    product = five.times(3)
    assert product.amount == 15
