import numbers
from typing import Type


class IntegerValue:
    """Data descriptor"""

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("возможны только целочисленные значения")
        setattr(instance, self.name, value)


class CellInteger:
    __slots__ = ("_value",)

    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

    def __str__(self):
        return str(self.value)


class TableValues:
    __slots__ = ("rows", "cols", "cells")

    def __new__(cls, *args, **kwargs):
        if "cell" not in kwargs:
            raise ValueError("параметр cell не указан")
        return super().__new__(cls)

    def __init__(self, rows: int, cols: int, cell: Type[CellInteger]):
        self.rows = rows
        self.cols = cols
        self.cells = [[cell() for _ in range(cols)] for _ in range(rows)]

    def _check_index(self, raw, col):
        if raw >= self.rows or col >= self.cols:
            raise IndexError("некорректный индекс")

    def __getitem__(self, index):
        raw, col = index
        self._check_index(raw, col)
        return self.cells[raw][col].value

    def __setitem__(self, index, value):
        raw, col = index
        self._check_index(raw, col)
        self.cells[raw][col].value = value

    def __repr__(self):
        return " ".join([str(i) for i in self.cells])


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45  # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=" ")
    print()
