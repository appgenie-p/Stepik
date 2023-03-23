# Объявим два класса:
# Stack - для управления односвязным списком в целом;
# StackObj - для представления отдельных объектов в односвязным списком.

# Объекты класса StackObj должны создаваться командой:
# obj = StackObj(data)
# где data - строка с некоторыми данными.

# Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
# __data - ссылка на строку с переданными данными;
# __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

# Объекты класса Stack создаются командой:
# st = Stack()
# и каждый из них должен содержать локальный атрибут:
# top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

# Также в классе Stack следует объявить следующие методы:
# push_back(self, obj) - добавление объекта класса StackObj в конец
# односвязного списка;
# pop_back(self) - удаление последнего объекта из односвязного списка.

# Дополнительно нужно реализовать следующий функционал (в этих операциях копии
# односвязного списка создавать не нужно):
# # добавление нового объекта класса StackObj в конец односвязного списка st
# st = st + obj
# st += obj
# # добавление нескольких объектов в конец односвязного списка
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']

# В последних двух строчках должны автоматически создаваться N объектов класса
# StackObj с данными, взятыми из списка (каждый элемент списка для очередного
# добавляемого объекта).


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.next = obj

    def pop_back(self):
        if self.top is None:
            return None
        elif self.top.next is None:
            self.top = None
        else:
            current = self.top
            while current.next.next is not None:
                current = current.next
            current.next = None

    def __add__(self, obj):
        self.push_back(obj)
        return self

    def __iadd__(self, obj):
        self.push_back(obj)
        return self

    def __mul__(self, lst):
        for i in lst:
            self.push_back(StackObj(i))
        return self

    def __imul__(self, lst):
        for i in lst:
            self.push_back(StackObj(i))
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
