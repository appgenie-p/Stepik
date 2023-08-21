from typing import Optional, Union


Weight = Union[int, float]


class Thing:
    def __init__(self, name: str, weight: Weight) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f"Thing({self.name}, {self.weight})"


class Bag:
    def __init__(self, max_weight: Weight) -> None:
        self.max_weight = max_weight
        self.things: list = []
        self.current_weight: Weight = 0

    def add_thing(self, thing: Thing) -> None:
        self._check_max_weight(thing)
        self.things.append(thing)
        self.current_weight += thing.weight

    def _check_max_weight(self, thing: Thing, index: Optional[int] = None):
        new_weight = (
            (self.current_weight - self.things[index].weight + thing.weight)
            if index is not None
            else (self.current_weight + thing.weight)
        )

        if new_weight > self.max_weight:
            raise ValueError("превышен суммарный вес предметов")

    def __getitem__(self, index: int) -> Thing:
        return self.things[index]

    def __setitem__(self, index: int, value: Thing) -> None:
        self._check_max_weight(value, index)
        self.current_weight -= self.things[index].weight
        self.things[index] = value
        self.current_weight += value.weight

    def __delitem__(self, index: int) -> None:
        deleted_item = self.things.pop(index)
        self.current_weight -= deleted_item.weight


b = Bag(700)
b.add_thing(Thing("книга", 100))
b.add_thing(Thing("носки", 200))

b[0] = Thing("рубашка", 500)

try:
    b[0] = Thing("рубашка", 800)
except ValueError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
