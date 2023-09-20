from typing import Union

Number = Union[int, float]


class Star:
    __slots__ = ("_name", "_massa", "_temp")

    def __init__(self, name: str, massa: Number, temp: Number) -> None:
        self._name = name
        self._massa = massa
        self._temp = temp


class ExtStar(Star):
    __slots__ = ("_type_star", "_radius")

    def __init__(
        self,
        name: str,
        massa: Number,
        temp: Number,
        type_star: str,
        radius: Number,
    ) -> None:
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class WhiteDwarf(ExtStar):
    __slots__ = ()


class YellowDwarf(ExtStar):
    __slots__ = ()


class RedGiant(ExtStar):
    __slots__ = ()


class Pulsar(ExtStar):
    __slots__ = ()


stars = [
    RedGiant("Альдебаран", 5, 3600, "красный гигант", 45),
    WhiteDwarf("Сириус А", 2.1, 9250, "белый карлик", 2),
    WhiteDwarf("Сириус B", 1, 8200, "белый карлик", 0.01),
    YellowDwarf("Солнце", 1, 6000, "желтый карлик", 1),
]

white_dwarfs = [star for star in stars if isinstance(star, WhiteDwarf)]
