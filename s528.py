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
        if type(value) not in (int, float):
            raise ValueError(
                "некорректные координаты и параметры прямоугольника"
            )
        if key in ("_width", "_height"):
            _check_negative_value(value)
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


def _check_negative_value(value: Number) -> None:
    if value <= 0:
        raise ValueError("некорректные координаты и параметры прямоугольника")


def _get_uncrossed_rectangles(combinations: List[Tuple[Rect, Rect]]) -> List[Rect]:
    lst_not_collision: Set[Rect] = set()
    failed_members: Set[Rect] = set()
    for rect1, rect2 in combinations:
        try:
            rect1.is_collision(rect2)
        except TypeError:
            failed_members.add(rect1)
        else:
            lst_not_collision.add(rect1)
    lst_not_collision.difference_update(failed_members)
    return list(lst_not_collision)


cords_raw = """
0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1
"""

data_for_rects = [line.split("; ") for line in cords_raw.strip().splitlines()]

lst_rect = [Rect(*map(eval, cords)) for cords in data_for_rects]

all_combinations = list(itertools.combinations(lst_rect, 2))

lst_not_collision = _get_uncrossed_rectangles(all_combinations)
pass

if __name__ == "__main__":
    r = Rect(1, 2, 10, 20)
    assert (
        r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20
    ), "неверные значения атрибутов объекта класса Rect"

    r2 = Rect(1.0, 2, 10.5, 20)

    try:
        r2 = Rect(0, 2, 0, 20)
    except ValueError:
        assert True
    else:
        assert (
            False
        ), "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"

    assert len(data_for_rects) == 4, "список lst_rect содержит не 4 элемента"
    assert (
        len(lst_not_collision) == 1
    ), "неверное число элементов в списке lst_not_collision"

    def not_collision(rect):
        for x in data_for_rects:
            try:
                if x != rect:
                    rect.is_collision(x)
            except TypeError:
                return False
        return True

    f = list(filter(not_collision, lst_rect))
    assert (
        lst_not_collision == f
    ), "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

    r = Rect(3, 2, 2, 5)
    rr = Rect(1, 4, 6, 2)

    try:
        r.is_collision(rr)
    except TypeError:
        assert True
    else:
        assert (
            False
        ), "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
