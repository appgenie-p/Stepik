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
            last_obj = self._top
            while last_obj.next is not None:
                last_obj = last_obj.next
            last_obj.next = obj

    def pop_back(self) -> Optional["StackObj"]:
        if self._top is None:
            return None
        if self._top.next is None:
            obj = self._top
            self._top = None
            return obj
        penult: StackObj = self._top
        while penult.next.next is not None:
            penult = penult.next
        obj = penult.next
        penult.next = None
        return obj


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
