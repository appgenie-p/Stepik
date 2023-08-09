from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

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
        # first stack object
        self._top: Optional["StackObj"] = None

    def push_back(self, obj: "StackObj"):
        if self._top is None:
            self._top = obj
        elif self._top.next is None:
            self._top.next = obj
        else:
            last = self._top.next
            last = self.return_last_obj(last)
            last.next = obj

    def return_last_obj(self, last: "StackObj") -> "StackObj":
        while last.next is not None:
            last = last.next
        return last

    def pop_back(self) -> Optional["StackObj"]:
        if self._top is None:
            return None
        elif self._top.next is None:
            last = self._top
            self._top = None
            return last
        else:
            last = self._top.next
            last = self.return_penult_obj(last)
            last.next = None
            return last


class StackObj:
    def __init__(self, data: str):
        self._data = data
        self._next: Optional["StackObj"] = None

    @property
    def next(self) -> Optional["StackObj"]:
        return self._next

    @next.setter
    def next(self, obj: "StackObj") -> None:
        self._next = obj
