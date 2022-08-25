from typing import Union


class Product:
    counter = 1
    param_types = {
        'id': (int,),
        'name': (str,),
        'weight': (int, float),
        'price': (int, float),
    }

    def __init__(self, name: str, weight: Union[int, float],
                 price: Union[int, float]) -> None:
        self.name = name
        self.weight = weight
        self.price = price
        self.id: int = self.counter
        Product.counter += 1

    def __setattr__(self, key, val) -> None:
        if key in self.param_types and type(val) in self.param_types[key]:
            if (key == 'weight' or key == 'price') and val <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            super().__setattr__(key, val)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, __name: str) -> None:
        if __name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(__name)


class Shop:
    def __init__(self, name: int) -> None:
        self.name = name
        self.goods: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        try:
            self.goods.remove(product)
        except ValueError:
            return


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Норм", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
