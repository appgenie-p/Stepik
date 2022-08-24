class TelecastDescriptor:
    def __set_name__(self, obj, name):
        self.name = "_" + name

    def __set__(self, obj, val):
        setattr(obj, self.name, val)

    def __get__(self, obj, type=None):
        return getattr(obj, self.name)


class Telecast:
    id = TelecastDescriptor()
    name = TelecastDescriptor()
    duration = TelecastDescriptor()

    def __init__(self, uid: int, name: str, duration: int) -> None:
        self.id = uid
        self.name = name
        self.duration = duration


class TVProgram:
    def __init__(self, name: str) -> None:
        self.name = name
        self.items: list[Telecast] = []

    def add_telecast(self, tl: Telecast) -> None:
        self.items.append(tl)

    def remove_telecast(self, indx: int) -> None:
        items_for_del = (x for x in self.items if x.id == indx)
        if items_for_del:
            self.items.remove(next(items_for_del))


assert hasattr(TVProgram, 'add_telecast') and hasattr(TVProgram, 'remove_telecast'), "в классе TVProgram должны быть методы add_telecast и remove_telecast"

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(3, "Новости", 2000))
t = Telecast(2, "Интервью с Балакиревым", 20)
pr.add_telecast(t)

pr.remove_telecast(3)
assert len(pr.items) == 2, "неверное число телеперач, возможно, некорректно работает метод remove_telecast"
assert pr.items[-1] == t, "удалена неверная телепередача (возможно, вы удаляете не по __id, а по порядковому индексу в списке items)"
