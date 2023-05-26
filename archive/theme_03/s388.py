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
        raw, col = index
        cell = self.pole[raw][col]
        if isinstance(col, slice):
            return tuple([item.value for item in cell])
        if isinstance(raw, slice):
            return tuple([item[col].value for item in self.pole[raw]])
        return cell.value

    def __setitem__(self, index, value):
        raw, col = index
        cell = self.pole[raw][col]
        if cell.value != 0:
            raise IndexError("клетка уже занята")
        cell.value = value
        cell.is_free = False


g = TicTacToe()

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3


assert (
    g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3)
), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert (
    cell.value == 0
), "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
