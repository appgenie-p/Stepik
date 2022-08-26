import pytest

from s324 import LengthValidator, CharsValidator

from string import ascii_lowercase, digits


@pytest.fixture
def length_validator():
    return LengthValidator(3, 50)


@pytest.fixture
def chars_validator():
    return CharsValidator(ascii_lowercase + digits)

@pytest.mark.parametrize('value,len_res,char_res', [
    ('zhopa', True, True),
    ('zhopa1234', True, True),
    ('zh', False, True),
    ('zhopa@', True, False),
])
def test_length_validator_class(
            length_validator,
            chars_validator,
            value,
            len_res,
            char_res
        ):
    # value, len_res, char_res,  = val
    assert length_validator(value) is len_res
    assert chars_validator(value) is char_res
