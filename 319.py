# import pytest


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c) -> None:
        self.__a = self.__b = self.__c = 0
        self.a, self.b, self.c = a, b, c

    @property
    def a(self):
        return self.__a

    @classmethod
    def checker(cls, num):
        return (cls.MIN_DIMENSION <= num <= cls.MAX_DIMENSION
                and type(num) in (int, float))

    @a.setter
    def a(self, val):
        if self.checker(val):
            self.__a = val

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, val):
        if self.checker(val):
            self.__b = val

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        if self.checker(val):
            self.__c = val

    def __setattr__(self, __name, __value) -> None:
        prohibited_names = ('MIN_DIMENSION', 'MAX_DIMENSION')
        if __name in prohibited_names:
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено."
            )
        super().__setattr__(__name, __value)


d = Dimensions(10.5, 20.1, 30)
d.a = 10
d.b = 20
d.b = 30

a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30