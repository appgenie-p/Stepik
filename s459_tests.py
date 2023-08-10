import pytest

from s459 import PointTrack, Track

# tr = Track(start_x, start_y)
# tr = Track(pt1, pt2, ..., ptN)


def test_track_class_instantiation_start_point():
    tr = Track(5, 6)
    assert tr.start_x == 5
    assert tr.start_y == 6


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


def test_track_class_instantiation_points():
    first_obj = PointTrack(4, 5)
    tr = Track(first_obj, PointTrack(6.5, 7), PointTrack(8.3, 9.1))
    assert tr.points[0] == first_obj
