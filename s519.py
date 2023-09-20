from typing import Any, Generic, Type, TypeVar, Union


T = TypeVar("T")
Numbers = Union[int, float]


class PositiveNumberDescriptor(Generic[T]):
    def __set_name__(self, owner: Type[T], name: str) -> None:
        self.name = f"_{name}"

    def __get__(self, obj: T, objtype: Type[T]) -> Numbers:
        return obj.__dict__[self.name]

    def __set__(self, obj: T, value: Any) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise TypeError("Value must be positive")
        obj.__dict__[self.name] = value


class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
