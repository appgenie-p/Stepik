from typing import Tuple, Union


class Animal:
    def __init__(self, name: str, old: int) -> None:
        self.name, self.old = name, old


class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: float) -> None:
        super().__init__(name, old)
        self.color, self.weight = color, weight

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


class Dog(Animal):
    Size = Tuple[float, float]

    def __init__(self, name: str, old: int, breed: str, size: Size) -> None:
        super().__init__(name, old)
        self.breed, self.size = breed, size

    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"


cat = Cat("кот", 4, "black", 2.25)
dog = Dog("пёс", 4, "хаски", (2, 3))
