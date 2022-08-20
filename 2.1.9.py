from typing import List, Optional


class LinkedList:
    def __init__(self) -> None:
        self.head: 'ObjList' = None
        self.tail: 'ObjList' = None

    def add_obj(self, obj: 'ObjList') -> None:
        """добавление нового объекта obj класса ObjList в конец связного
        списка
        """
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self) -> None:
        try:
            prev = self.tail.get_prev()
            prev.set_next(None)
            self.tail = prev
        except AttributeError:
            self.head = None
            self.tail = None

    def get_data(self) -> List[str]:
        """получение списка из строк локального свойства __data всех объектов
        связного списка
        """
        try:
            list = []
            list.append(self.head.get_data())
            next_obj = self.head.get_next()
            while next_obj is not None:
                list.append(next_obj.get_data())
                next_obj = next_obj.get_next()
            return list
        except AttributeError:
            return []


class ObjList:
    def __init__(self, data: str) -> None:
        self.__next: ObjList = None
        self.__prev: ObjList = None
        self.__data: str = data

    def set_next(self, obj: 'ObjList') -> None:
        self.__next = obj

    def set_prev(self, obj: 'ObjList') -> None:
        self.__prev = obj

    def get_next(self) -> 'ObjList':
        return self.__next

    def get_prev(self) -> 'ObjList':
        return self.__prev

    def set_data(self, data: str) -> None:
        self.__data = data

    def get_data(self) -> str:
        return self.__data

    def __repr__(self) -> str:
        return f'{self.__data}'


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.add_obj(ObjList("данные 4"))
lst.remove_obj()
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)
