from s4310 import ItemAttrs, Point


def test_itemattrs_class():
    pt = Point(1, 2.5)
    assert pt[0] == 1
    assert pt[1] == 2.5
    pt[0] = 10
    assert pt[0] == 10


def test_itemattrs():
    pt = ItemAttrs(1, 2.5)
    assert pt[0] == 1
