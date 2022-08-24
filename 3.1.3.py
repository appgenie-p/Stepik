class Book:
    def __init__(self, title: str = '', author: str = '', pages: int = 0,
                 year: int = 0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, val) -> None:
        key_type = self.__init__.__annotations__.get(key)
        if not isinstance(val, key_type):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, val)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
