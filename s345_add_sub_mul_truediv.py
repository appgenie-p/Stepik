from typing import List, Sequence, Union


class ListMath:
    Term = Union[int, float]
    Values = List[Term]

    def __init__(self, init_values: Sequence = []) -> None:
        self.__init_values = [
            val for val in init_values
            if type(val) == int or type(val) == float]

    @property
    def lst_math(self) -> Values:
        return self.__init_values

    @staticmethod
    def __check(var: Term) -> None:
        if not (type(var) == int or type(var) == float):
            raise ArithmeticError('Ошибка данных')

    def __add__(self, second_term: Term) -> Values:
        self.__check(second_term)
        return ListMath([val + second_term for val in self.__init_values])

    def __radd__(self, first_term: Term) -> Values:
        self.__check(first_term)
        return self + first_term

    def __iadd__(self, second_term: Term) -> Values:
        for indx, _ in enumerate(self.__init_values):
            self.__init_values[indx] += second_term
        return self

    def __sub__(self, subtrahend: Term) -> Values:
        return ListMath([val - subtrahend for val in self.__init_values])

    def __rsub__(self, minued: Term) -> Values:
        return ListMath([minued - val for val in self.__init_values])

    def __isub__(self, subtrahend: Term) -> Values:
        for indx, _ in enumerate(self.__init_values):
            self.__init_values[indx] -= subtrahend
        return self

    def __mul__(self, factor: Term) -> Values:
        return ListMath([val * factor for val in self.__init_values])

    def __rmul__(self, factor: Term) -> Values:
        return self.__mul__(factor)

    def __imul__(self, factor: Term) -> Values:
        for indx, _ in enumerate(self.__init_values):
            self.__init_values[indx] *= factor
        return self

    def __truediv__(self, divider: Term) -> Values:
        return ListMath([val / divider for val in self.__init_values])

    def __rtruediv__(self, dividend: Term) -> Values:
        return ListMath([dividend / val for val in self.__init_values])

    def __itruediv__(self, divider: Term) -> Values:
        for indx, _ in enumerate(self.__init_values):
            self.__init_values[indx] /= divider
        return self


lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0
