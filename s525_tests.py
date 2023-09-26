from _pytest.monkeypatch import MonkeyPatch

from s525 import Point, main


def test_create_empty_point_class():
    assert Point()


def test_create_point_class():
    assert Point(1, 2)


def test_main_with_numbers_input(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda: "1 2")

    assert main() == Point(1, 2)


def test_main_with_empty_input(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda: "1 k")

    assert main() == Point(0, 0)
