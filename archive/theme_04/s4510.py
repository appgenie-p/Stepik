from abc import ABC
from typing import Union

Number = Union[int, float]


class Food(ABC):
    def __init__(self, name: str, weight: Number, calories: int) -> None:
        self._name = name
        self._weight = weight
        self._calories = calories

    def __getattr__(self, name: str) -> None:
        property = f"_{name}"
        if hasattr(self, property):
            return getattr(self, property)


class BreadFood(Food):
    def __init__(self, name: str, weight: Number, calories: int, white: bool) -> None:
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name: str, weight: Number, calories: int, dietary: bool) -> None:
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name: str, weight: Number, calories: int, fish: str) -> None:
        super().__init__(name, weight, calories)
        self._fish = fish
