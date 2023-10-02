from pytest import MonkeyPatch

from s537 import TupleLimit, main


def test_tuplelimit_creation() -> None:
    assert TupleLimit([1, 2, 3], 5) == (1, 2, 3)


def test_main(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda: "1 2 3 4 5")
    assert main() == (1.0, 2.0, 3.0, 4.0, 5.0)


def test_main_err(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda: "1 2 3 4 5 6")
    assert isinstance(main(), ValueError)
