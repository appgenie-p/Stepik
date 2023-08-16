from typing import Any, List, Tuple, Union, cast

Number = Union[int, float]


class Track:
    def __init__(self, *args: Union[Number, "PointTrack"]) -> None:
        self.__points: List["PointTrack"] = []

        if isinstance(args[0], (int, float)):
            self.__points.append(PointTrack(args[0], args[1]))
        elif all(isinstance(arg, PointTrack) for arg in args):
            self.__points.extend([cast(PointTrack, arg) for arg in args])

    @property
    def points(self) -> Tuple["PointTrack"]:
        return tuple(self.__points)

    def add_back(self, pt: "PointTrack") -> None:
        self.__points.append(pt)

    def add_front(self, pt: "PointTrack") -> None:
        self.__points.insert(0, pt)

    def pop_back(self) -> "PointTrack":
        return self.__points.pop()

    def pop_front(self) -> "PointTrack":
        return self.__points.pop(0)


class PointTrack:
    def __init__(self, x: Any, y: Any) -> None:
        self.validate_args(x, y)
        self.x = x
        self.y = y

    def validate_args(self, x: Any, y: Any):
        if not all(isinstance(arg, (int, float)) for arg in (x, y)):
            raise TypeError("координаты должны быть числами")

    def __str__(self) -> str:
        return f"PointTrack: {self.x}, {self.y}"
