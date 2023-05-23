from collections import namedtuple
import reprlib

from typing import Union

Pt = Union[int, float]


Point = namedtuple('Point', ['x', 'y'])


class Track:
    def __init__(self, start_x: Pt, start_y: Pt):
        self.start_x = start_x
        self.start_y = start_y
        self.points: list = []

    def add_point(self, x: Pt, y: Pt, speed: Pt):
        self.points.append([Point(x, y), speed])

    def _check_index(self, index):
        if index >= len(self.points):
            raise IndexError('некорректный индекс')

    def __getitem__(self, index):
        self._check_index(index)
        return self.points[index][0], self.points[index][1]

    def __setitem__(self, index, value):
        self._check_index(index)
        self.points[index][1] = value

    def __repr__(self):
        return reprlib.repr(self.points)


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)
