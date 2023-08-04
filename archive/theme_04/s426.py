from typing import Any, Iterable


class Tuple(tuple[Any, ...]):
    def __add__(self, other: Iterable[Any]) -> "Tuple":
        return Tuple(tuple(self) + tuple(other))
