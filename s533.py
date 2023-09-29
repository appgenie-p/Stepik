from typing import Tuple


def input_int_numbers() -> Tuple[int, ...]:
    try:
        return tuple(int(x) for x in input().split())
    except ValueError as e:
        raise TypeError("все числа должны быть целыми") from e


def main():
    while True:
        try:
            print(" ".join([str(x) for x in input_int_numbers()]))
            break
        except TypeError:
            continue


if __name__ == "__main__":
    main()
