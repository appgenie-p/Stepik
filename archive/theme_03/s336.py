class ComplexNumberDescr:
    def __set_name__(self, obj, name):
        self.name = f"_{obj.__name__}__" + name

    def __set__(self, obj, val):
        if isinstance(val, (int, float)):
            setattr(obj, self.name, val)
        else:
            raise ValueError("Неверный тип данных.")

    def __get__(self, obj, type=None):
        if obj is None:
            return property()
        return getattr(obj, self.name)


class Complex:
    real = ComplexNumberDescr()
    img = ComplexNumberDescr()

    def __init__(self, real, img) -> None:
        self.real = real
        self.img = img

    def __abs__(self):
        return (self.real**2 + self.img**2) ** 0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)


print(type(Complex.real))
assert (
    type(Complex.real) == property and type(Complex.img) == property
), "в классе Complex должны быть объявлены объекты-свойства real и img"
