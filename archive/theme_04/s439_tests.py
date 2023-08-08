import pytest

from s439 import StringDigit


def test_stringdigit_class():
    sd = StringDigit("6546186465463")
    assert sd.data == "6546186465463"
    with pytest.raises(ValueError):
        s_error = StringDigit("dfgdfdshdfhdf")
