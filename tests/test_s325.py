from s325 import DigitRetrieve


def test_digit_retrieve():
    dg = DigitRetrieve()
    assert dg("123") == 123
    assert dg("45.54") is None
    assert dg("-56") == -56
    assert dg("12fg") == None
    assert dg("abc") == None
