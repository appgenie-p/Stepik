from typing import Any, List, Union

Number = Union[int, float]


class Validator:
    def __init__(self, min_value: Number, max_value: Number):
        self.min_value = min_value
        self.max_value = max_value

    def _check_min_max(self, value: Any) -> bool:
        if value < self.min_value:
            raise ValueError(f"Value must be >= {self.min_value}")
        if value > self.max_value:
            raise ValueError(f"Value must be <= {self.max_value}")
        return True


class FloatValidator(Validator):
    def __call__(self, value: Any) -> bool:
        if not isinstance(value, float):
            raise ValueError("значение не прошло валидацию")
        self._check_min_max(value)
        return True


class IntegerValidator(Validator):
    def __call__(self, value: Any) -> bool:
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError("значение не прошло валидацию")
        self._check_min_max(value)
        return True


def is_valid(
    lst: List[Any],
    validators: List[Union[FloatValidator, IntegerValidator]],
) -> List[Number]:  # sourcery skip: instance-method-first-arg-name
    result: List[Number] = []
    for num in lst:
        for validator in validators:
            try:
                validator(num)
            except (TypeError, ValueError):
                continue
            else:
                result.append(num)
    return result
