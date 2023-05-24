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
        if isinstance(index, slice):
            return tuple([self.pole[index[0]][i].value for i in range(3)])
        return self.pole[index[0]][index[1]].value

    def __setitem__(self, index, value):
        self.pole[index[0]][index[1]].value = value
        self.pole[index[0]][index[1]].is_free = False


g = TicTacToe()
g.clear()
assert (
    g[0, 0] == 0 and g[2, 2] == 0
), "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert (
    g[1, 1] == 1 and g[2, 1] == 2
), "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"


try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


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
