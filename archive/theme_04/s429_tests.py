import pytest

from s429 import SmartPhone


@pytest.fixture
def smartphone() -> SmartPhone:
    return SmartPhone(model="iPhone 12", size=(1170, 2532), memory=128)


def test_smartphone(smartphone: SmartPhone) -> None:
    assert smartphone.model == "iPhone 12"
    assert smartphone.size == (1170, 2532)
    assert smartphone.memory == 128


def test_smartphone_is_iterable(smartphone: SmartPhone):
    for key, value in smartphone:
        assert key in ("model", "size", "memory")
        assert value in ("iPhone 12", (1170, 2532), 128)
