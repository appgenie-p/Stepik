"""Data validation module"""

from abc import abstractmethod
from typing import Generic, Type, TypeVar

T = TypeVar('T', Type[int], Type[float])


class Validator(Generic[T]):
    """Базовый класс для валидаторов"""

    @abstractmethod
    def _is_valid(self, data: T) -> bool:
        pass

    def __call__(self, data: T):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return data


class ValidatorInit(Validator, Generic[T]):
    """Абстрактный класс для валидаторов с параметрами"""

    VALIDATOR_TYPE: T

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: T) -> bool:
        return (
            isinstance(data, self.VALIDATOR_TYPE)
            and self.min_value <= data <= self.max_value
        )

    def __init_subclass__(cls, validator_type: T, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.VALIDATOR_TYPE = validator_type


class IntegerValidator(ValidatorInit, validator_type=int):
    """Валидатор целых чисел"""


class FloatValidator(ValidatorInit, validator_type=float):
    """Валидатор вещественных чисел"""
