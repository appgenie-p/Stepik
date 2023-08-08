import pytest

from s449 import Vector, vector_log


def test_decorator():
    v = Vector(1, 2, 3)
    v[0] = 4
    assert vector_log == ['__init__', '__setitem__']
