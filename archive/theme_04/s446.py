from typing import Any, NoReturn, Tuple, Union

Number = Union[int, float]


class Furniture:
    def __init__(self, name: str, weight: Number) -> None:
        self._name = name
        self._weight = weight

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__validate_name_and_weight_values(__name, __value)
        super().__setattr__(__name, __value)

    def __verify_name(self, name: Any) -> bool:
        self.__does_name_is_true(name)
        return True

    def __verify_weight(self, weight: Any) -> bool:
        self.__does_weight_is_number(weight)
        return True

    def __does_name_is_true(self, name: Any) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

    def __does_weight_is_number(self, weight: Any) -> None:
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")

    def __validate_name_and_weight_values(
        self, __name: str, __value: Any
    ) -> None:
        if __name == "_name":
            self.__verify_name(__value)
        if __name == "_weight":
            self.__verify_weight(__value)

    def get_attrs(self) -> Tuple[Any]:
        return tuple(attr for attr in vars(self) if attr.startswith('_'))


class Closet(Furniture):
    DoorsNumber = int
    IfSliding = bool

    def __init__(
        self, name: str, weight: Number, tp: IfSliding, doors: DoorsNumber
    ) -> None:
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name: str, weight: Number, height: Number) -> None:
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(
        self, name: str, weight: Number, height: Number, square: Number
    ) -> None:
        super().__init__(name, weight)
        self._height = height
        self._square = square
