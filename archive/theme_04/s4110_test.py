# BEGIN: 6f8d2b3c7e5a
import pytest
from s4110 import Vector, VectorInt


def test_vector_creation():
    v = Vector(1, 2, 3)
    assert v.get_coords() == (1, 2, 3)


def test_vector_creation_with_floats():
    v = Vector(1.0, 2.5, 3.7)
    assert v.get_coords() == (1.0, 2.5, 3.7)


def test_vector_creation_with_mixed_types():
    v = Vector(1, 2.5, 3)
    assert v.get_coords() == (1, 2.5, 3)


def test_vector_creation_with_single_argument():
    v = Vector(1)
    assert v.get_coords() == (1,)


def test_vector_creation_with_no_arguments():
    v = Vector()
    assert v.get_coords() == ()


# END: 6f8d2b3c7e5a
# BEGIN: 7d8f6a2d9b3c
def test_vector_addition():
    v1 = Vector(1, 2, 3)
    v2 = Vector(3, 4, 5)
    v3 = Vector(1, 2, 3, 4)
    assert (v1 + v2).get_coords() == (4, 6, 8)
    assert (v1 - v2).get_coords() == (-2, -2, -2)
    with pytest.raises(TypeError):
        v1 + v3


# END: 7d8f6a2d9b3c


def test_vector_int_only_accepts_integers():
    with pytest.raises(ValueError):
        VectorInt(1, 2, 3.5)


def test_vector_int_addition():
    v1 = VectorInt(1, 2, 3)
    v2 = VectorInt(4, 5, 6)
    assert (v1 + v2).get_coords() == (5, 7, 9)


def test_vector_int_subtraction():
    v1 = VectorInt(1, 2, 3)
    v2 = VectorInt(4, 5, 6)
    v = v1 + v2
    assert isinstance(v, VectorInt)


def test_vector_int_must_be_same_length():
    v1 = VectorInt(1, 2, 3)
    v2 = VectorInt(4, 5)
    with pytest.raises(TypeError):
        v1 + v2


def test_vector_and_vector_int_addition():
    v1 = Vector(1, 2, 3)
    v2 = VectorInt(4, 5, 6)
    v_int = v2 + v1
    assert isinstance(v_int, VectorInt)


def test_vector_and_vector_int_float_addition():
    v1 = Vector(1, 2, 3.3)
    v2 = VectorInt(4, 5, 6)
    v_int = v1 + v2
    assert isinstance(v_int, Vector)
