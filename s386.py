import numbers
from typing import Optional


class StackObj:
    __slots__ = ('data', 'next')

    def __init__(self, data: str):
        self.data: str = data
        self.next: Optional['StackObj'] = None

    def __repr__(self):
        return f'StackObj({self.data})'


class Stack:
    __slots__ = ('top', '_size')

    def __init__(self):
        self.top = None
        self._size = 0

    @staticmethod
    def _check_data(data):
        if not isinstance(data, StackObj):
            raise ValueError('возможны только объекты StackObj')

    def _check_top(self):
        if not self.top:
            raise IndexError('стек пуст')

    def _check_index(self, index):
        if (
            not isinstance(index, numbers.Integral)
            or index < 0
            or index >= len(self)
        ):
            raise IndexError('неверный индекс')

    def _get_by_index(self, index):
        self._check_index(index)
        self._check_top()
        current = self.top
        for _ in range(index):
            current = current.next
        return current

    def push(self, data: StackObj):
        self._check_data(data)
        self[len(self)] = data
        self._size += 1

    def pop(self) -> StackObj:
        last_element = len(self) - 1
        data = self[last_element]
        self[last_element - 1].next = None
        self._size -= 1
        return data

    def __len__(self):
        return self._size

    def __iter__(self):
        self._check_top()
        current = self.top
        while current:
            yield current
            current = current.next

    def __getitem__(self, index: int) -> StackObj:
        current = self._get_by_index(index)
        return current

    def __setitem__(self, index: int, data: StackObj):
        self._check_data(data)
        # If it's first object and there is no next object
        if index == 0 and not getattr(self.top, 'next', None):
            self.top = data
        # If it's first object and there is next object
        elif index == 0:
            data.next = self.top.next
            self.top = data
        else:
            previous = self._get_by_index(index - 1)
            if getattr(previous.next, 'next', None):
                data.next = previous.next.next
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

assert (
    n == 2
), "неверное число объектов в стеке (возможно, нарушена его структура)"
