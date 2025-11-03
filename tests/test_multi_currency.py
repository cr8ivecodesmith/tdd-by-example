from tdd_by_example.currency import Dollar, Franc, Money


def test_multiplication() -> None:
    five:Money = Money.dollar(5)

    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)


def test_equality() -> None:
    assert Money.dollar(5).equals(Money.dollar(5))
    assert not Money.dollar(5).equals(Money.dollar(6))

    assert Money.franc(5).equals(Money.franc(5))
    assert not Money.franc(5).equals(Money.franc(6))

    assert not Money.franc(5).equals(Money.dollar(5))


def test_franc_multiplication() -> None:
    five:Franc = Money.franc(5)

    assert five.times(2) == Money.franc(10)
    assert five.times(3) == Money.franc(15)
