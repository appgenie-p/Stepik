import pytest

from s459 import PointTrack, Track


def test_pointtrack_class_instantiation():
    pt = PointTrack(5, 6)
    assert pt.x == 5
    assert pt.y == 6


def test_pointtrack_class_instantiation_error():
    with pytest.raises(TypeError):
        PointTrack("5", 6)


def test_pointtrack_class_str():
    pt = PointTrack(5, 6)
    assert str(pt) == "PointTrack: 5, 6"
