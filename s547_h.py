from typing import Any, Optional, Union


class CellException(Exception):
    pass


class CellFloatException(CellException):
    pass


class CellIntegerException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    error = CellException

    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value
        self._value: Optional[Union[int, float, str]] = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Union[int, float, str]):
        value_for_range_check = len(value) if isinstance(value, str) else value
        if not self._min_value <= value_for_range_check <= self._max_value:
            raise self.error(
                "значение выходит за допустимый диапазон"
            )
        self._value = value


class CellInteger(Cell):
    error = CellIntegerException


class CellFloat(Cell):
    error = CellFloatException


class CellString(Cell):
    error = CellStringException


class TupleData:
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
