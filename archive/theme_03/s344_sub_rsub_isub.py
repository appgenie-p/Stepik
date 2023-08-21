from typing import Sequence, Union


class NewList:
    Val = Union["NewList", list]

    def __init__(self, init_vals: list = []) -> None:
        self.init_vals = init_vals

    def get_list(self):
        return self.init_vals

    @staticmethod
    def __subtraction(minued: Sequence, subtrahend: Sequence) -> list:
        minuend_vstype = [(val, type(val)) for val in minued]
        subtrahend_vstype = [(val, type(val)) for val in subtrahend]
        for val in subtrahend_vstype:
            if val in minuend_vstype:
                minuend_vstype.remove(val)
        return [val for val, _ in minuend_vstype]

    @staticmethod
    def value_check(val: Val) -> list:
        if not isinstance(val, (list, NewList)):
            raise TypeError(
                "Переданные данные доложны быть следующих типов:" "list or NewList"
            )
        return val if isinstance(val, list) else val.init_vals

    def __sub__(self, subtrahend: Val) -> "NewList":
        return NewList(
            self.__subtraction(self.value_check(self), self.value_check(subtrahend))
        )

    def __isub__(self, subtrahend: Val) -> "NewList":
        self.init_vals = self.__subtraction(
            self.value_check(self), self.value_check(subtrahend)
        )
        return self

    def __rsub__(self, minued: Val) -> "NewList":
        return NewList(self.value_check(minued)) - self


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])

res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
