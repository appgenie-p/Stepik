from typing import Union


class Rect:
    Digits = Union[int, float]

    def __init__(self, x: Digits, y: Digits, width: Digits, height: Digits):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.width, self.height))


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)  # h1 == h2

assert h1 == h2, "хэши не совпадают"
