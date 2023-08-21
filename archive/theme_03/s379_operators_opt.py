import operator as op


class Vector:
    def __init__(self, *args):
        self.args = args

    def main_exec(self, other, func, new_obj=True):
        self.check_len(other)
        # для каждого элемента вектора применяем функцию func
        new_tuple = [func(a, b) for a, b in zip(self.args, other.args)]
        if new_obj:
            return Vector(*new_tuple)
        else:
            self.args = new_tuple

    def __add__(self, other):
        return self.main_exec(other, op.add)

    def __sub__(self, other):
        return self.main_exec(other, op.sub)

    def __mul__(self, other):
        return self.main_exec(other, op.mul)

    def __iadd__(self, other):
        return self.main_exec(other, op.add, False)

    def __isub__(self, other):
        return self.main_exec(other, op.sub, False)

    def __imul__(self, other):
        return self.main_exec(other, op.mul, False)

    def __len__(self):
        return len(self.args)

    def __str__(self) -> str:
        return str(self.args)

    def check_len(self, other):
        if len(self) != len(other):
            raise ArithmeticError("размерности векторов не совпадают")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.args == other.args
        raise TypeError("Сравнение векторов не возможно!")


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2))  # [5, 7, 9]
# print((v1 - v2))  # [-3, -3, -3]
# print((v1 * v2))  # [4, 10, 18]

# v1 += 10
# print(v1)  # [11, 12, 13]
# v1 -= 10
# print(v1)  # [1, 2, 3]
# v1 += v2
# print(v1)  # [5, 7, 9]
# v2 -= v1
# print(v2)  # [-1, -2, -3]

# print(v1 == v2)  # False
# print(v1 != v2)  # True
