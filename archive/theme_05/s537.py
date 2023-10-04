from typing import Any, Collection, Tuple, Union


class TupleLimit(Tuple[Any, ...]):
    def __new__(cls, lst: Collection[Any], max_length: int):
        if len(lst) > max_length:
            raise ValueError(
                "число элементов коллекции превышает заданный предел"
            )
        return super().__new__(cls, lst)

    def __repr__(self):
        return " ".join(map(str, self))


def main() -> Union[TupleLimit, ValueError]:
    digits = list(map(float, input().split()))
    try:
        return TupleLimit(digits, 5)
    except ValueError as e:
        return e


if __name__ == "__main__":
    print(main())
