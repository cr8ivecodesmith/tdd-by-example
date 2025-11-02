from tdd_by_example.currency import Dollar


def test_multiplication() -> None:
    five = Dollar(5)

    product = five.times(2)
    assert product.amount == 10

    product = five.times(3)
    assert product.amount == 15
