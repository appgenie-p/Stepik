from random import randint


class GamePole:
    """
    Cоздание и управление игровым полем.

    Каждая клетка игрового поля представлена объектом класса Cell и содержать
    либо число мин вокруг этой клетки, либо саму мину.
    """

    def __new__(cls, *args, **kwargs):
        """
        Возвращает ссылку на единственный экземпляр класса GamePole.
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(GamePole, cls).__new__(cls)
        return cls.instance

    def __del__(self):
        """
        Удаляет ссылку на единственный экземпляр класса GamePole.
        """
        GamePole.instance = None

    def __init__(self, N: int, M: int, total_mines: int) -> None:
        """
        Initialize attributes.
        """
        self.__N = N
        self.__M = M
        self.__total_mines = total_mines

        # __pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов
        # (N строк и M столбцов), состоящий из объектов класса Cell.
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.init_pole()

    @property
    def pole(self) -> tuple:
        """
        Возвращает игровое поле.
        """
        return self.__pole_cells

    def init_pole(self) -> None:
        """
        Для инициализации начального состояния игрового поля (расставляет мины
        и делает все клетки закрытыми).
        После расстановки всех total_mines мин, вычислите их количество вокруг
        остальных клеток (где нет мин). Область охвата - соседние (прилегающие)
        клетки (8 штук).
        """
        installed_mines_counter = self.__total_mines
        while installed_mines_counter > 0:
            i = randint(0, self.__N - 1)
            j = randint(0, self.__M - 1)
            if not self.__pole_cells[i][j].is_mine:
                self.__pole_cells[i][j].is_mine = True
                installed_mines_counter -= 1

        # Для каждой клетки, где нет мин, вычисляем количество мин вокруг
        # этой клетки и записываем в аттрибут number объекта Cell.
        for i in range(self.__N):
            for j in range(self.__M):
                if not self.__pole_cells[i][j].is_mine:
                    self.__pole_cells[i][j].number = self.count_mines(i, j)

    def count_mines(self, i: int, j: int) -> int:
        """
        Возвращает количество мин вокруг клетки с индексами (i, j);
        нумерация индексов начинается с нуля.
        """
        mines_counter = 0
        for x in range(max(0, i - 1), min(self.__N, i + 2)):
            for y in range(max(0, j - 1), min(self.__M, j + 2)):
                if self.__pole_cells[x][y].is_mine:
                    mines_counter += 1
        return mines_counter

    def open_cell(self, i: int, j: int) -> None:
        """
        Открывает ячейку с индексами (i, j); нумерация индексов начинается с
        нуля;
        метод меняет значение атрибута __is_open объекта Cell в
        ячейке (i, j) на True;

        В методе open_cell() необходимо проверять корректность индексов (i, j).
        Если индексы указаны некорректно, то генерируется исключение командой:
        raise IndexError('некорректные индексы i, j клетки игрового поля')
        """
        if i < 0 or i >= self.__N or j < 0 or j >= self.__M:
            raise IndexError("некорректные индексы i, j клетки игрового поля")
        self.__pole_cells[i][j].is_open = True

    def show_pole(self) -> None:
        """
        Отображает игровое поле в консоли (как именно сделать - придумайте).
        """
        for i in range(self.__N):
            for j in range(self.__M):
                if self.__pole_cells[i][j].is_open:
                    print(self.__pole_cells[i][j].number, end=" ")
                else:
                    print("*", end=" ")
            print()


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
        self.__is_mine = False
        #  число мин вокруг клетки (целое число от 0 до 8).
        self.__number = 0
        #  флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
        self.__is_open = False

    @property
    def is_mine(self) -> bool:
        """
        Для чтения информации из атрибута __is_mine;
        """
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool) -> None:
        """
        Для записи информации в атрибут __is_mine;
        """
        self.check_value_bool(value)
        self.__is_mine = value

    @property
    def number(self) -> int:
        """
        Для чтения информации из атрибута __number attribute.
        """
        return self.__number

    @number.setter
    def number(self, value: int) -> None:
        """
        Для записи информации в атрибут __number attribute.
        """
        self.check_value_int(value)
        self.__number = value

    @property
    def is_open(self) -> bool:
        """
        Для чтения информации из атрибута __is_open attribute.
        """
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool) -> None:
        """
        Для записи информации в атрибут __is_open attribute.
        """
        self.check_value_bool(value)
        self.__is_open = value

    def __bool__(self) -> bool:
        """
        True, если клетка закрыта и False - если открыта.
        """
        return not self.is_open

    def __str__(self) -> str:
        """
        Возвращает строку, описывающую состояние ячейки.
        """
        if self.is_open:
            return str(self.number)
        else:
            return "*"

    def check_value_bool(self, value: bool) -> bool:
        """
        Проверяет, является ли переданное значение булевым.
        """
        if not isinstance(value, bool):
            raise ValueError("Недопустимое значение атрибута")
        return value

    def check_value_int(self, value: int) -> int:
        """
        Проверяет, является ли переданное значение целым числом от 0 до 8.
        """
        if not isinstance(value, int) or value < 0 or value > 8:
            raise ValueError("Недопустимое значение атрибута")
        return value


# Пример использования классов:
# создается поле размерами 10x20 с общим числом мин 10
pole = GamePole(10, 20, 10)
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.show_pole()
# pole.open_cell(30, 100)  # генерируется исключение IndexError
