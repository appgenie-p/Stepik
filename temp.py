from typing import TypeVar

Abc = TypeVar("Abc", bound="A")


class A:
    def __init__(self, x: int) -> None:
        self.x = x


class B(A):
    def __init__(self, x: int) -> None:
        super().__init__(x)