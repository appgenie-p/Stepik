from functools import wraps
from typing import Any, Callable, List, Type, TypeVar, cast

T = TypeVar("T")
F = Callable[..., Any]


def integer_params(cls: Type[T]) -> Type[T]:
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))
    return cls


def integer_params_decorated(func: Callable[..., T]) -> Callable[..., T]:
    @wraps(func)
    def wrapper(self: Type[T], *args: int, **kwargs: int) -> T:
        if not all(type(arg) == int for arg in args):
            raise TypeError("All arguments must be integers")
        if not all(type(v) == int and type(v) != bool for v in kwargs.values()):
            raise TypeError("All keyword arguments must be integers")
        return func(self, *args, **kwargs)

    return cast(F, wrapper)


@integer_params
class Vector:
    def __init__(self, *args: int):
        self.__coords: List[int] = list(args)

    def __getitem__(self, item: int) -> int:
        return self.__coords[item]

    def __setitem__(self, key: int, value: int):
        self.__coords[key] = value

    def set_coords(self, *coords: int, reverse: bool = False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]
