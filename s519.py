from typing import Any, Generic, List, Type, TypeVar

T = TypeVar("T")


class PositiveNum(Generic[T]):
    def __set_name__(self, owner: Type[T], name: str) -> None:
        self.name = name

    def __set__(self, obj: T, value: Any) -> None:
        if isinstance(value, bool):
            raise TypeError("Value must not be a boolean")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise TypeError("Value must be positive")
        obj.__dict__[self.name] = value

    def __get__(self, obj: T, objtype: Type[T]) -> float:
        return obj.__dict__[self.name]


class Triangle:
    _a = PositiveNum()
    _b = PositiveNum()
    _c = PositiveNum()

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._check_triangle()

    def _check_triangle(self) -> bool:
        a, b, c = sorted((self._a, self._b, self._c))
        if a + b <= c:
            raise ValueError("Provided edges cannot form a valid triangle.")
        return True


def main() -> List[Triangle]:
    input_data = [
        (1.0, 4.54, 3),
        ("abc", 1, 2, 3),
        (-3, 3, 5.2),
        (4.2, 5.7, 8.7),
        (True, 3, 5),
        (7, 4, 6),
    ]
    result = []
    for entry in input_data:
        try:
            t = Triangle(*entry)
        except (TypeError, ValueError):
            continue
        else:
            result.append(t)
    return result


if __name__ == "__main__":
    lst_tr = main()
