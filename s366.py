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
        return hash(self.name) + hash(self.weight) + hash(self.price)