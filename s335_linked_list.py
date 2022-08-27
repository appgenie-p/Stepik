class ObjDataDescriptor:
    def __set_name__(self, obj, name):
        self.name = f'_{obj.__name__}__' + name

    def __set__(self, obj, val):
        setattr(obj, self.name, val)

    def __get__(self, obj, type=None):
        return getattr(obj, self.name)        


class ObjList:
    data = ObjDataDescriptor()
    prev = ObjDataDescriptor()
    next = ObjDataDescriptor()

    def __init__(self, data: str) -> None:
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        return f'Obj: {self.data}'


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head = self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx: int):
        if indx == 0:
            self.head = self.tail = None
            return
        iter_obj = self.iter_linked_list()
        for _ in range(indx):
            obj = next(iter_obj)
        obj.next = None
        self.tail = obj

    def iter_linked_list(self) -> ObjList:
        obj = self.head
        while obj:
            yield obj
            obj = obj.next

    def __len__(self) -> int:
        return len(list(self.iter_linked_list()))

    def __call__(self, indx: int):
        iter_obj1 = self.iter_linked_list()
        for _ in range(indx+1):
            obj = next(iter_obj1)
        return obj.data


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"

ln.remove_obj(0)