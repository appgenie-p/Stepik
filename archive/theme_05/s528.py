import itertools
from typing import Any, List, Set, Tuple, Union

Number = Union[int, float]


class Rect:
    def __init__(self, x: Number, y: Number, width: Number, height: Number):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key: Any, value: Any):
        _raise_err_if_value_is_not_int_or_float(value)
        if key in ("_width", "_height"):
            _raise_err_if_negative_value(value)
        super().__setattr__(key, value)

    def __repr__(self):
        return f"Rect({self._x}, {self._y}, {self._width}, {self._height})"

    def is_collision(self, rect: "Rect"):
        if (
            self._x < rect._x + rect._width
            and self._x + self._width > rect._x
            and (
                self._y < rect._y + rect._height
                and self._y + self._height > rect._y
            )
        ):
            raise TypeError("прямоугольники пересекаются")
        return False


def _raise_err_if_value_is_not_int_or_float(value: Any) -> None:
    if type(value) not in (int, float):
        raise ValueError("некорректные координаты и параметры прямоугольника")


def _raise_err_if_negative_value(value: Number) -> None:
    if value <= 0:
        raise ValueError("некорректные координаты и параметры прямоугольника")


def _get_crossed_rectangles(
    combinations: List[Tuple[Rect, Rect]]
) -> Set[Rect]:
    failed_members: Set[Rect] = set()
    for rect1, rect2 in combinations:
        try:
            rect1.is_collision(rect2)
        except TypeError:
            failed_members.update((rect1, rect2))
    return failed_members


if __name__ == "__main__":
    cords_raw = """
    0; 0; 5; 3
    6; 0; 3; 5
    3; 2; 4; 4
    0; 8; 8; 1
    """

    data_for_rects = [
        line.split("; ") for line in cords_raw.strip().splitlines()
    ]

    lst_rect = [Rect(*map(eval, cords)) for cords in data_for_rects]

    all_combinations = list(itertools.combinations(lst_rect, 2))

    lst_not_collision = list(
        set(lst_rect) - _get_crossed_rectangles(all_combinations)
    )
