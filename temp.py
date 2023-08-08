from typing import Callable, TypeVar

from typing_extensions import Concatenate, ParamSpec

P = ParamSpec('P')
T = TypeVar('T')


def printing_decorator(
    func: Callable[P, T]
) -> Callable[Concatenate[str, P], T]:
    def wrapper(msg: str, /, *args: P.args, **kwds: P.kwargs) -> T:
        print("Calling", func, "with", msg)
        return func(*args, **kwds)

    return wrapper


@printing_decorator
def add_forty_two(value: int) -> int:
    return value + 42


a = add_forty_two('three', 3)
