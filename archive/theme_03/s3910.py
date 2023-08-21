import operator
from typing import List, Tuple, Union

Value = Union[int, float]


class Matrix:
    def __init__(self, *args: Union[Tuple[int, int, Value], List[List[Value]]]) -> None:
        if len(args) == 3:
            self.rows, self.cols, fill_value = args
            self.check_value(fill_value)
            self.matrix = [[fill_value] * self.cols for _ in range(self.rows)]
        elif len(args) == 1:
            list_arg = args[0]
            cols_number = len(list_arg[0])
            for row in list_arg:
                if len(row) != cols_number:
                    raise TypeError(
                        "список должен быть прямоугольным, состоящим из чисел"
                    )
                for item in row:
                    self.check_value(item)
            self.matrix = list_arg
            self.rows = len(list_arg)
            self.cols = cols_number
        else:
            raise TypeError("ожидается 1 или 3 аргумента")

    @staticmethod
    def check_value(value: Value) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(
                "аргументы rows, cols - целые числа; fill_value - " "произвольное число"
            )

    def __getitem__(self, item: Tuple[int, int]) -> Value:
        row, col = item
        return self.matrix[row][col]

    def __setitem__(self, key: Tuple[int, int], value: Value) -> None:
        self.check_value(value)
        row, col = key
        self.matrix[row][col] = value

    def __get_other_value(
        self, other: Union["Matrix", Value]
    ) -> Tuple[str, Union[Value, List[List[Value]]]]:
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("размеры матриц должны быть одинаковыми")
            return "matrix", other.matrix
        elif isinstance(other, (int, float)):
            return "number", other
        raise TypeError("допустимы только матрицы и числа")

    def matrix_construct(self, operation, value_type, other_value):
        do = getattr(operator, operation)
        return Matrix(
            [
                [
                    do(self.matrix[row][col], other_value[row][col])
                    if value_type == "matrix"
                    else do(self.matrix[row][col], other_value)
                    for col in range(self.cols)
                ]
                for row in range(self.rows)
            ]
        )

    def __add__(self, other: Union["Matrix", Value]) -> "Matrix":
        value_type, other_value = self.__get_other_value(other)
        return self.matrix_construct("__add__", value_type, other_value)

    def __sub__(self, other: Union["Matrix", Value]) -> "Matrix":
        value_type, other_value = self.__get_other_value(other)
        return self.matrix_construct("__sub__", value_type, other_value)

    def __repr__(self) -> str:
        return str(self.matrix)
