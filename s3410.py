from typing import Tuple

import pytest


class MaxPooling:
    def __init__(
        self, step: Tuple[int, int] = (2, 2), size: Tuple[int, int] = (2, 2)
    ):
        """
        step - шаг смещения окна по горизонтали и вертикали;
        size - размер окна по горизонтали и вертикали.
        """
        self.step = step
        self.size = size

    # res = mp(matrix)
    def __call__(self, matrix: list[list[int]]) -> list[list[int]]:
        # Check that all nested lists are equal size and all members are
        # digits.
        self._check_matrix(matrix)
        # Get first square of size self.size from matrix and find max vlaue,
        # add max value to result list.
        res = []
        step_right = self.step[0]
        step_down = self.step[1]
        for list in range(0, len(matrix), step_right):
            res.append([])
            list_len = matrix[0]
            for list_member in range(0, len(list_len), step_down):
                res[-1].append(
                    self._get_max_value(
                        matrix, list, list_member, self.size[0], self.size[1]
                    )
                )

    @classmethod
    def _check_matrix(self, matrix):
        list_size = len(matrix[0])
        for list in matrix:
            if len(list) != list_size or not self._check_symbols(list):
                raise ValueError(
                    "Неверный формат для первого параметра matrix."
                )

    @staticmethod
    def _check_symbols(list):
        return all(isinstance(symbol, int) for symbol in list)


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
