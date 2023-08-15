from s465 import Book, ShopGenericView, ShopUserView


def test_book_str():
    class Book_str(Book, ShopGenericView):
        pass

    book = Book_str("Python ООП", "Балакирев", 2022)
    assert str(book) == (
        f"_id: {book.get_pk()}\n"
        f"_title: {book._title}\n"
        f"_author: {book._author}\n"
        f"_year: {book._year}\n"
    )


def test_book_repr():
    class Book_repr(Book, ShopUserView):
        pass

    book = Book_repr("Python ООП", "Балакирев", 2022)
    assert str(book) == (
        f"_title: {book._title}\n"
        f"_author: {book._author}\n"
        f"_year: {book._year}\n"
    )
