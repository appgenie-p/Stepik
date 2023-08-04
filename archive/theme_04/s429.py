from typing import Any, Generator, NamedTuple, Protocol, Tuple, TypeVar

T = TypeVar("T")


class Itr(Protocol):
    def __iter__(self) -> Generator[Any, None, None]:
        ...


class IteratorAttrs(Itr):
    def __iter__(self) -> Generator[Tuple[str, Any], None, None]:
        return (items for items in self.__dict__.items())


WidthLength = NamedTuple("WidthLength", [("width", int), ("length", int)])


class Phone(Protocol):
    model: str
    size: WidthLength
    memory: int

    def __iter__(self) -> Generator[Any, None, None]:
        ...


class SmartPhone(IteratorAttrs, Phone):
    def __init__(self, model: str, size: Tuple[int, int], memory: int) -> None:
        self.model = model
        self.size = WidthLength(*size)
        self.memory = memory
