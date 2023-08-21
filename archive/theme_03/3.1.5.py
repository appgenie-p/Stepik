class LessonItem:
    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, val) -> None:
        val_type = self.__init__.__annotations__.get(key)
        if isinstance(val, val_type):
            if (key == "practices" or key == "duration") and val <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                super().__setattr__(key, val)
                return
        raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, key):
        return False

    def __delattr__(self, __name: str) -> None:
        keys = ("title", "practices", "duration")
        if __name in keys:
            return
        super().__delattr__(__name)


class Module:
    def __init__(self, name):
        self.name: str = name
        self.lessons: list[LessonItem] = []

    def add_lesson(self, lesson: LessonItem) -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:
    def __init__(self, name):
        self.name: str = name
        self.modules: list[Module] = []

    def add_module(self, module: Module) -> None:
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
