from typing import Union


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.__x: float = 0
        self.__y: float = 0
        self.x: float = x
        self.y: float = y

    @classmethod
    def check(cls, num: Union[int, float]) -> bool:
        return (
            isinstance(num, float)
            or isinstance(num, int)
            and cls.MIN_COORD <= num <= cls.MAX_COORD
        )

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float) -> None:
        if self.check(x):
            self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float) -> None:
        if self.check(y):
            self.__y = y

    @staticmethod
    def norm2(vector: "RadiusVector2D") -> float:
        return vector.x**2 + vector.y**2


r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)

assert hasattr(RadiusVector2D, "MIN_COORD") and hasattr(
    RadiusVector2D, "MAX_COORD"
), "в классе RadiusVector2D должны присутствовать атрибуты MIN_COORD и MAX_COORD"

assert (
    type(RadiusVector2D.x) == property and type(RadiusVector2D.y) == property
), "в классе RadiusVector2D должны присутствовать объекты-свойства x и y"

assert (
    r1.x == 0 and r1.y == 0 and r2.x == 1 and r2.y == 0 and r3.x == 4 and r3.y == 5
), "свойства x и y возвращают неверные значения"

assert RadiusVector2D.norm2(r3) == 41, "неверно вычисляется норма вектора"

r4 = RadiusVector2D(4.5, 5.5)
assert (
    4.4 < r4.x < 4.6 and 5.4 < r4.y < 5.6
), "свойства x и y возвращают неверные значения"

r5 = RadiusVector2D(-102, 2000)
assert (
    r5.x == 0 and r5.y == 0
), "присвоение значений, выходящих за диапазон [-100; 1024] не должно выполняться"

r = RadiusVector2D(10, 20)
r.x = "a"
r.y = (1, 2)
assert r.x == 10 and r.y == 20, "присвоение не числовых значений должно игнорироваться"
