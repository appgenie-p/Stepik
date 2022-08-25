
import time

import pytest

from archive.s3111 import Aragon, Calcium, GeyserClassic, Mechanical


@pytest.fixture
def create_filters():
    return (
        Mechanical(time.time()),
        Aragon(time.time()),
        Calcium(time.time()),
    )


def test_water_on_true(create_filters):
    g = GeyserClassic()
    for indx, _ in g.slots.items():
        g.add_filter(indx, create_filters[indx-1])
    assert g.water_on() is True


def test_water_on_false(create_filters):
    g = GeyserClassic()
    g.add_filter(1, Mechanical(time.time()))
    g.add_filter(2, Aragon(time.time()))
    assert g.water_on() is False


def test_filter_add_wrong():
    g = GeyserClassic()
    filter = Aragon(time.time())
    g.add_filter(1, filter)
    assert g.slots[1] is None


def test_filter_add():
    g = GeyserClassic()
    filter = Mechanical(time.time())
    g.add_filter(1, filter)
    assert g.slots[1] == filter
