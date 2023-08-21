import inspect
import numbers
from typing import Optional


class StackObj:
    __slots__ = ("data", "next")

    def __init__(self, data: str):
        self.data: str = data
        self.next: Optional["StackObj"] = None

    def __repr__(self):
        return f"StackObj({self.data})"


class Stack:
    __slots__ = ("top", "_size")

    def __init__(self):
        self.top = None
        self._size = 0

    def _check_index(self, index):
        calling_function = inspect.stack()[1].function
        stack_length = len(self) - 1 if calling_function == "__getitem__" else len(self)
        if not isinstance(index, numbers.Integral) or index < 0 or index > stack_length:
            raise IndexError("неверный индекс")

    def push(self, data: StackObj):
        if not isinstance(data, StackObj):
            raise ValueError("возможны только объекты StackObj")
        self[len(self)] = data
        self._size += 1

    def pop(self) -> StackObj:
        if not self.top:
            raise IndexError("стек пуст")
        last_index = len(self) - 1
        data = self[last_index]
        self[last_index - 1].next = None
        self._size -= 1
        return data

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.top
        while current:
            yield current
            current = current.next

    def __getitem__(self, index: int) -> StackObj:
        self._check_index(index)
        current = self.top
        for _ in range(index):
            current = current.next
        return current

    def __setitem__(self, index: int, data: StackObj):
        self._check_index(index)
        if index == 0 and not getattr(self.top, "next", None):
            self.top = data
        elif index == 0:
            data.next = self.top.next
            self.top = data
        else:
            previous = self[index - 1]
            if getattr(previous.next, "next", None):
                data.next = getattr(previous.next, "next")
            previous.next = data


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
obj = st[2]
st[1] = StackObj("obj2-new")
assert (
    st[0].data == "obj11" and st[1].data == "obj2-new"
), "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert (
    obj.data == "obj13"
), "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(
        h, StackObj
    ), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
