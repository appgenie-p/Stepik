class Ellipse:
    """Ellipse class"""

    def __init__(self,*args):
        """Initialize attributes"""
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self) -> bool:
        """Return True if all attributes are non-zero"""
        return bool(self.__dict__)

    def get_coords(self) -> tuple:
        if not self:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]

for geom in lst_geom:
    if geom:
        geom.get_coords()
