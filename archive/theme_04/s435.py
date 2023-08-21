from numbers import Number
from typing import Generator, List


class SellItem:
    def __init__(self, name: str, price: Number) -> None:
        self.name = name
        self.price = price


class Flat(SellItem):
    def __init__(self, name: str, price: Number, size: Number, rooms: int) -> None:
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class House(SellItem):
    def __init__(self, name: str, price: Number, material: str, square: Number) -> None:
        super().__init__(name, price)
        self.material = material
        self.square = square


class Land(SellItem):
    def __init__(self, name: str, price: Number, square: Number) -> None:
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name: str) -> None:
        self.name = name
        self._objects: List[SellItem] = []

    def add_object(self, item: SellItem) -> None:
        self._objects.append(item)

    def remove_object(self, item: SellItem) -> None:
        self._objects.remove(item)

    def get_objects(self) -> Generator[SellItem, None, None]:
        yield from self._objects
