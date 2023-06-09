"""Data validation module"""

from abc import abstractmethod
from typing import Type, Union


class Validator:
    """Базовый класс для валидаторов"""

    @abstractmethod
    def _is_valid(self, data) -> bool:
        pass

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return data


class ValidatorInit(Validator):
    """Абстрактный класс для валидаторов с параметрами"""

    VALIDATOR_TYPE: Type[Union[int, float]]

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: int) -> bool:
        return (
            isinstance(data, self.VALIDATOR_TYPE)
            and self.min_value <= data <= self.max_value
        )

    def __init_subclass__(cls, validator_type, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.VALIDATOR_TYPE = validator_type


class IntegerValidator(ValidatorInit, validator_type=int):
    """Валидатор целых чисел"""


class FloatValidator(ValidatorInit, validator_type=float):
    """Валидатор вещественных чисел"""


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)  # исключение ValueError
