from abc import ABC, abstractmethod
from typing import Union

PositiveNum = Union[int, float]


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def population(self) -> int:
        pass

    @property
    @abstractmethod
    def square(self) -> PositiveNum:
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass


class Country(CountryInterface):
    def __init__(self, name: str, population: int, square: PositiveNum):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, value: int):
        self._population = value

    @property
    def square(self) -> PositiveNum:
        return self._square

    @square.setter
    def square(self, value: PositiveNum):
        self._square = value

    def get_info(self) -> str:
        return f"{self.name}: {self.square}, {self.population}"

    def __str__(self):
        return self.get_info()
