import sys
from typing import Union


class ShopItem:
    Number = Union[int, float]

    def __init__(self, name: str, weight: Number, price: Number) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, comparable) -> bool:
        return hash(self) == hash(comparable)

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.weight, self.price))

    def __repr__(self):
        return f"Object: {self.name}"


lst_in = list(map(str.strip, sys.stdin.readlines()))

# lst_in = [
#     "Системный блок: 1500 75890.56",
#     "Монитор Samsung: 2000 34000",
#     "Клавиатура: 200.44 545",
#     "Монитор Samsung: 2000 34000"
# ]

shop_items: dict = {}

for string in lst_in:
    string_dev = string.split(":")
    name = string_dev[0]
    weight, price = string_dev[1].strip().split()
    item = ShopItem(name, float(weight), float(price))
    if item in shop_items:
        shop_items[item][1] += 1
    else:
        shop_items[item] = [item, 1]


it1 = ShopItem("name", 10, 11)
it2 = ShopItem("name", 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem("name", 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem("name", 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem("NAME", 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(":")
for sp in shop_items.values():
    assert (
        isinstance(sp[0], ShopItem) and type(sp[1]) == int
    ), "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    assert (
        v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3
    ), "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert (
        v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3
    ), "неверные значения в словаре shop_items"
