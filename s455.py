from typing import Any, Generic, TypeVar

T = TypeVar('T', contravariant=True)


class Validator(Generic[T]):
    def _is_valid(self, data: T) -> bool:
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator[float]):
    def __init__(self, min_value: float, max_value: float) -> None:
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data: Any) -> bool:
        return (
            isinstance(data, float)
            and self._min_value <= data <= self._max_value
        )

    def __call__(self, value: float) -> bool:
        return self._is_valid(value)
