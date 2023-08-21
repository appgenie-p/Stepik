"""Description: Tic-tac-toe game."""

import random


class Cell:
    """Класс, описывающий клетку игрового поля."""

    def __init__(self):
        # value - значение поля: 0 - клетка свободна; 1 - стоит крестик; 2 -
        # стоит нолик.
        self.value: int = 0

    def __bool__(self) -> bool:
        # Свободно ли поле?
        return self.value == 0

    def __repr__(self) -> str:
        return f"Cell({self.value})"


class TicTacToe:
    """Класс, описывающий игровое поле."""

    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        # self.pole: Tuple[List[Cell], ...]
        self.init()

    def init(self):
        # Game initialization, set all cells to FREE_CELL
        self.pole = tuple(([Cell() for _ in range(3)] for _ in range(3)))

    @property
    def is_human_win(self) -> bool:
        """
        Check if the human has won the game.
        """
        return self._check_game_result(self.HUMAN_X)

    @property
    def is_computer_win(self) -> bool:
        """
        Check if the computer has won the game.
        """
        return self._check_game_result(self.COMPUTER_O)

    @property
    def is_draw(self) -> bool:
        # check if all the cells are filled, but no one won
        cells_filled: bool = all(
            cell.value != self.FREE_CELL for raw in self.pole for cell in raw
        )
        return cells_filled and not self.is_human_win and not self.is_computer_win

    def _check_game_result(self, mark) -> bool:
        """Check if human won the game."""
        # check rows for HUMAN_X
        for raw in self.pole:
            if all(cell.value == mark for cell in raw):
                return True
        # check columns for HUMAN_X
        for col in range(3):
            if all(self.pole[raw][col].value == mark for raw in range(3)):
                return True
        # check diagonal for HUMAN_X
        if all(self.pole[i][i].value == mark for i in range(3)):
            return True
        if all(self.pole[i][2 - i].value == mark for i in range(3)):
            return True
        return False

    def show(self):
        """Visualize the game field. For each empty cell print a dot, for each
        human cell print X, for each computer cell print O."""
        cell: Cell
        lookup = {0: "\u2605", 1: "X", 2: "O"}
        for raw in self.pole:
            for cell in raw:
                print(lookup[cell.value], end=" ")
            print("\n")

    def human_go(self):
        """Ask human to make a move and enter coordinates of the cell."""
        # ask coordinates, set X to the cell
        input_raw, input_col = map(
            int, input("Введите координаты через пробел: ").split()
        )
        self.pole[input_raw][input_col].value = self.HUMAN_X

    def computer_go(self):
        """Computer makes a move, set O to random empty cell."""
        while True:
            # generate random coordinates
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            cell_value = self.pole[row][col].value
            # check if cell value is 0
            if cell_value == self.FREE_CELL:
                # if empty - set O to the cell and break out of the loop
                self.pole[row][col].value = self.COMPUTER_O
                break

    def __getitem__(self, index: tuple) -> int:
        """Get value of the cell by its coordinates."""
        raw, col = index
        cell: Cell = self.pole[raw][col]
        return cell.value

    def __setitem__(self, index: tuple, value: int) -> None:
        raw, col = index
        cell: Cell = self.pole[raw][col]
        cell.value = value


if __name__ == "__main__":
    cell = Cell()
    assert (
        cell.value == 0
    ), "начальное значение атрибута value объекта класса Cell должно быть равно 0"
    assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
    cell.value = 1
    assert (
        bool(cell) == False
    ), "функция bool для объекта класса Cell вернула неверное значение"

    assert (
        hasattr(TicTacToe, "show")
        and hasattr(TicTacToe, "human_go")
        and hasattr(TicTacToe, "computer_go")
    ), "класс TicTacToe должен иметь методы show, human_go, computer_go"

    game = TicTacToe()
    assert bool(
        game
    ), "функция bool вернула неверное значения для объекта класса TicTacToe"
    assert (
        game[0, 0] == 0 and game[2, 2] == 0
    ), "неверные значения ячеек, взятые по индексам"
    game[1, 1] = TicTacToe.HUMAN_X
    assert (
        game[1, 1] == TicTacToe.HUMAN_X
    ), "неверно работает оператор присваивания нового значения в ячейку игрового поля"

    game[0, 0] = TicTacToe.COMPUTER_O
    assert (
        game[0, 0] == TicTacToe.COMPUTER_O
    ), "неверно работает оператор присваивания нового значения в ячейку игрового поля"

    game.init()
    assert (
        game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL
    ), "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

    try:
        game[3, 0] = 4
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    game.init()
    assert (
        game.is_human_win == False
        and game.is_computer_win == False
        and game.is_draw == False
    ), "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

    game[0, 0] = TicTacToe.HUMAN_X
    game[1, 1] = TicTacToe.HUMAN_X
    game[2, 2] = TicTacToe.HUMAN_X
    assert (
        game.is_human_win and game.is_computer_win == False and game.is_draw == False
    ), "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

    game.init()
    game[0, 0] = TicTacToe.COMPUTER_O
    game[1, 0] = TicTacToe.COMPUTER_O
    game[2, 0] = TicTacToe.COMPUTER_O
    assert (
        game.is_human_win == False and game.is_computer_win and game.is_draw == False
    ), "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
