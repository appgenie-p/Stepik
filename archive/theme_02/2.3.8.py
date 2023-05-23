from typing import Union


class Thing:
    def __init__(self, name: str, weight: Union[int, float]) -> None:
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.__things: list = []

    @property
    def things(self) -> list:
        return self.__things

    def add_thing(self, thing: Thing):
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        try:
            self.__things.pop(indx)
        except IndexError:
            return

    def get_total_weight(self):
        return sum(thing.weight for thing in self.things)


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")