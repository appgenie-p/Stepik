import pytest

from s528 import Rect


def test_rect_creation():
    assert Rect(5, 4, 5, 4)


def test_rect_creation_error_with_negative_values():
    with pytest.raises(ValueError):
        Rect(5, 4, -5, 4)


def test_rect_is_collision():
    rect_a = Rect(0, 0, 5, 3)
    rect_b = Rect(6, 0, 3, 5)
    rect_c = Rect(3, 2, 4, 4)
    rect_d = Rect(0, 8, 8, 1)
    assert rect_a.is_collision(rect_b)
