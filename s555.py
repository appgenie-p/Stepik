from copy import deepcopy
from typing import Any, List, NamedTuple, Tuple


class Stuff(NamedTuple):
    name: str
    weight: int


class Box:
    def __init__(self, name: str, max_weight: int):
        self._name = name
        self._max_weight = max_weight
        self._things: List[Any] = []
        self._current_weight = 0

    def add_thing(self, obj: Tuple[str, int]):
        obj = Stuff(*obj)
        if self._current_weight + obj.weight > self._max_weight:
            raise ValueError("Невозможно добавить предмет в коробку")
        self._things.append(obj)
        self._current_weight += obj.weight


class BoxDefender(Box):
    def __init__(self, box: Box):
        self._box = box

    def __enter__(self):
        pass