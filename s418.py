"""Data validation module"""


from abc import abstractmethod


class Validator:
    """Базовый класс для валидаторов"""

    @abstractmethod
    def _is_valid(self, data) -> bool:
        pass

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return data


class IntegerValidator(Validator):
    """Валидатор целых чисел"""

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: int) -> bool:
        return (
            isinstance(data, int) and self.min_value <= data <= self.max_value
        )


class FloatValidator(Validator):
    """Валидатор вещественных чисел"""

    def __init__(self, min_value: float, max_value: float):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: float) -> bool:
        return (
            isinstance(data, float)
            and self.min_value <= data <= self.max_value
        )


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)  # исключение ValueError
