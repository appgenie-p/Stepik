from typing import Union
import pytest
from s454 import ShopItem


PositiveNumber = Union[int, float]


@pytest.fixture
def shop_item():
    return ShopItem("apple", 0.5, 1.0)


def test_get_id(shop_item):
    assert isinstance(shop_item.get_id(), int)


def test_name(shop_item):
    assert shop_item._name == "apple"


def test_weight(shop_item):
    assert shop_item._weight == 0.5


def test_price(shop_item):
    assert shop_item._price == 1.0


def test_id_uniqueness():
    item1 = ShopItem("apple", 0.5, 1.0)
    item2 = ShopItem("banana", 0.3, 0.5)
    assert item1.get_id() != item2.get_id()
