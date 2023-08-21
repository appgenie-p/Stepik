from typing import Union


class Thing:
    def __init__(self, name: str, mass: Union[int, float]):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        """
        Предметы считаются равными, если у них одинаковые названия name (без
        учета регистра) и массы mass.
        """
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __lt__(self, other):
        return (self.name.lower(), self.mass) < (
            other.name.lower(),
            other.mass,
        )

    def __repr__(self):
        return f"Thing({self.name}, {self.mass})"


class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj: Thing) -> None:
        self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other) -> bool:
        """
        Для каждого объекта класса Thing одного ящика и можно найти ровно один
        равный объект из второго ящика
        """
        return sorted(self.box) == sorted(other.box)
