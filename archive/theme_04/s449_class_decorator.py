from typing import Any, Callable, List, ParamSpec, Type, TypeVar

vector_log: List[str] = []

T = TypeVar('T', bound="Vector")
P = ParamSpec('P')
Logs = List[str]


class ClassLog:
    def __init__(self, log: Logs) -> None:
        self.log = log

    def __call__(self, cls: Type[T]) -> Type[T]:
        methods: dict[str, Callable[..., Any]] = {
            k: v for k, v in cls.__dict__.items() if callable(v)
        }
        for k, v in methods.items():
            setattr(cls, k, self.log_decorator(v))
        return cls

    def log_decorator(self, method: Callable[P, T]) -> Callable[P, T]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            self.log.append(method.__name__)
            return method(*args, **kwargs)

        return wrapper


@ClassLog(vector_log)
class Vector:
    def __init__(self, *args: int):
        self.__coords = list(args)

    def __getitem__(self, item: int) -> int:
        return self.__coords[item]

    def __setitem__(self, key: int, value: int):
        self.__coords[key] = value
