import pytest

from s437 import Vector


def test_vector_init():
    v = Vector(1, 2, 3)
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3


def test_vector_set_coords():
    v = Vector(1, 2, 3)
    v.set_coords(4, 5, 6)
    assert v[0] == 4
    assert v[1] == 5
    assert v[2] == 6


def test_vector_set_coords_reverse():
    v = Vector(1, 2, 3)
    v.set_coords(4, 5, 6, reverse=True)
    assert v[0] == 6
    assert v[1] == 5
    assert v[2] == 4


def test_vector_setitem():
    v = Vector(1, 2, 3)
    v[0] = 4
    assert v[0] == 4


def test_vector_integer_params():
    v = Vector(1)
    with pytest.raises(TypeError):
        v[0] = 30.5
