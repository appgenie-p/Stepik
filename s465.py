from typing import Iterable, List, Optional


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self) -> str:
        return create_str_repr_output(self, "")


class ShopUserView:
    def __repr__(self) -> str:
        return create_str_repr_output(self, ["_id"])


def create_str_repr_output(
    object: object, attrs_exclude: Iterable[str]
) -> str:
    res = ""
    for attr, value in vars(object).items():
        if attr not in attrs_exclude:
            res += f"{attr}: {value}\n"
    return res


class Book(ShopItem):
    def __init__(self, title: str, author: str, year: int):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year
