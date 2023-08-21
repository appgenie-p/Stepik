from typing import Union


class Digit:
    def __init__(self, value: Union[int, float]) -> None:
        if type(value) not in (int, float):
            raise TypeError("значение не соответствует типу объекта")
        self.value = value


class Integer(Digit):
    def __init__(self, value) -> None:
        if type(value) != int:
            raise TypeError("значение не соответствует типу объекта")
        super().__init__(value)


class Float(Digit):
    def __init__(self, value) -> None:
        if type(value) != float:
            raise TypeError("значение не соответствует типу объекта")
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value) -> None:
        if value < 0:
            raise TypeError("значение не соответствует типу объекта")
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value) -> None:
        if value > 0:
            raise TypeError("значение не соответствует типу объекта")
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [
    PrimeNumber(3),
    PrimeNumber(1),
    PrimeNumber(4),
    FloatPositive(1.5),
    FloatPositive(9.2),
    FloatPositive(6.5),
    FloatPositive(3.5),
    FloatPositive(8.9),
]

lst_positive = [obj for obj in digits if isinstance(obj, Positive)]
lst_float = [obj for obj in digits if isinstance(obj, Float)]
