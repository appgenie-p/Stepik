from tkinter.messagebox import NO


class LinkedList:
    def __init__(self) -> None:
        self.head: 'ObjList' = None
        # ссылка на первый объект связного списка (если список пустой, то head = None)
        self.tail: 'ObjList' = None
        # ссылка на последний объект связного списка (если список пустой, то tail = None).

    def add_obj(self, obj: 'ObjList') -> None:
        """добавление нового объекта obj класса ObjList в конец связного
        списка
        """
        # вставка, если есть предыдущее значение
        if self.head is None:
            self.head = obj
            self.tail = obj
            self.tail.set_prev(self.head)
        else:
            prev_obj = self.tail.get_prev()
            obj.set_prev(prev_obj)
            prev_obj.set_next(obj)
            self.tail = obj

    def remove_obj(self):
        """удаление последнего объекта из связного списка
        Взять последний эллемент, проверить свойство __prev
        if __prev not Null: self.tail = __prev
        """
        pass

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов
        связного списка
        """
        pass


class ObjList:
    def __init__(self, data: str) -> None:
        self.__next: ObjList = None
        # ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
        self.__prev: ObjList = None
        # ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
        self.__data: str = data
        # строка с данными.

    def set_next(self, obj: 'ObjList') -> None:
        #  - изменение приватного свойства __next на значение obj;
        self.__next = obj

    def set_prev(self, obj: 'ObjList') -> None:
        #  - изменение приватного свойства __prev на значение obj;
        self.__prev = obj

    def get_next(self) -> 'ObjList':
        return self.__next

    def get_prev(self) -> 'ObjList':
        return self.__prev

    def set_data(self, data: str) -> None:
        self.__data = data

    def get_data(self) -> str:
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']