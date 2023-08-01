"""Data validation module"""

from abc import abstractmethod
from typing import Any, Generic, Type, TypeVar


class Validator:
    """Базовый класс для валидаторов"""

    @abstractmethod
    def _is_valid(self, data: Any) -> bool:
        return True

    def __call__(self, data: Any) -> Any:
        if not self._is_valid(data):
            raise ValueError("Invalid data")
        return data


class IntegerValidator(Validator):
    """Валидатор целых чисел в заданном диапазоне."""

    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: Any) -> bool:
        return isinstance(data, int) and (
            self.min_value <= data <= self.max_value
        )


integer_validator = IntegerValidator(-10, 10)
# float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
# res2 = float_validator(10)    # исключение ValueError
