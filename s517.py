from typing import List


def if_int(x: str) -> int:
    try:
        return int(x)
    except ValueError:
        return 0


def main() -> int:
    lst_in: List[str] = input().split()
    return sum(if_int(x) for x in lst_in)


if __name__ == "__main__":
    print(main())
