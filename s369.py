from typing import Union

test = False

DimType = Union[int, float]


class Dimensions:
    def __init__(self, a: DimType, b: DimType, c: DimType):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __setattr__(self, name, value):
        if value < 0:
            raise ValueError(
                "габаритные размеры должны быть положительными числами"
            )
        super().__setattr__(name, value)

    def __repr__(self):
        return self.hash()


if test:
    s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"
else:
    s_inp = input()


lst_dims = [
    Dimensions(*(float(x) for x in line.split())) for line in s_inp.split("; ")
]

lst_dims.sort(key=lambda x: hash(x))
