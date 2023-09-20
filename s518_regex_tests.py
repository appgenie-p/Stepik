from _pytest.monkeypatch import MonkeyPatch

from s518_regex import main


def test_my_function(monkeypatch: MonkeyPatch):
    user_input = "1 -5.6 True abc 0 23.56 hello"
    monkeypatch.setattr("builtins.input", lambda: user_input)
    assert main() == [1, -5.6, "True", "abc", 0, 23.56, "hello"]
