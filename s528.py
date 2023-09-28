from typing import Union

Number = Union[int, float]


class Rect:
    def __init__(self, x: Number, y: Number, width: Number, height: Number):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
