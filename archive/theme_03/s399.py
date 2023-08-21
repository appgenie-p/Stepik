from typing import Any


class Cell:
    __slots__ = ("__data",)

    def __init__(self, data: Any) -> None:
        self.data: Any = data

    @property
    def data(self) -> Any:
        return self.__data

    @data.setter
    def data(self, data: Any) -> None:
        self.__data = data

    def __repr__(self) -> str:
        return f"Cell({self.data})"


class TableValues:
    __slots__ = ("table", "type_data")

    def __init__(self, rows: int, cols: int, type_data: Any = int) -> None:
        self.type_data: Any = type_data
        self.table = tuple(tuple(Cell(0) for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, index: tuple) -> Any:
        row, col = index
        return self.table[row][col].data

    def __setitem__(self, index: tuple, data: Any) -> None:
        if type(data) != self.type_data:
            raise TypeError("неверный тип присваиваемых данных")
        row, col = index
        self.table[row][col].data = data

    def __iter__(self):
        return ((item.data for item in row) for row in self.table)


cell = Cell("a")

print(
    list(cell.data),
    (cell.data),
)

# tb = TableValues(3, 2)
# n = m = 0
# for row in tb:
#     n += 1
#     for value in row:
#         m += 1
#         assert (
#             type(value) == int and value == 0
#         ), "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

# assert (
#     n > 1 and m > 1
# ), "неверно отработали вложенные циклы для перебора ячеек таблицы"


# tb[0, 0] = 10
# assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"


# try:
#     tb[2, 0] = 5.2
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError"
