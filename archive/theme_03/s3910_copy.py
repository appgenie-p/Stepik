import operator
from typing import List, Tuple, Union
from functools import singledispatchmethod

Value = Union[int, float]


class Matrix:
    def __init__(self, *args) -> None:
        self.matrix = None
        self.rows = None
        self.cols = None
        self.initialize(*args)

    @singledispatchmethod
    def initialize(self, *args):
        raise TypeError('ожидается 1 или 3 аргумента')

    @initialize.register
    def _(self, arg: list):
        cols_number = len(arg[0])
        for row in arg:
            if len(row) != cols_number:
                raise TypeError(
                    'список должен быть прямоугольным, состоящим из чисел'
                )
            for item in row:
                self.check_value(item)
        self.matrix = arg
        self.rows = len(arg)
        self.cols = cols_number

    @initialize.register
    def _(self, rows: int, cols: int, fill_value: Union[int, float]):
        self.check_value(fill_value)
        self.matrix = [[fill_value] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def check_value(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError('элементы матрицы должны быть числами')

    def __getitem__(self, item: Tuple[int, int]) -> Value:
        row, col = item
        return self.matrix[row][col]

    def __setitem__(self, key: Tuple[int, int], value: Value) -> None:
        self.check_value(value)
        row, col = key
        self.matrix[row][col] = value

    def __get_other_value(
        self, other: Union['Matrix', Value]
    ) -> Tuple[str, Union[Value, List[List[Value]]]]:
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('размеры матриц должны быть одинаковыми')
            return 'matrix', other.matrix
        elif isinstance(other, (int, float)):
            return 'number', other
        raise TypeError('допустимы только матрицы и числа')

    def matrix_construct(self, operation, value_type, other_value):
        do = getattr(operator, operation)
        return Matrix(
            [
                [
                    do(self.matrix[row][col], other_value[row][col])
                    if value_type == 'matrix'
                    else do(self.matrix[row][col], other_value)
                    for col in range(self.cols)
                ]
                for row in range(self.rows)
            ]
        )

    def __add__(self, other: Union['Matrix', Value]) -> 'Matrix':
        value_type, other_value = self.__get_other_value(other)
        return self.matrix_construct('__add__', value_type, other_value)

    def __sub__(self, other: Union['Matrix', Value]) -> 'Matrix':
        value_type, other_value = self.__get_other_value(other)
        return self.matrix_construct('__sub__', value_type, other_value)

    def __repr__(self) -> str:
        return str(self.matrix)


a = Matrix(2, 3, 0)
