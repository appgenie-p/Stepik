from numbers import Number
from typing import NamedTuple, Tuple


class Thing:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name: str, weight: float, author: str, date: str):
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name: str, weight: float, memory: int, cpu: str):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


Dimensions = NamedTuple(
    "Dimensions", [("width", Number), ("length", Number), ("height", Number)]
)


class Auto(Thing):
    def __init__(self, name: str, weight: float, dims: Tuple[Number, Number, Number]):
        super().__init__(name, weight)
        self.dims = Dimensions(*dims)


class Mercedes(Auto):
    def __init__(
        self,
        name: str,
        weight: float,
        dims: Tuple[Number, Number, Number],
        model: str,
        old: int,
    ):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(
        self,
        name: str,
        weight: float,
        dims: Tuple[Number, Number, Number],
        model: str,
        wheel: int,
    ):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel
