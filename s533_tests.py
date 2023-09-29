import pytest
from _pytest.monkeypatch import MonkeyPatch

from s533 import input_int_numbers


def test_input_int_numbers(monkeypatch: MonkeyPatch):
    input_ = "1 2 3 4 5"
    monkeypatch.setattr("builtins.input", lambda: input_)
    assert input_int_numbers() == (1, 2, 3, 4, 5)


def test_int_numbers_raise(monkeypatch: MonkeyPatch):
    input_ = "1 2 3 4 F"
    monkeypatch.setattr("builtins.input", lambda: input_)
    with pytest.raises(TypeError):
        input_int_numbers()

