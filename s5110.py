from typing import Any, Union


class FloatValidator:
    def __init__(self, min_value: float, max_value: float):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value: Any) -> bool:
        if not isinstance(value, float):
            raise TypeError(f"Value must be float, not {type(value)}")
        if value < self.min_value:
            raise ValueError(f"Value must be >= {self.min_value}")
        if value >= self.max_value:
            raise ValueError(f"Value must be <= {self.max_value}")
        return True


class IntegerValidator:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value: Any) -> bool:
        if not isinstance(value, int):
            raise TypeError(f"Value must be int, not {type(value)}")
        if value < self.min_value:
            raise ValueError(f"Value must be >= {self.min_value}")
        if value >= self.max_value:
            raise ValueError(f"Value must be <= {self.max_value}")
        return True


# def check_value(
#     value: An
#     obj: Union[FloatValidator, IntegerValidator],
#     type_: Union[int, float],
# ) -> bool:
#     return True
