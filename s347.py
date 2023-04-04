import pytest


class Book:
    """Book."""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    """Library."""

    def __init__(self):
        self.book_list: list[Book] = []

    # Should be implemented methods: +, +=, -, -=, len.
    # While implementing methods, you should not create copies of the list.
    def __add__(self, book: Book):
        self.book_list.append(book)
        return self

    def __iadd__(self, book: Book):
        self.__add__(book)
        return self

    def __sub__(self, book: Book):
        """
        Надо делать проверку на тип объекта: если тип Book, то убираем элемент
        из списка методом remove(), а если тип int то удаляем элемент по его
        индексу из списка.
        """
        if isinstance(book, Book):
            try:
                self.book_list.remove(book)
            except ValueError:
                pass
        elif isinstance(book, int):
            self.book_list.pop(book)
        return self

    def __isub__(self, book: Book):
        self.__sub__(book)
        return self

    def __len__(self):
        return len(self.book_list)

    def __str__(self):
        return str(self.book_list)


@pytest.fixture
def lib():
    library = {}
    library["lib"] = Lib()
    library["book_1"] = Book('Name_1', 'Author_1', 2022)
    library["book_2"] = Book('Name_2', 'Author_1', 2023)
    return library


def test_add_book(lib):
    lib = lib["lib"]
    assert len(lib) == 0
    book_1 = lib["book_1"]
    lib + book_1
    assert len(lib) == 1
    book_2 = lib["book_2"]
    lib += book_2
    assert len(lib) == 2


def test_remove_book():
    lib = Lib()
    book_1 = Book('Name_1', 'Author_1', 2022)
    lib + book_1
    book_2 = Book('Name_2', 'Author_1', 2023)
    lib += book_2
    assert len(lib) == 2
    lib - book_1
    assert len(lib) == 1
    lib -= book_2
    assert len(lib) == 0
    # test removal from emty list.
    # assert error.
    lib -= book_2
    assert len(lib) == 0


def test_library_len():
    lib = Lib()
    assert len(lib) == 0
    book_1 = Book('Name_1', 'Author_1', 2022)
    lib = lib + book_1
    assert len(lib) == 1
    book_2 = Book('Name_2', 'Author_2', 2023)
    lib += book_2
    assert len(lib) == 2
    lib -= book_2
    assert len(lib) == 1
    lib -= book_2
    assert len(lib) == 1


if __name__ == "__main__":
    pytest.main([__file__])
