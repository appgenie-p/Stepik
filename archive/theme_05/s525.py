from typing import Any


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self._x = x
        self._y = y

    def __eq__(self, other: Any):
        return self._x == other._x and self._y == other._y

    def __repr__(self):
        return f"Point: x = {self._x}, y = {self._y}"


def main():
    num1, num2 = input().split()
    return (
        Point(int(num1), int(num2))
        if all([_check_num(num1), _check_num(num2)])
        else Point()
    )


def _check_num(num: Any) -> bool:
    try:
        int(num)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    print(main())
