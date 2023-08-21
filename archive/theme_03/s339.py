from typing import Tuple


class Ingredient:
    def __init__(self, name: str, volume: float, measure: str) -> None:
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self) -> str:
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args: Ingredient) -> None:
        self.ingridients = list(args)

    def add_ingredient(self, ingridient: Ingredient) -> None:
        self.ingridients.append(ingridient)

    def remove_ingredient(self, ingridient: Ingredient) -> None:
        self.ingridients.remove(ingridient)

    def get_ingredients(self) -> Tuple[Ingredient, ...]:
        return tuple(self.ingridients)

    def __len__(self) -> int:
        return len(self.ingridients)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe)
