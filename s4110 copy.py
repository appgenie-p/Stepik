# classDiagram

# class Vector{
#     +List~Number~ coords
#     +get_coords() Tuple~coords~

# }

# class VectorInt
# VectorInt --|> Vector

from operator import add, sub
from typing import Callable, Tuple, Type, Union

Number = Union[int, float]


class Vector:
    def __init__(self, *args: Number) -> None:
        self.coords: Tuple[Number] = args

    def get_coords(self) -> Tuple[Number]:
        return self.coords

    # implement vector addition
    def __add__(self, other: "Vector") -> "Vector":
        return self.add_sub_vector(other, add)

    # implement vector subtraction
    def __sub__(self, other: "Vector") -> "Vector":
        return self.add_sub_vector(other, sub)

    def add_sub_vector(
        self, other: "Vector", operator: Callable[[Number, Number], Number]
    ) -> "Vector":
        if len(self.coords) != len(other.coords):
            raise TypeError("размерности векторов не совпадают")

        constructor = self.constructor(other)

        return constructor(
            *[operator(x, y) for x, y in zip(self.coords, other.coords)]
        )

    def constructor(self, other: "Vector") -> Type["Vector"]:
        if self.__class__ == other.__class__:
            return self.__class__

        if all(isinstance(x, int) for x in self.coords) and all(
            isinstance(x, int) for x in other.coords
        ):
            return VectorInt
        return Vector


class VectorInt(Vector):
    def __init__(self, *args: Number) -> None:
        if any(not isinstance(x, int) for x in args):
            raise ValueError("координаты должны быть целыми числами")
        super().__init__(*args)
