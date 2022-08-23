import copy
from typing import List, Optional


class StackObj:
    def __init__(self, data: str) -> None:
        self.__data: Optional[str] = None
        self.__next: Optional[StackObj] = None
        self.data = data

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str) -> None:
        self.__data = data

    @property
    def next(self) -> Optional['StackObj']:
        return self.__next

    @next.setter
    def next(self, next_obj: Optional['StackObj']) -> None:
        if isinstance(next_obj, StackObj) or next_obj is None:
            self.__next = next_obj

    def __repr__(self) -> str:
        return f'{self.data}'


class Stack:
    def __init__(self) -> None:
        self.top: Optional[StackObj] = None

    def push(self, obj: StackObj) -> None:
        try:
            last_obj = self.top
            next_obj = self.top.next
            while next_obj is not None:
                last_obj = next_obj
                next_obj = next_obj.next
            last_obj.next = obj
        except AttributeError:
            self.top = obj

    def pop(self) -> Optional[StackObj]:
        if self.top is None:
            return None
        if not self.top.next:
            deleted_obj = self.top
            self.top = None
            return deleted_obj
        iter_obj = self.top
        while iter_obj.next.next is not None:
            iter_obj = iter_obj.next
        return_obj = iter_obj.next
        iter_obj.next = None
        return return_obj

    def get_data(self) -> Optional[List[StackObj]]:
        obj = self.top
        objs_list = []
        while obj is not None:
            objs_list.append(obj.data)
            obj = obj.next
        return objs_list

    def __repr__(self) -> str:
        return ' -> '.join(self.get_data())


# s = Stack()
# top = StackObj("obj_1")
# s.push(top)
# # s.push(StackObj("obj_2"))
# # s.push(StackObj("obj_3"))
# s.pop()

# res = s.get_data()
# assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
# assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

# h = s.top
# while h:
#     res = h.data
#     h = h.next

s = Stack()
top1 = StackObj("obj_1")
top2 = StackObj("obj_2")
top3 = StackObj("obj_3")
s.push(top1)
s.push(top2)
s.push(top3)
pop = s.pop()
print(pop)
print(s)

# assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

# n = 0
# h = s.top
# while h:
#     h = h.next
#     n += 1
    
# assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

# s = Stack()
# top = StackObj("name_1")
# s.push(top)
# obj = s.pop()
# assert obj == top, "метод pop() должен возвращать удаляемый объект"