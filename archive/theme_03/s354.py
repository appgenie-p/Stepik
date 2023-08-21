from typing import Union


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a: int, b: int, c: int):
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def __check_dimension(cls, value: int):
        return Dimensions.MIN_DIMENSION <= value <= Dimensions.MAX_DIMENSION

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, value: int) -> None:
        self.__a = value if self.__check_dimension(value) else self.__a

    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, value: int) -> None:
        self.__b = value if self.__check_dimension(value) else self.__b

    @property
    def c(self) -> int:
        return self.__c

    @c.setter
    def c(self, value: int) -> None:
        self.__c = value if self.__check_dimension(value) else self.__c

    def __volume(self) -> int:
        return self.a * self.b * self.c

    def __ge__(self, other: "Dimensions") -> bool:
        return self.__volume() >= other.__volume()

    def __gt__(self, other: "Dimensions") -> bool:
        return self.__volume() > other.__volume()


class ShopItem:
    Digit = Union[int, float]

    def __init__(self, name: str, price: Digit, dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim

    def __repr__(self) -> str:
        return f"name: {self.name} vol: {self.dim.c}"


trainers = ShopItem("кеды", 1024, Dimensions(40, 30, 120))
umbrella = ShopItem("зонт", 500.24, Dimensions(10, 20, 50))
fridge = ShopItem("холодильник", 40000, Dimensions(2000, 600, 500))
chair = ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))

lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)


assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

lst_sp = []
lst_sp.append(ShopItem("кеды", 1024, Dimensions(40, 30, 120)))
lst_sp.append(ShopItem("зонт", 500.24, Dimensions(10, 20, 50)))
lst_sp.append(ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)))
lst_sp.append(ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200)))

lst_sp_sorted = ["зонт", "кеды", "табуретка", "холодильник"]
s = [x.name for x in lst_shop_sorted]
assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)
assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10
assert (
    d2 < d1
), "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"
