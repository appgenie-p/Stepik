class Circle:
    def __init__(self, x, y, radius) -> None:
        # self.__x, self.__y, self.__radius = 0, 0, 0
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if isinstance(val, int) or isinstance(val, float):
            self.__x = val
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if isinstance(val, int) or isinstance(val, float):
            self.__y = val
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, val):
        if not (isinstance(val, int) or isinstance(val, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if val >= 0:
            self.__radius = val

    def __getattr__(self, name):
        return False


assert (
    type(Circle.x) == property
    and type(Circle.y) == property
    and type(Circle.radius) == property
), "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

try:
    cr = Circle(20, "7", 22)
except TypeError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

cr = Circle(20, 7, 22)
assert (
    cr.x == 20 and cr.y == 7 and cr.radius == 22
), "объекты-свойства x, y и radius вернули неверные значения"

cr.radius = (
    -10
)  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
assert (
    cr.radius == 22
), "при присваивании некорректного значения, прежнее значение изменилось"

x, y = cr.x, cr.y
assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
assert (
    cr.name == False
), "при обращении к несуществующему атрибуту должно возвращаться значение False"

try:
    cr.x = "20"
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
