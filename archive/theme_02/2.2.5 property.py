class WindowDlg:
    """
    wnd = WindowDlg(заголовок окна, ширина, высота)
    """

    def __init__(self, title: str, width: int, height: int) -> None:
        self.__title: str = title
        self.__width: int = width
        self.__height: int = height

    def show(self):
        return f"{self.__title}: {self.width}, {self.height}"

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        if isinstance(width, int) and 0 <= width <= 10000:
            self.__width = width
            self.show()

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        if isinstance(height, int) and 0 <= height <= 10000:
            self.__height = height
            self.show()
