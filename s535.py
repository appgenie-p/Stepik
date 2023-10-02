from typing import Any, Union


class Test:
    def __init__(self, descr: str):
        _check_descr_size(descr)
        self.name = descr

    def run(self) -> bool:
        raise NotImplementedError


def _check_descr_size(descr: str):
    if not 10 <= len(descr) <= 10000:
        raise ValueError(
            "формулировка теста должна быть от 10 до 10 000 символов"
        )


Number = Union[int, float]


class TestAnsDigit(Test):
    def __init__(
        self, descr: str, ans_digit: Number, max_error_digit: Number = 0.01
    ):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, key: Any, value: Any) -> None:
        if (
            key in ("ans_digit", "max_error_digit")
            and type(value)
            not in (
                int,
                float,
            )
            or (key == "max_error_digit" and value < 0)
        ):
            raise ValueError("недопустимые значения аргументов теста")
        super().__setattr__(key, value)

    def run(self) -> bool:
        ans = float(input())
        ans_digit = self.ans_digit
        max_error_digit = self.max_error_digit
        return (
            ans_digit - max_error_digit <= ans <= ans_digit + max_error_digit
        )


def main() -> Union[Exception, bool]:
    descr, ans = map(str.strip, input().split("|"))
    try:
        test = TestAnsDigit(descr, float(ans))
        return test.run()
    except Exception as e:
        return e


if __name__ == "__main__":
    print(main())
