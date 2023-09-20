from typing import Any, Union

Number = Union[int, float]


class Function:
    def __init__(self):
        self._amplitude = 1.0
        self._bias = 0.0

    def __call__(self, x: Number, *args: Any, **kwargs: Any) -> Number:
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x: Number) -> Number:
        raise NotImplementedError(
            "метод _get_function должен быть переопределен в дочернем классе"
        )

    def __add__(self, other: Number):
        obj = self._return_object_copy(other)
        obj._bias = self._bias + other
        return obj

    def _return_object_copy(self, other: Any):
        if type(other) not in (int, float):
            raise TypeError("other должно быть числом")
        return self.__class__(self)


class Linear(Function):
    def __init__(self, *args: Any):
        super().__init__()
        if len(args) == 1 and isinstance(args[0], Linear):
            self._k = args[0]._k
            self._b = args[0]._b
        else:
            self._k, self._b = args

    def _get_function(self, x: Number) -> Number:
        return self._k * x + self._b

    def __mul__(self, other: Number):
        obj = self._return_object_copy(other)
        obj._amplitude = self._amplitude * other
        return obj
