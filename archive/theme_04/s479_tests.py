import pytest

from s479 import Function, Linear


def test_linear_create():
    f = Linear(1, 0.5)


@pytest.fixture
def f():
    return Linear(1, 0.5)


def test_linear_add(f):
    f2 = f + 10  # изменение смещения (атрибут _bias)
    assert f2._bias == 10


def test_linear_call(f):
    assert f(0) == 0.5


def test_linear_call2(f):
    f2 = f + 10  # изменение смещения (атрибут _bias)
    assert f2(0) == 10.5


def test_linear_mul(f):
    f2 = f * 5  # изменение амплитуды (атрибут _amplitude)
    assert f(0) == 0.5
    assert f2(0) == 2.5
