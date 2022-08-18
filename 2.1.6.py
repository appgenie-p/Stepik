class Book:
    def __init__(self, author, title, price) -> None:
        self.__author: str = ''
        self.__title: str = ''
        self.__price: int = 0
        self.set_title(title)
        self.set_author(author)
        self.set_price(price)

    def set_title(self, title: str) -> None:
        '''запись в локальное приватное свойство __title объектов
        класса Book значения title'''
        self.__title = title

    def set_author(self, author: str) -> None:
        '''запись в локальное приватное свойство __author объектов
        класса Book значения author'''
        self.__author = author

    def set_price(self, price: int) -> None:
        '''запись в локальное приватное свойство __price объектов
        класса Book значения price'''
        self.__price = price

    def get_title(self) -> str:
        '''получение значения локального приватного свойства __title
        объектов класса Book'''
        return self.__title

    def get_author(self) -> str:
        '''получение значения локального приватного свойства __author
        объектов класса Book'''
        return self.__author

    def get_price(self) -> int:
        '''получение значения локального приватного свойства __price
        объектов класса Book'''
        return self.__price
