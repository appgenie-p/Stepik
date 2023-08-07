import pytest

from s446 import Furniture


def test_furniture():
    f = Furniture("Chair", 100.5)
    assert f._name == "Chair"
    assert f._weight == 100.5


def test_method__verify_name():
    with pytest.raises(TypeError):
        Furniture(456, 100)


def test_method__verify_weight():
    with pytest.raises(TypeError):
        f = Furniture("Chair", "100")
    f = Furniture("Chair", 100)
    with pytest.raises(TypeError):
        f._name = 456
