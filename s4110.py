from operator import add, sub
from typing import Callable, Tuple, Union

Number = Union[int, float]
Operator = Callable[[Number, Number], Number]


class Vector:
    def __init__(self, *args: Number) -> None:
        self.coords: Tuple[Number] = args

    def get_coords(self) -> Tuple[Number]:
        return self.coords

    def __add__(self, other: "Vector") -> "Vector":
        return self.add_sub_vector(other, add)

    def __sub__(self, other: "Vector") -> "Vector":
        return self.add_sub_vector(other, sub)

    def add_sub_vector(self, other: "Vector", operator: Operator) -> "Vector":
        self.len_check(other)
        coords = self.get_total_coords(other, operator)
        try:
            return self.__class__(*coords)
        except TypeError:
            return Vector(*coords)

    def len_check(self, other: "Vector") -> None:
        if len(self.coords) != len(other.coords):
            raise TypeError("размерности векторов не совпадают")

    def get_total_coords(
        self, other: "Vector", operator: Operator
    ) -> Tuple[Number]:
        return tuple(operator(x, y) for x, y in zip(self.coords, other.coords))


class VectorInt(Vector):
    def __init__(self, *args: Number) -> None:
        if any(not isinstance(x, int) for x in args):
            raise ValueError("координаты должны быть целыми числами")
        super().__init__(*args)