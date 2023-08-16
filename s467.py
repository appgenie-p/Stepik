from operator import add, sub
from typing import Any, Callable, Union

Number = Union[int, float]
Other = Union[Number, "Money"]


class Money:
    def __init__(self, money: Number) -> None:
        self.money = money

    @property
    def money(self) -> Number:
        return self._money

    @money.setter
    def money(self, money: Any) -> None:
        if not isinstance(money, (int, float)):
            raise TypeError("сумма должна быть числом")
        self._money = money


class MoneyOperators:
    def __add__(self, other: Other) -> "Money":
        self._other = other
        return self.execute_math(add)

    def __sub__(self, other: Other) -> "Money":
        self._other = other
        return self.execute_math(sub)

    Operator = Callable[[Number, Number], Number]

    def execute_math(self, operator: Operator) -> "Money":
        self._operator = operator
        if self.other_is_number():
            return self.execute_operation(self._other)

        self.raise_error_if_mismatched_type()
        return self.execute_operation(self._other.money)

    def execute_operation(
        self, other: Union[Number, "Money"]
    ) -> "Money":
        return self.__class__(self._operator(self.money, other))  # type: ignore

    def other_is_number(self) -> bool:
        return type(self._other) in (int, float)

    def raise_error_if_mismatched_type(self):
        if not isinstance(self._other, type(self)):
            raise TypeError("Разные типы объектов")


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"
