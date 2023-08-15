from abc import ABC, abstractmethod
from typing import Any, Optional, TypeVar

T = TypeVar("T", bound="StackObj")


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj: Any):
        """Adds an object to end of the stack"""

    @abstractmethod
    def pop_back(self) -> Any:
        """Removes and returns the last object of the stack"""


class Stack(StackInterface):
    def __init__(self):
        self._top: Optional["StackObj"] = None

    def push_back(self, obj: "StackObj") -> None:
        if self._top is None:
            self._top = obj
        else:
            *_, last_obj = self
            last_obj.next = obj

    def pop_back(self) -> Optional["StackObj"]:
        if self._top is None:
            return None
        if self._top.next is None:
            last_obj = self._top
            self._top = None
            return last_obj
        *_, penult_obj, last_obj = self
        penult_obj.next = None
        return last_obj

    def __iter__(self):
        last_obj = self._top
        while last_obj is not None:
            yield last_obj
            last_obj = last_obj.next


class StackObj:
    def __init__(self, data: str):
        self._data = data
        self._next: Optional["StackObj"] = None

    @property
    def next(self) -> Optional["StackObj"]:
        return self._next

    @next.setter
    def next(self, obj: Optional["StackObj"]) -> None:
        self._next = obj
