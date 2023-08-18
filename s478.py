from typing import Any, Protocol, Type

NOTES = "до", "ре", "ми", "фа", "соль", "ля", "си"


class Note:
    __slots__ = "_name", "_ton"

    def __init__(self, name: str, ton: int):
        self._name = name
        self._ton = ton

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "_ton" and __value not in (-1, 0, 1):
            raise ValueError("недопустимое значение тона")
        if __name == "_name" and __value not in NOTES:
            raise ValueError("недопустимое название ноты")
        super().__setattr__(__name, __value)


class NoteInterface(Protocol):
    def __init__(self, name: str, ton: int):
        ...

    def __setattr__(self, __name: str, __value: Any) -> None:
        ...


class Notes:
    __slots__ = "_do", "_re", "_mi", "_fa", "_solt", "_la", "_si"

    instance = None

    note_cls: Type[NoteInterface] = Note

    def __new__(cls) -> "Notes":
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        for i, note in enumerate(NOTES):
            setattr(self, self.__slots__[i], type(self).note_cls(note, 0))

    def __getitem__(self, item: Any) -> NoteInterface:
        if isinstance(item, int):
            return self._get_by_note_number(item)
        raise TypeError("недопустимый тип аргумента")

    def _get_by_note_number(self, number: int) -> NoteInterface:
        if number < 0 or number > 6:
            raise IndexError("недопустимый индекс")
        return getattr(self, self.__slots__[number])
