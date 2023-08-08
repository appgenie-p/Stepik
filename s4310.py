from typing import Union

Number = Union[int, float]


class ItemAttrs:
    def __getitem__(self, index: int) -> Number:
        return self.__dict__[list(self.__dict__.keys())[index]]

    def __setitem__(self, index: int, value: Number) -> None:
        self.__dict__[list(self.__dict__.keys())[index]] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y
