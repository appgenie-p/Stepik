from typing import Any, Generic, List, SupportsIndex, TypeVar, Union, overload

_T = TypeVar("_T")


class SoftList(List[Any], Generic[_T]):
    @overload
    def __getitem__(self, __i: SupportsIndex) -> Union[_T, bool]:
        ...

    @overload
    def __getitem__(self, __s: slice) -> list[_T]:
        ...

    def __getitem__(self, index: Any):
        if index not in range(-len(self), len(self)):
            return False
        return super().__getitem__(index)
