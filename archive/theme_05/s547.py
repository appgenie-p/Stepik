from typing import Any, Optional, Union


class CellException(Exception):
    pass


class CellFloatException(CellException):
    pass


class CellIntegerException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:
    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value
        self._value: Optional[int] = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Any):
        if not isinstance(value, int):
            raise CellIntegerException
        if not self._min_value <= value <= self._max_value:
            raise CellIntegerException(
                "значение выходит за допустимый диапазон"
            )
        self._value = value


class CellFloat:
    def __init__(self, min_value: float, max_value: float):
        self._min_value = min_value
        self._max_value = max_value
        self._value: Optional[float] = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Any):
        if not isinstance(value, int):
            raise CellFloatException
        if not self._min_value <= value <= self._max_value:
            raise CellFloatException("значение выходит за допустимый диапазон")
        self._value = value


class CellString:
    def __init__(self, min_length: int, max_length: int):
        self._min_length = min_length
        self._max_length = max_length
        self._value: Optional[str] = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Any):
        if not isinstance(value, str):
            raise CellStringException
        if not self._min_length <= len(value) <= self._max_length:
            raise CellStringException(
                "значение выходит за допустимый диапазон"
            )
        self._value = value


class TupleData:
    __slots__ = ("data",)

    def __init__(self, *args: Union[CellInteger, CellFloat, CellString]):
        self.data = args

    def __getitem__(self, item: int):
        return self.data[item].value

    def __setitem__(self, key: int, value: Any):
        self.data[key].value = value

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return (x.value for x in self.data)
