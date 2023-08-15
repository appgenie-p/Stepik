from s455 import FloatValidator


def test_float_validator_valid_value():
    validator = FloatValidator(0.0, 1.0)
    assert validator(0.5) is True


def test_float_validator_invalid_value():
    validator = FloatValidator(0.0, 1.0)
    assert validator(1.5) is False


def test_float_validator_invalid_type():
    validator = FloatValidator(0.0, 1.0)
    assert validator("not a float") is False
