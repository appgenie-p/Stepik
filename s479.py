from typing import Any, Union

Number = Union[int, float]


class Function:
    def __init__(self):
        self._amplitude = 1.0  # амплитуда функции
        self._bias = 0.0  # смещение функции по оси Oy

    def __call__(self, x: Number, *args: Any, **kwargs: Any) -> Number:
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x: Number) -> Number:
        raise NotImplementedError(
            "метод _get_function должен быть переопределен в дочернем классе"
        )

    def __add__(self, other: Number):
        if type(other) not in (int, float):
            raise TypeError("смещение должно быть числом")

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj
