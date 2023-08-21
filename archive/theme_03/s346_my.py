from typing import List


class StackObj:
    def __init__(self, data: str) -> None:
        self.__data = data
        self.__next = None

    @property
    def next(self) -> "StackObj":
        return self.__next

    @next.setter
    def next(self, value: "StackObj"):
        self.__next = value


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push_back(self, obj: StackObj) -> None:
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.next = obj

    def pop_back(self) -> None:
        if self.top is None:
            return None
        elif self.top.next is None:
            self.top = None
        else:
            current = self.top
            while current.next.next is not None:
                current = current.next
            current.next = None

    def __add__(self, new_obj: StackObj) -> "Stack":
        self.push_back(new_obj)
        return self

    def __iadd__(self, new_obj: StackObj) -> "Stack":
        self.__add__(new_obj)
        return self

    def __mul__(self, values: List[str]) -> "Stack":
        for value in values:
            self.push_back(StackObj(value))
        return self

    def __imul__(self, values: List[str]) -> "Stack":
        self.__mul__(values)
        return self


assert hasattr(Stack, "pop_back"), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ["data_1", "data_2"]
st *= ["data_3", "data_4"]

d = ["1", "2", "3", "4", "data_1", "data_2", "data_3", "data_4"]
h = top
i = 0
while h:
    assert (
        h._StackObj__data == d[i]
    ), "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
