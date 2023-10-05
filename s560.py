import random
from enum import Enum
from typing import List, NamedTuple, Optional, Set, Tuple, cast


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
        self._cells[key] = Hit(value)

    def __getitem__(self, key: int) -> int:
        return self._cells[key]

    @property
    def cells_around(self) -> Set[Coords]:
        """Get set of cell's coordinates around ship"""
        return {
            Coords(coord.x + i, coord.y + j)
            for coord in self.cells
            for i in range(-1, 2)
            for j in range(-1, 2)
            if not (i == 0 and j == 0)
        } - self.cells

    @property
    def cells(self) -> Set[Coords]:
        """
        Returns a set of coordinates representing the cells occupied by the
        ship.
        """
        if self.direction.name == "horizontal":
            return {Coords(self.x + x, self.y) for x in range(self._length)}
        return {Coords(self.x, self.y + y) for y in range(self._length)}

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
    def direction(self) -> Direction:
        return Direction(self._tp)

    @direction.setter
    def direction(self, tp: int) -> None:
        if tp not in (1, 2):
            raise ValueError("tp must be 1 or 2")
        self._tp = tp

    @property
    def cells_condition(self) -> List[Hit]:
        return self._cells

    @property
    def is_moveable(self) -> bool:
        return self._is_move

    def set_start_coords(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def get_start_coords(self) -> Coords:
        return Coords(self.x, self.y)

    def move(self, go: int) -> None:
        self._check_go_value(go)
        self._check_ship_initialized()
        self.move_ship(go)

    def _check_ship_initialized(self):
        if self._x is None or self._y is None:
            raise ValueError("Ship is not initialized")

    def _check_go_value(self, go: int):
        if go not in (1, -1):
            raise ValueError("go must be 1 or -1")

    def move_ship(self, go: int) -> None:
        if self.is_moveable:
            if self.direction.name == "horizontal":
                self._x += go  # type: ignore
            elif self.direction.name == "vertical":
                self._y += go  # type: ignore

    def is_collide(self, other: "Ship") -> bool:
        """
        Check if the current ship collides with another ship.
        True if the ships collide, False otherwise.
        """
        return bool(self.cells_around.intersection(other.cells))

    def is_out_pole(self, size: int = 10) -> bool:
        return any(
            coord.x < 0 or coord.y < 0 or coord.x >= size or coord.y >= size
            for coord in self.cells
        )


class GamePole:
    def __init__(self, size: int = 10):
        self._size = size
        self._ships: List[Ship] = []

    def init(self):
        """
        Initializes the class by creating a fleet of ships with decreasing deck
        sizes from 4 to 1.
        """
        [
            [self._set_ship(deck_size) for _ in range(ship_number)]
            for ship_number, deck_size in enumerate(range(4, 0, -1), 1)
        ]

    def _set_ship(self, deck_size: int):
        ship = Ship(deck_size)
        while True:
            ship.direction = cast(Direction, random.randint(1, 2))
            ship.x = random.randint(0, self._size - 1)
            ship.y = random.randint(0, self._size - 1)
            if not ship.is_out_pole(self._size) and not any(
                ship.is_collide(other) for other in self._ships
            ):
                break
        self._ships.append(ship)
        return ship

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            original_coords = ship.x, ship.y
            first_try = random.choice((-1, 1))
            if self._moved(ship, original_coords, first_try):
                continue
            second_try = -first_try
            if self._moved(ship, original_coords, second_try):
                continue
            ship.x, ship.y = original_coords

    def _moved(
        self, ship: Ship, original_coords: Tuple[int, int], move_len: int
    ) -> bool:
        ship.move(move_len)
        if ship.is_out_pole(self._size) or any(
            ship.is_collide(other) for other in self._ships
        ):
            return False
        return True

    def get_pole(self) -> Tuple[Tuple[str, ...], ...]:
        pole = [["0"] * self._size for _ in range(self._size)]
        for ship in self._ships:
            for coord, cell in zip(ship.cells, ship.cells_condition):
                pole[coord.x][coord.y] = "2" if cell == Hit.hit else "1"
        return tuple(tuple(row) for row in pole)

    def show(self) -> None:
        pole = self.get_pole()
        for row in pole:
            print(" ".join(row))
