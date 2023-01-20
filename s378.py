class GamePole:
    """
    Cоздание и управление игровым полем.

    Нужно контролировать создание только одного объекта класса GamePole
    (используйте паттерн Singleton и  магический метод __new__()).

    Каждая клетка игрового поля представлена объектом класса Cell и содержать 
    либо число мин вокруг этой клетки, либо саму мину.
    """

    def __init__(self, N: int, M: int, total_mines: int) -> None:
        """
        Initialize attributes.
        """
        self.__N = N
        self.__M = M
        self.__total_mines = total_mines
        # __pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов
        # (N строк и M столбцов), состоящий из объектов класса Cell.
        self.__pole_cells = tuple(tuple(Cell()
                                  for _ in range(M)) for _ in range(N))

    @property
    def pole(self) -> tuple:
        """
        Return a copy of the __pole_cells tuple.
        """
        return self.__pole_cells

    def init_pole(self) -> None:
        """
        Для инициализации начального состояния игрового поля (расставляет мины
        и делает все клетки закрытыми).

        Расстановку мин выполняйте случайным образом по игровому полю (для этого 
        удобно воспользоваться функцией randint модуля random). После расстановки
        всех total_mines мин, вычислите их количество вокруг остальных клеток
        (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).
        """
        pass

    def open_cell(self, i: int, j: int) -> None:
        """
        Открывает ячейку с индексами (i, j); нумерация индексов начинается с
        нуля; метод меняет значение атрибута __is_open объекта Cell в
        ячейке (i, j) на True;

        В методе open_cell() необходимо проверять корректность индексов (i, j).
        Если индексы указаны некорректно, то генерируется исключение командой:
        raise IndexError('некорректные индексы i, j клетки игрового поля')
        """
        pass

    def show_pole(self) -> None:
        """
        Отображает игровое поле в консоли (как именно сделать - придумайте).
        """
        pass


class Cell:
    """
    Cell описывает состояние одной ячейки игрового поля. 
    Объекты этого класса создаются командой: Cell()

    """

    def __init__(self) -> None:
        """
        Initialize attributes.
        """
        # булево значение True/False; True - в клетке находится мина,
        # False - мина отсутствует.
        self.__is_mine = None
        #  число мин вокруг клетки (целое число от 0 до 8).
        self.__number = None
        #  флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
        self.__is_open = None

    # В этих свойствах необходимо выполнять проверку на корректность переданных
    # значений (либо булево значение True/False, либо целое число от 0 до 8).
    # Если передаваемое значение некорректно, то генерировать исключение командой:
    # raise ValueError("недопустимое значение атрибута")
    @property
    def is_mine(self) -> bool:
        """
        Для чтения информации из атрибута __is_mine;
        """
        pass

    @is_mine.setter
    def is_mine(self, value: bool) -> None:
        """
        Для записи информации в атрибут __is_mine;
        """
        pass

    @property
    def number(self) -> int:
        """
        Для чтения информации из атрибута __number attribute.
        """
        pass

    @number.setter
    def number(self, value: int) -> None:
        """
        Для записи информации в атрибут __number attribute.
        """
        pass

    @property
    def is_open(self) -> bool:
        """
        Для чтения информации из атрибута __is_open attribute.
        """
        pass

    @is_open.setter
    def is_open(self, value: bool) -> None:
        """
        Для записи информации в атрибут __is_open attribute.
        """
        pass

    def __bool__(self) -> bool:
        """
        True, если клетка закрыта и False - если открыта.
        """
        pass


# Пример использования классов:
# создается поле размерами 10x20 с общим числом мин 10
pole = GamePole(10, 20, 10)
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
