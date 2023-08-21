# BEGIN: 5d8f4e1f8c5a
import pytest
from s424 import DictShop, Thing


def test_thing_hash():
    t1 = Thing("apple", 1.0, 0.5)
    t2 = Thing("apple", 1.0, 0.5)
    t3 = Thing("banana", 0.5, 0.3)
    assert hash(t1) == hash(t2)
    assert hash(t1) != hash(t3)


def test_dict_shop():
    th_1 = Thing("Лыжи", 11000, 1978.55)
    th_2 = Thing("Книга", 1500, 256)
    dict_things = DictShop()
    dict_things[th_1] = th_1
    dict_things[th_2] = th_2

    assert dict_things[th_1] == th_1
    assert dict_things[th_2] == th_2

    with pytest.raises(TypeError):
        dict_things[1] = th_1

    with pytest.raises(TypeError):
        dict_things["key"] = th_1

    # test DictShop is iterable
    for x in dict_things:
        assert x in dict_things
        assert dict_things[x] == x

    with pytest.raises(TypeError):
        DictShop({"th_1": th_1, "th_2": th_2})
