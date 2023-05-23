import itertools
import numbers
from typing import Union


Tr = Union[int, float]


##########################################
# Descriptor class used as a data descriptor.
##########################################
class Descriptor:
    def __set_name__(self, owner, name) -> None:
        self.name = '_' + name

    def __set__(self, instance, value: Tr) -> None:
        '''sets the value to instance and perform value validation'''
        if not isinstance(value, numbers.Integral):
            raise TypeError("Value should be a number.")
        if value < 0:
            raise ValueError("Value should be positive.")
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        '''returns the value of the instance.'''
        return getattr(instance, self.name)


###############################################
# Triangle Class - encapsulates Descrptor object
###############################################
class Triangle:
    '''Triangle class as a shape with three sides/edges.'''
    __slots__ = ('_a', '_b', '_c')

    # each side is a descriptor type so before setting value through assigned
    # variable their values validation is checked through descriptors.
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a: Tr, b: Tr, c: Tr):
        '''
        Initialize triangle with its edges with proper checks.
        :param a: First edge of the triangle.
        :param b: Second edge of the triangle.
        :param c: Third edge of the triangle.
        '''
        # permutes all three edges and compare if they can form a valid
        # triangle
        self.check_triangle(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def check_triangle(a: Tr, b: Tr, c: Tr) -> bool:
        '''
        Check if the provided edges can form a valid triangle.
        :param a: First edge of the triangle.
        :param b: Second edge of the triangle.
        :param c: Third edge of the triangle.
        '''
        for x, y, z in itertools.permutations((a, b, c), 3):
            if x >= y + z:
                raise ValueError(
                    "Provided edges cannot form a valid triangle."
                )
        return True

    def __len__(self) -> int:
        '''Returns Perimeter of the triangle.'''
        return int(self.a + self.b + self.c)

    def __call__(self) -> float:
        '''Calculates and returns Area of the triangle using Heron's
        formula.'''
        p = len(self) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


tr = Triangle(5, 4, 3)
assert (
    tr.a == 5 and tr.b == 4 and tr.c == 3
), "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
