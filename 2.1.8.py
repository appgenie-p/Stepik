class Point:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def get_coords(self) -> tuple:
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, *args) -> None:

        if all(isinstance(i, Point) for i in args) and len(args) == 2:
            self.set_coords(*args)

        if all(isinstance(i, int) for i in args) and len(args) == 4:
            x1, y1, x2, y2 = args
            self.set_coords(Point(x1, y1), Point(x2, y2))

    def set_coords(self, sp: Point, ep: Point) -> None:
        self.__sp = sp
        self.__ep = ep

    def get_coords(self) -> None:
        return (self.__sp, self.__ep)

    def draw(self):
        print(
            f'Прямоугольник с координатами: {self.__sp.get_coords()}'
            f' {self.__ep.get_coords()}'
        )


rect = Rectangle(Point(0, 0), Point(20, 34))
