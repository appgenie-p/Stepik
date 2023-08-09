from abc import abstractmethod
from typing import Union


class ShopInterface:
    @abstractmethod
    def get_id(self) -> int:
        raise NotImplementedError('в классе не переопределен метод get_id')


PositiveNumber = Union[int, float]


class ShopItem(ShopInterface):
    def __init__(
        self, name: str, weight: PositiveNumber, price: PositiveNumber
    ) -> None:
        self._name = name
        self._weight = weight
        self._price = price
        self._id = id(self)

    def get_id(self) -> int:
        return self._id
