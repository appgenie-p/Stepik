class Animal:
    def __init__(self, name: str, kind: str, old: int) -> None:
        self.__name, self.__kind, self.__old = name, kind, old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


input_data = """
Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3
"""

animal = [Animal(val.split('; ')) for val in input_data.strip().split('\n')]

print(animal)