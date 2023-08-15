from typing import Any, Iterable


class ShopItem:
    id_shop_item = 0

    def __init__(self):
        ShopItem.id_shop_item += 1
        self._id = ShopItem.id_shop_item

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self) -> str:
        return create_str_repr_output(vars(self))


class ShopUserView:
    def __repr__(self) -> str:
        return create_str_repr_output(vars(self), attrs_exclude=["_id"])


def create_str_repr_output(
    attrs: dict[str, Any], attrs_exclude: Iterable[str] = ""
) -> str:
    res = ""
    for attr, value in vars(attrs).items():
        if attr not in attrs_exclude:
            res += f"{attr}: {value}\n"
    return res


class Book(ShopItem):
    def __init__(self, title: str, author: str, year: int):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year
