from typing import Any, Tuple


class Cell:
    def __init__(self, value: Any = None) -> None:
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


class SparseTable:
    def __init__(self):
        self.table = {}

    @property
    def rows(self):
        return max(row for row, _ in self.table.keys()) + 1 if self.table else 0

    @property
    def cols(self):
        return max(cols for _, cols in self.table.keys()) + 1 if self.table else 0

    def add_data(self, row: int, col: int, data: Cell) -> None:
        self.table[(row, col)] = data

    def remove_data(self, row: int, col: int) -> None:
        if (row, col) not in self.table:
            raise IndexError("ячейка не существует")
        del self.table[row, col]

    def __getitem__(self, key: Tuple[int, int]) -> Cell:
        if key not in self.table:
            raise ValueError("ячейка не существует")
        return self.table[key].value

    def __setitem__(self, key: Tuple[int, int], value: Any) -> None:
        self.table[key] = Cell(value)

    def __delitem__(self, key: Tuple[int, int]) -> None:
        del self.table[key]


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert (
    st[3, 2] == 100
), "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell("5")
assert (
    d.value == "5"
), "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
