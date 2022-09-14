from typing import List, Sequence, Union


class ListMath:
    Term = Union[int, float]
    Values = List[Term]

    def __init__(self, init_values: Sequence = []) -> None:
        self.__init_values = [
            val for val in init_values if type(val) in (int, float)
        ]

    def do(self, term, func):
        return [getattr(val, func)(term) for val in self.__init_values]

    def __add__(self, term: Term) -> "ListMath":
        return self.do(term, '__add__')


lst2 = ListMath([1, 2, -5, 7.68])
res = lst2 + 10
pass