from typing import List


class FloatValue:
    def __set_name__(self, obj, name):
        self.name = "_" + name

    def __get__(self, obj, type=None):
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if not isinstance(val, float):
            raise TypeError(
                "Присваивать можно только вещественный типданных.")
        setattr(obj, self.name, val)


class Cell:
    value = FloatValue()

    def __init__(self, val: float = 0.0) -> None:
        self.value = val

    def __repr__(self) -> str:
        return f'{self.value}'


class TableSheet:
    def __init__(self, n, m) -> None:
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]


table = TableSheet(5, 3)
inc = float(1)
for i in table.cells:
    for j in i:
        j.value = inc
        inc += 1

print(
    table.cells[0][0].value
)

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

