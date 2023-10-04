from typing import Optional


class PrimaryKeyError(Exception):
    def __init__(self, *, id: Optional[str] = None, pk: Optional[str] = None):
        self.id = id
        self.pk = pk

    def __str__(self) -> str:
        if self.id is None and self.pk is None:
            return "Первичный ключ должен быть целым неотрицательным числом"
        if self.id:
            return f"Значение первичного ключа id = {self.id} недопустимо"
        return f"Значение первичного ключа pk = {self.pk} недопустимо"


def main():
    try:
        raise PrimaryKeyError(id="-10.5")
    except PrimaryKeyError as e:
        print(e)


if __name__ == "__main__":
    main()