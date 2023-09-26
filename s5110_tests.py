import pytest

from s5110 import FloatValidator, IntegerValidator, is_valid


def test_float_validator_creation():
    f = FloatValidator(0.0, 1.0)
    assert f(0.5) is True


def test_float_validator_creation_with_bad_min_value():
    f = FloatValidator(0.0, 1.0)
    with pytest.raises(ValueError):
        f(-0.1)


def test_symbols_check_with_validators():
    fv = FloatValidator(0, 10.5)
    iv = IntegerValidator(-10, 20)
    assert is_valid(
        [1, 4.5, -10.5, 100, True, "abc", (1, 2)], validators=[fv, iv]
    ) == [1, 4.5]
