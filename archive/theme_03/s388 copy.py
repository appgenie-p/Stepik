class Cell:
    def __init__(self):
        # True, если клетка свободна; False в противном случае;
        self.is_free = True
        # value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).
        self.value = 0

    def __bool__(self):
        # Возвращает значение поля is_free.
        return self.is_free

    def __repr__(self):
        return f"Cell({self.value}, {self.is_free})"


class TicTacToe:
    # pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.
    def __init__(self):
        self.pole = tuple([[Cell() for col in range(3)] for raw in range(3)])

    def clear(self):
        for raw in range(3):
            for col in range(3):
                self.pole[raw][col].is_free = True
                self.pole[raw][col].value = 0

    def __getitem__(self, index):
        cell = self.pole[index[0]][index[1]]
        if isinstance(index[1], slice):
            return tuple([item.value for item in cell])
        if isinstance(index[0], slice):
            return tuple(
                [item[index[1]].value for item in self.pole[index[0]]]
            )
        return cell.value

    def __setitem__(self, index, value):
        cell = self.pole[index[0]][index[1]]
        if cell.value != 0:
            raise IndexError("летка уже занята")
        cell.value = value
        cell.is_free = False

