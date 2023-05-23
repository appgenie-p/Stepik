import numbers
from typing import Any, Type


class Number:
    def __init__(self, start_value=0):
        self.value = start_value
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, self.TYPE):
            raise ValueError(self.ERROR)
        self.__value = new_value

    def __str__(self):
        return str(self.value)


class Integer(Number):
    TYPE = numbers.Integral
    ERROR = 'должно быть целое число'


# ar = Array(max_length, cell)
class Array:
    def __init__(self, max_length: int, cell: Type[Any]):
        self.cell = cell
        self.array = [cell() for _ in range(max_length)]

    def _index_check(self, index):
        if index >= len(self.array):
            raise IndexError('некорректный индекс')

    def __getitem__(self, index: int) -> Integer:
        self._index_check(index)
        return self.array[index].value

    def __setitem__(self, index: int, value: Any):
        self._index_check(index)
        self.array[index].value = value

    def __repr__(self):
        return ' '.join([str(i) for i in self.array])

