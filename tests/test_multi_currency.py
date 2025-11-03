from tdd_by_example.currency import Money


def test_multiplication() -> None:
    five:Money = Money.dollar(5)

    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)


def test_equality() -> None:
    assert Money.dollar(5).equals(Money.dollar(5))
    assert not Money.dollar(5).equals(Money.dollar(6))
    assert not Money.franc(5).equals(Money.dollar(5))


def test_franc_multiplication() -> None:
    five:Money = Money.franc(5)

    assert five.times(2) == Money.franc(10)
    assert five.times(3) == Money.franc(15)


def test_currency() -> None:
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()
