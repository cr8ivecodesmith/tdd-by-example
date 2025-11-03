from tdd_by_example.currency import Money, Bank


def test_multiplication() -> None:
    five:Money = Money.dollar(5)

    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)


def test_equality() -> None:
    assert Money.dollar(5).equals(Money.dollar(5))
    assert not Money.dollar(5).equals(Money.dollar(6))
    assert not Money.franc(5).equals(Money.dollar(5))


def test_currency() -> None:
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()


def test_simple_addition() -> None:
    five:Money = Money.dollar(5)
    sum_:Expression = five.plus(five)
    bank:Bank = Bank()
    reduced:Money = bank.reduce(sum_, "USD")
    assert Money.dollar(10) == reduced
