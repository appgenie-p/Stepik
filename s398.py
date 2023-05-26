from typing import Optional


class StackObj:
    __slots__ = ('data', 'next')

    def __init__(self, data: str):
        self.data: str = data
        self.next: Optional['StackObj'] = None

    def __repr__(self):
        return f'StackObj({self.data})'


class Stack:
    __slots__ = ('top',)

    def __init__(self):
        self.top = None

    def push_back(self, data: StackObj) -> None:
        """Add object to the end of stack"""
        if not self.top:
            self.top = data
            return
        last_index = len(self) - 1
        self._get_object_by_index(last_index).next = data

    def push_front(self, data: StackObj) -> None:
        """Add object to the begin of stack"""
        data.next = self.top
        self.top = data

    def _get_object_by_index(self, index):
        if type(index) != int or not 0 <= index < len(self):
            raise IndexError('индекс выходит за пределы стека')
        current = self.top
        for _ in range(index):
            current = current.next
        return current

    def __len__(self):
        return sum(1 for _ in self)

    def __iter__(self):
        current = self.top
        while current:
            yield current
            current = current.next

    def __getitem__(self, index: int) -> StackObj:
        return self._get_object_by_index(index).data

    def __setitem__(self, index: int, data: str) -> None:
        self._get_object_by_index(index).data = data


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
st.push_back(StackObj("3"))

assert (
    st[0] == "2" and st[1] == "1"
), "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert (
    st[0] == "0"
), "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(
        obj, StackObj
    ), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
