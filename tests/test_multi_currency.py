from tdd_by_example.currency import Dollar, Franc, Money


def test_multiplication() -> None:
    five:Money = Money.dollar(5)

    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)


def test_equality() -> None:
    assert Money.dollar(5).equals(Money.dollar(5))
    assert not Money.dollar(5).equals(Money.dollar(6))

    assert Franc(5).equals(Franc(5))
    assert not Franc(5).equals(Franc(6))

    assert not Franc(5).equals(Money.dollar(5))


def test_franc_multiplication() -> None:
    five:Franc = Franc(5)

    assert five.times(2) == Franc(10)
    assert five.times(3) == Franc(15)
