from s438 import SoftList


def test_softline_class():
    sl = SoftList("python")
    sl = SoftList("python")
    assert sl[0] == "p"
    assert sl[-1] == "n"
    assert sl[6] == False
    assert sl[-7] == False
