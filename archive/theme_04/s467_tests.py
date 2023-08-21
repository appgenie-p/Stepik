import pytest
from s467 import Money, MoneyR, MoneyD


def test_money_class():
    money = Money(100)
    assert money.money == 100

    # Test setting money with valid value
    money.money = 200
    assert money.money == 200

    # Test setting money with invalid value
    with pytest.raises(TypeError):
        money.money = "invalid"

    # Test setting money with another valid value
    money.money = 300.5
    assert money.money == 300.5


def test_money_creation_with_invalid_argument():
    with pytest.raises(TypeError):
        Money("invalid")


def test_money_wallets_add():
    m1 = MoneyR(1)
    m = m1 + 10
    assert str(m) == "MoneyR: 11"


def test_money_wallets_sub():
    m1 = MoneyR(1)
    m2 = MoneyD(2)
    m = m1 + 9
    assert str(m) == "MoneyR: 10"
    m = m - 5
    assert str(m) == "MoneyR: 5"
    with pytest.raises(TypeError):
        m1 + m2
