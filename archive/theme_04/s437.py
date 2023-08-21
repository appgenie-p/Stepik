from functools import wraps
from typing import Callable, List, ParamSpec, Type, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


def integer_params(cls: Type[T]) -> Type[T]:
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))
    return cls


def integer_params_decorated(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        if not all(isinstance(arg, int) for arg in (*args[1:], *kwargs.values())):
            raise TypeError("All arguments must be integers")
        return func(*args, **kwargs)

    return wrapper


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
