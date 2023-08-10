from typing import Any, Union, cast

Number = Union[int, float]


class Track:
    def __init__(self, *args: Union[Number, "PointTrack"]) -> None:
        self.__points: list["PointTrack"] = []

        if isinstance(args[0], (int, float)):
            self.__points.append(PointTrack(args[0], args[1]))
        elif all(isinstance(arg, PointTrack) for arg in args):
            self.__points.append(cast(PointTrack, args))

    @property
    def points(self) -> tuple["PointTrack"]:
        return tuple(self.__points)


class PointTrack:
    def __init__(self, x: Any, y: Any) -> None:
        if not all(isinstance(arg, (int, float)) for arg in (x, y)):
            raise TypeError("координаты должны быть числами")
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"PointTrack: {self.x}, {self.y}"
