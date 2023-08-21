class Descriptor:
    def __set_name__(self, obj, name) -> None:
        self.name = "_" + name

    def __set__(self, obj, value: str) -> None:
        if self.checker(value):
            setattr(obj, self.name, value)

    def __get__(self, obj, type=None):
        return getattr(obj, self.name)


class StringValue(Descriptor):
    def __init__(self, min_length: int = 2, max_length: int = 50) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def checker(self, value: str):
        return (
            isinstance(value, str) and self.min_length <= len(value) <= self.max_length
        )


class PriceValue(Descriptor):
    def __init__(self, max_value: int = 10000) -> None:
        self.max_value = max_value

    def checker(self, value: str):
        return (
            isinstance(value, int)
            or isinstance(value, float)
            and value in range(0, self.max_value + 1)
        )


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, good_name, good_price) -> None:
        self.name = good_name
        self.price = good_price


class SuperShop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods: list[Product] = []

    def add_product(self, product: "Product") -> None:
        self.goods.append(product)

    def remove_product(self, product: "Product") -> None:
        if product in self.goods:
            self.goods.remove(product)


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")

shop = SuperShop("У Балакирева")
shop.add_product(Product("name", 100))
shop.add_product(Product("name", 100))
assert (
    shop.name == "У Балакирева"
), "атрибут name объекта класса SuperShop содержит некорректное значение"

for p in shop.goods:
    assert p.price == 100, "дескриптор price вернул неверное значение"
    assert p.name == "name", "дескриптор name вернул неверное значение"

t = Product("name 123", 1000)
shop.add_product(t)
shop.remove_product(t)
assert (
    len(shop.goods) == 2
), "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"

assert hasattr(shop.goods[0], "name") and hasattr(shop.goods[0], "price")

t = Product(1000, "name 123")
if hasattr(t, "_name"):
    assert type(t.name) == str, "типы поля name должнен быть str"
if hasattr(t, "_price"):
    assert type(t.price) in (int, float), "тип поля price должнен быть int или float"
