class Cell:
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
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.init()

    def init(self):
        # Game initialization, set all cells to FREE_CELL
        self.pole: tuple = tuple(
            [[Cell() for _ in range(3)] for _ in range(3)]
        )

    def show(self):
        """Visualize the game field. For each empty cell print a dot, for each
        human cell print X, for each computer cell print O."""
        cell: Cell
        lookup = {0: "\u2605", 1: "X", 2: "O"}
        for raw in self.pole:
            for cell in raw:
                print(lookup[cell.value], end=" ")
            print('\n')

    def human_go(self):
        """Ask human to make a move and enter coordinates of the cell."""
        pass

    def __getitem__(self, index: tuple) -> int:
        """Get value of the cell by its coordinates."""
        raw, col = index
        cell: Cell = self.pole[raw][col]
        return cell.value

    def __setitem__(self, index: tuple, value: int) -> None:
        raw, col = index
        cell: Cell = self.pole[raw][col]
        cell.value = value


ss = TicTacToe()
ss.show()
