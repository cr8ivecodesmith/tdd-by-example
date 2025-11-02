import pytest


def test_multiplication() -> None:
    five = Dollar(5)
    five.times(2)
    assert five.amount == 10
