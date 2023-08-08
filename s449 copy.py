from functools import wraps
from typing import Any, Callable, List, Type, TypeVar

vector_log: List[str] = []

T = TypeVar('T', bound="Vector")
Logs = List[str]


def class_log(log: Logs) -> Callable[[Type[T]], Type[T]]:
    def decorator(cls: Type[T]) -> Type[T]:
        methods: dict[str, Callable[..., Any]] = {
            k: v for k, v in cls.__dict__.items() if callable(v)
        }
        for k, v in methods.items():
            setattr(cls, k, log_decorator(v, log))
        return cls

    return decorator


def log_decorator(method: Callable[..., T], log: Logs) -> Callable[..., T]:
    @wraps(method)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        log.append(method.__name__)
        return method(*args, **kwargs)

    return wrapper


@class_log(vector_log)
class Vector:
    def __init__(self, *args: int):
        self.__coords = list(args)

    def __getitem__(self, item: int) -> int:
        return self.__coords[item]

    def __setitem__(self, key: int, value: int):
        self.__coords[key] = value
