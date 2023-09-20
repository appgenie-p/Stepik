import re
from curses.ascii import isdigit
from typing import List, Union


def return_object(string: str) -> Union[int, float, str]:
    if re.fullmatch(r"-?\d+", string):
        return int(string)
    elif re.fullmatch(r"-?\d+\.\d+", string):
        return float(string)
    else:
        return string


def main() -> List[Union[int, float, str]]:
    lst_in = input().split()
    return [return_object(string) for string in lst_in]


if __name__ == "__main__":
    lst_out = main()
