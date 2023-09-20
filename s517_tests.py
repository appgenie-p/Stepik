from s517 import if_int, main


def test_if_int():
    sample = [1, "a", 2, "b", 3, "c"]
    count = sum(if_int(x) for x in sample)
    assert count == 3
