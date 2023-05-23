from typing import List, Tuple, Union

import pytest


class MaxPooling:
    Matrix = List[List[int]]
    Digit = Union[int, float]

    def __init__(
        self, step: Tuple[int, int] = (2, 2), size: Tuple[int, int] = (2, 2)
    ):
        self.step = step
        self.size = size

    @classmethod
    def _check_matrix(self, matrix: Matrix) -> None:
        list_size = len(matrix[0])
        if any(
            len(list) != list_size or not self._check_symbols(list)
            for list in matrix
        ):
            raise ValueError("Неверный формат для первого параметра matrix.")

    @staticmethod
    def _check_symbols(list: List[Digit]) -> bool:
        return all(isinstance(symbol, (int, float)) for symbol in list)

    def _get_submatrix_max_value(
        self, matrix: Matrix, x: int, y: int
    ) -> Digit:
        max_value = max(
            matrix[local_y][local_x]
            for local_y in range(y, y + self.size[1])
            for local_x in range(x, x + self.size[0])
        )
        return max_value

    # res = mp(matrix)
    def __call__(self, matrix: Matrix) -> Matrix:
        self._check_matrix(matrix)
        x_axis_step, y_axis_step = self.step
        x_axis_len = len(matrix[0])
        y_axis_len = len(matrix)
        x_axis_steps_count = x_axis_len // x_axis_step
        y_axis_steps_count = y_axis_len // y_axis_step

        # Get starting point for each submatrix and delegate max value
        # calculation to _get_submatrix_max_value method.
        res = []
        for y_count in range(y_axis_steps_count):
            res.append([])
            y = y_count * y_axis_step
            for x_count in range(x_axis_steps_count):
                x = x_count * x_axis_step
                res[y_count].append(
                    self._get_submatrix_max_value(matrix, x, y)
                )
        return res

    def __repr__(self):
        return f"MaxPooling(step={self.step}, size={self.size})"


mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [
    [12]
], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert (
        False
    ), "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert (
        False
    ), "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"


@pytest.fixture
def mp():
    return MaxPooling(step=(2, 2), size=(2, 2))


# test ValueError if all nested lists are not equal size.
def test_check_matrix(mp):
    with pytest.raises(ValueError):
        mp._check_matrix([[1, 2], [3, 4, 5], [6, 7, 8]])
    with pytest.raises(ValueError):
        mp([[1, 2], [3, 4, 5], [6, 7, 8]])


# If any symbol in matrix is not int, then raise ValueError.
def test_check_symbol(mp):
    with pytest.raises(ValueError):
        mp([[1, 2], ["3", 4], [6, 7]])


# Test MaxPooling.
def test_matrix_processing(mp):
    res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    assert res == [[6, 8], [9, 7]]


if __name__ == "__main__":
    pytest.main([__file__])
