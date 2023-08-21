from typing import Union, Tuple


class RadiusVector:
    """RadiusVector.
    vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0
    (аргумент - целое число больше 1)
    vector = RadiusVector(1, -5, 3.4, 10)
    (координаты - любые целые или вещественные числа)
    """

    Coord = Union[int, float]

    def __init__(self, *args: Coord) -> None:
        len_args = len(args)
        first_arg = args[0]
        if len_args == 1 and (first_arg < 1 or type(first_arg) != int):
            raise Exception("Единственны аргумент д.б. int и больше 0")
        self.coords = [0] * first_arg if len_args == 1 else [coord for coord in args]

    def set_coords(self, *coord):
        self.coords = list(coord[: len(self.coords)]) + self.coords[len(coord) :]

    def get_coords(self) -> Tuple[Coord, ...]:
        """для получения текущих координат радиус-вектора (в виде кортежа)"""
        return tuple(self.coords)

    def __abs__(self) -> float:
        """возвращает длину радиус-вектора.
        (вычисляется как:
        sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N)
             - корень квадратный из суммы квадратов координат).
        """
        return sum(i**2 for i in self.coords) ** 0.5

    def __len__(self) -> int:
        """возвращает число координат радиус-вектора (его размерность)"""
        return len(self.coords)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(
    3, -5.6, 8, 10, 11
)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(
    1, 2
)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
