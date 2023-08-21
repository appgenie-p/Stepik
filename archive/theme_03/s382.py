from typing import Any, Union


class Record:
    def __init__(self, **kwargs) -> None:
        self.__dict__ = kwargs

    def get_item_key(self, index: int) -> str:
        item_list = list(enumerate(self.__dict__.items()))
        try:
            return item_list[index][1][0]
        except IndexError:
            raise IndexError("неверный индекс поля")

    def __getitem__(self, index: int) -> Union[str, int]:
        return getattr(self, self.get_item_key(index))

    def __setitem__(self, index: int, value: Any) -> None:
        return setattr(self, self.get_item_key(index), value)


r = Record(pk=1, title="Python ООП", author="Балакирев")
breakpoint()
print(r[0])
r[0] = 2
print(r[0])
