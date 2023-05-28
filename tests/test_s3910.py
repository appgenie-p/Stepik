import pytest
from s3910_copy import Matrix


@pytest.fixture
def matrix():
    return Matrix(2, 3, 0)


def test_matrix_init(matrix):
    assert matrix.rows == 2
    assert matrix.cols == 3
    assert matrix.matrix == [[0, 0, 0], [0, 0, 0]]


def test_matrix_init_with_list():
    matrix = Matrix([[1, 2, 3], [4, 5, 6]])
    assert matrix.rows == 2
    assert matrix.cols == 3
    assert matrix.matrix == [[1, 2, 3], [4, 5, 6]]


def test_matrix_init_with_invalid_list():
    with pytest.raises(TypeError):
        Matrix([[1, 2, 3], [4, 5]])


def test_matrix_getitem(matrix):
    assert matrix[0, 0] == 0
    assert matrix[1, 2] == 0


def test_matrix_setitem(matrix):
    matrix[0, 0] = 1
    matrix[1, 2] = 2
    assert matrix.matrix == [[1, 0, 0], [0, 0, 2]]


def test_matrix_add(matrix):
    result = matrix + 1
    assert result.matrix == [[1, 1, 1], [1, 1, 1]]

    other = Matrix(2, 3, 1)
    result = matrix + other
    assert result.matrix == [[1, 1, 1], [1, 1, 1]]

    with pytest.raises(ValueError):
        matrix + Matrix(3, 2, 1)


def test_matrix_sub(matrix):
    result = matrix - 1
    assert result.matrix == [[-1, -1, -1], [-1, -1, -1]]

    other = Matrix(2, 3, 1)
    result = matrix - other
    assert result.matrix == [[-1, -1, -1], [-1, -1, -1]]

    with pytest.raises(ValueError):
        matrix - Matrix(3, 2, 1)


def test_matrix_repr(matrix):
    assert repr(matrix) == '[[0, 0, 0], [0, 0, 0]]'
