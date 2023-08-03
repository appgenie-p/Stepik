from __future__ import annotations

from typing_extensions import TypeGuard


def is_str_list(value: list[object]) -> TypeGuard[list[str]]:
    """Are all list items strings?"""
    return all(isinstance(x, str) for x in value)


x: list[object]

reveal_type(x)
if is_str_list(x):
    reveal_type(x)
