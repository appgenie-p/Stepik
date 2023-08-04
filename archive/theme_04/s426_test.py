# BEGIN: 6f9d1b2e4c5a
from s426 import Tuple


def test_tuple_addition():
    t1 = Tuple((1, 2, 3))
    t2 = Tuple((4, 5, 6))
    t3 = t1 + t2
    assert t3 == (1, 2, 3, 4, 5, 6)

    t4 = t1 + [4, 5, 6]
    assert t4 == (1, 2, 3, 4, 5, 6)

    t5 = t1 + (4, 5, 6)
    assert t5 == (1, 2, 3, 4, 5, 6)

    t6 = t1 + range(4, 7)
    assert t6 == (1, 2, 3, 4, 5, 6)


def test_tuple_addition_1():
    t = Tuple([1, 2, 3])
    t = t + "Python"
    t = t + "P"
    assert t == (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n', 'P')
    assert type(t) == Tuple
    t = (t + "Python") + "ООП"
    assert type(t) == Tuple


def test_tuple_addition_2():
    t = Tuple([1, 2])
    assert t == (1, 2)
