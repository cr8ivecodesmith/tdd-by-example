from tdd_by_example.currency import Dollar


def test_multiplication() -> None:
    five = Dollar(5)

    assert five.times(2) == Dollar(10)
    assert five.times(3) == Dollar(15)


def test_equality() -> None:
    assert Dollar(5).equals(Dollar(5))
    assert not Dollar(5).equals(Dollar(6))
