"""Урок 415 Наследование"""

import itertools


class Thing:
    """Base class"""

    ID = itertools.count(1)

    def __init__(
        self,
        name: str,
        price: float,
    ) -> None:
        self.id = next(self.__class__.ID)
        self.name = name
        self.price = price
        self.weight, self.dims, self.memory, self.frm = (None,) * 4

    def get_data(self):
        return tuple(self.__dict__.values())


# table = Table(name, price, weight, dims)
class Table(Thing):
    """Table class"""

    def __init__(self, name, price, weight, dims) -> None:
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


# book = ElBook(name, price, memory, frm)
class ElBook(Thing):
    """Table class"""

    def __init__(self, name, price, memory, frm) -> None:
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(table.get_data())
print(book.get_data())
