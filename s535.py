from typing import Any, Union


class Test:
    def __init__(self, descr: str):
        _check_descr_size(descr)
        self.name = descr

    def run(self) -> bool:
        raise NotImplementedError


def _check_descr_size(descr: str):
    if not 10 <= len(descr) <= 10000:
        raise ValueError("Description must be 10-10000 characters long")


Number = Union[int, float]


class TestAnsDigit(Test):
    def __init__(self, descr: str, ans_digit: Number, max_error_digit: Number):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, key: Any, value: Any) -> None:
        if key in ("ans_digit", "max_error_digit") and type(value) not in (
            int, float
        ):
            raise ValueError("недопустимые значения аргументов теста")
        if key == "max_error_digit" and value < 0:
            raise ValueError("недопустимые значения аргументов теста")
