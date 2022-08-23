class SuperShop:
    """
    myshop = SuperShop(название магазина)
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods: list = []

    def add_product(self, product: 'Product') -> None:
        self.goods.append(product)

    def remove_product(self, product: 'Product') -> None:
        self.goods.remove(product)


class StringValue:
    """
    должен проверять, что присваивается строковый тип с длиной строки в
    диапазоне [2; 50], т.е. min_length = 2, max_length = 50. Если проверки не
    проходят, то соответствующие (прежние) значения меняться не должны.
    """
    pass


class PriceValue :
    """
    должен проверять, что присваивается вещественное или целочисленное значение
    в диапазоне [0; 10000], т.е. max_value = 10000. Если проверки не проходят,
    то соответствующие (прежние) значения меняться не должны.
    """
    pass


class Product:
    """
    pr = Product(наименование, цена)
    """
    name = StringValue(min_length=2, max_length=50)
    price = PriceValue(max_value=10000)

    def __init__(self, good_name, good_price) -> None:
        self.name = good_name
        self.price = good_price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
