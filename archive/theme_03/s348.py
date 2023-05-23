from typing import List, Union


class Item:
    def __init__(self, name: str, money: Union[int, float]):
        self.name = name
        self.money = money

    # s = it1 + it2
    # s = it1 + it2 + ... + itN
    def __add__(self, other: "Item"):
        if isinstance(other, Item):
            return self.money + other.money
        return self.money + other

    def __radd__(self, other: int):
        return self.money + other


class Budget:
    def __init__(self) -> None:
        self.items: List[Item] = []

    # add_item(self, it)
    def add_item(self, it: Item) -> None:
        if isinstance(it, Item):
            self.items.append(it)

    # remove_item(self, indx) if index exists
    def remove_item(self, indx: int) -> None:
        if indx < len(self.items):
            self.items.pop(indx)

    # get_items(self)
    def get_items(self) -> List[Item]:
        return self.items


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)
