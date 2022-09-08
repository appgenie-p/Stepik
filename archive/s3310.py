from typing import List, Tuple

Coord = Tuple[int, int]


class PolyLine:
    def __init__(self, *args: Coord) -> None:
        self.polyline = list(args)

    def add_coord(self, x: int, y: int) -> None:
        self.polyline.append((x, y))

    def remove_coord(self, indx: int):
        try:
            self.polyline.pop(indx)
        except IndexError:
            pass

    def get_coords(self) -> List[Coord]:
        return self.polyline
