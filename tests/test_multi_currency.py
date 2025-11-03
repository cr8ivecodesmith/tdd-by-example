from tdd_by_example.currency import Money, Bank, Sum, Expression


def test_multiplication() -> None:
    five: Money = Money.dollar(5)

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
    five: Money = Money.dollar(5)
    sum_: Expression = five.plus(five)
    bank: Bank = Bank()
    reduced: Money = bank.reduce(sum_, "USD")
    assert Money.dollar(10) == reduced


def test_plus_returns_sum() -> None:
    five: Money = Money.dollar(5)
    result: Expression = five.plus(five)
    sum_: Sum = Sum.from_expression(result)
    assert five == sum_.augend
    assert five == sum_.addend


def test_reduce_sum() -> None:
    sum_: Expression = Sum(Money.dollar(3), Money.dollar(4))
    bank: Bank = Bank()
    result: Money = bank.reduce(sum_, "USD")
    assert Money.dollar(7) == result


def test_reduce_money() -> None:
    bank: Bank = Bank()
    result: Money = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result


def test_reduce_money_different_currency() -> None:
    bank: Bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result: Money = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result


def test_identity_rate() -> None:
    assert 1 == Bank().rate("USD", "USD")


def test_mixed_addition() -> None:
    five_bucks: Expression = Money.dollar(5)
    ten_francs: Expression = Money.franc(10)
    bank: Bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result: Money = bank.reduce(
        five_bucks.plus(ten_francs),
        "USD"
    )
    assert Money.dollar(10) == result
