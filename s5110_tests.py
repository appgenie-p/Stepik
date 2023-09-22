import pytest

from s5110 import FloatValidator


def test_float_validator_creation():
    f = FloatValidator(0.0, 1.0)
    assert f(0.5) is True


def test_float_validator_creation_with_bad_min_value():
    f = FloatValidator(0.0, 1.0)
    with pytest.raises(ValueError):
        f(-0.1)
