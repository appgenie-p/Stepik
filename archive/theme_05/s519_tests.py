import pytest

from s519 import Triangle, main


def test_triangle_args_positive_numbers():
    t = Triangle(1, 2, 3)
    assert t._a == 1
    assert t._b == 2
    assert t._c == 3


def test_triangle_args_negative_numbers():
    with pytest.raises(TypeError):
        assert Triangle(-1, 2, 3)


def test_triangle_args_str():
    with pytest.raises(TypeError):
        assert Triangle(1, "str", 3)


def test_triangle_args_set_negative():
    t = Triangle(1, 2, 3)
    with pytest.raises(TypeError):
        t._a = -1


def test_input_data_triangle_creation():
    input_data = [
        (1.0, 4.54, 3),
        ("abc", 1, 2, 3),
        (-3, 3, 5.2),
        (4.2, 5.7, 8.7),
        (True, 3, 5),
        (7, 4, 6),
    ]
    assert len(main()) == 2
