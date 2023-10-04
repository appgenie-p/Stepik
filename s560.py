from enum import Enum
from typing import List, NamedTuple, Optional, Set


class Direction(int, Enum):
    horizontal = 1
    vertical = 2


class Coords(NamedTuple):
    x: int
    y: int


class Hit(int, Enum):
    intact = 1
    hit = 2


class Ship:
    def __init__(
        self,
        length: int,
        tp: int = 1,
        x: Optional[int] = None,
        y: Optional[int] = None,
    ):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [Hit.intact] * length

    def __setitem__(self, key: int, value: int) -> None:
        if value not in (1, 2):
            raise ValueError("value must be 1 or 2")
        self._cells[key] = Hit.intact if value == 1 else Hit.hit

    def __getitem__(self, key: int) -> int:
        return self._cells[key]

    @property
    def around(self) -> Set[Coords]:
        if self.tp == "horizontal":
            return self._around_horizontal_ship()
        return self._around_vertical_ship()

    def _around_vertical_ship(self) -> Set[Coords]:
        above = {Coords(self.coords_init.x, self.coords_init.y - 1)}
        below = {Coords(self.coords_init.x, self.coords_init.y + self.length)}
        left = {
            Coords(self.coords_init.x - 1, self.coords_init.y + y)
            for y in range(-1, self.length + 1)
        }
        right = {
            Coords(self.coords_init.x + 1, self.coords_init.y + y)
            for y in range(-1, self.length + 1)
        }
        return above.union(below, left, right)

    def _around_horizontal_ship(self) -> Set[Coords]:
        above = {
            Coords(self.coords_init.x + x, self.coords_init.y - 1)
            for x in range(-1, self.length + 1)
        }
        below = {
            Coords(self.coords_init.x + x, self.coords_init.y + 1)
            for x in range(-1, self.length + 1)
        }
        left = {Coords(self.coords_init.x - 1, self.coords_init.y)}
        right = {Coords(self.coords_init.x + self.length, self.coords_init.y)}
        return above.union(below, left, right)

    @property
    def coords(self) -> Set[Coords]:
        if self.tp == "horizontal":
            return {
                Coords(self.coords_init.x + x, self.coords_init.y)
                for x in range(self.length)
            }
        return {
            Coords(self.coords_init.x, self.coords_init.y + y)
            for y in range(self.length)
        }

    @property
    def coords_init(self) -> Coords:
        if self._x is None or self._y is None:
            raise ValueError("Ship is not initialized")
        return Coords(self._x, self._y)

    @property
    def x(self) -> int:
        if self._x is None:
            raise ValueError("Ship is not initialized")
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self._x = x

    @property
    def y(self) -> int:
        if self._y is None:
            raise ValueError("Ship is not initialized")
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        self._y = y

    @property
    def tp(self) -> str:
        return Direction(self._tp).name

    @property
    def length(self) -> int:
        return self._length

    @property
    def cells(self) -> List[Hit]:
        return self._cells

    @property
    def is_move(self) -> bool:
        return self._is_move

    def set_start_coords(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def get_start_coords(self) -> Coords:
        return self.coords_init

    def move(self, go: int) -> None:
        self.check_go_value(go)
        self.check_ship_initialized()
        self.move_ship(go)

    def check_ship_initialized(self):
        if self._x is None or self._y is None:
            raise ValueError("Ship is not initialized")

    def check_go_value(self, go: int):
        if go not in (1, -1):
            raise ValueError("go must be 1 or -1")

    def move_ship(self, go: int) -> None:
        if self.is_move:
            if self.tp == "horizontal":
                self._x += go  # type: ignore
            elif self.tp == "vertical":
                self._y += go  # type: ignore

    def is_collide(self, other: "Ship") -> bool:
        return bool(self.around.intersection(other.coords))

    def is_out_pole(self, size: int = 10) -> bool:
        for coord in self.coords:
            if (
                coord.x < 0
                or coord.y < 0
                or coord.x >= size
                or coord.y >= size
            ):
                return True
        return False


class GamePole:
    pass
