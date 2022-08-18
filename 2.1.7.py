from typing import Tuple

class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__x1 = self.__y1 = self.__x2 = self.__y2 = 0
        self.set_coords(x1, y1, x2, y2)

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self) -> Tuple[int]:
        """для получения кортежа из текущих координат линии"""
        return (self.__x1, self.__y1, self.__x2, self.__y2)

    def draw(self):
        """для отображения в консоли списка текущих координат линии (в одну
        строчку через пробел)
        """
        print(*self.get_coords())


line = Line(1, 2, 3, 4)
line.draw()
