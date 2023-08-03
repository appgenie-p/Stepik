from typing import Any, Dict, Mapping


class Thing:
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(Dict[Thing, Thing]):
    def __init__(self, things: Mapping[Any, Thing] = {}):
        if not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')

        if not all(isinstance(x, Thing) for x in things.keys()):
            raise TypeError('все ключи должны быть экземплярами Thing')
        super().__init__(things)

    def __setitem__(self, key: Any, value: Thing) -> None:
        if not isinstance(key, Thing):
            raise TypeError('все ключи должны быть экземплярами Thing')
        super().__setitem__(key, value)
