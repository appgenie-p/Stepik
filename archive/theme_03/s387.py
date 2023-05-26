import reprlib
from typing import Any, List, Tuple, Union


class RadiusVector:
    __slots__ = ("coords",)

    def __init__(self, *args: Any) -> None:
        # Initialize the RadiusVector object with a list of coordinates
        self.coords: List[Any] = list(args)

    def __repr__(self) -> str:
        # Return a string representation of the coordinates using reprlib
        return reprlib.repr(self.coords)

    def __getitem__(self, index: Union[int, slice]) -> Union[Any, Tuple[Any]]:
        # Return the coordinate at the given index or a tuple of coordinates
        # for a slice
        if isinstance(index, slice):
            return tuple(self.coords[index])

        return self.coords[index]

    def __setitem__(self, index: int, value: Any) -> None:
        # Set the coordinate at the given index to the given value
        self.coords[index] = value


v = RadiusVector(1, 1, 1, 1)
print(v[1])  # 1
v[:] = 1, 2, 3, 4
print(v[2])  # 3
print(v[1:])  # (2, 3, 4)
v[0] = 10.5
