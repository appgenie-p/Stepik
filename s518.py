from curses.ascii import isdigit
from typing import List, Union


def return_object(string: str) -> Union[int, float, str]:
    if string.isdigit() or string[0] == "-" and string[1:].isdigit():
        return int(string)
    elif string[0] == "-" and string[1:].replace(".", "", 1).isdigit():
        return float(string)
    elif string.replace(".", "", 1).isdigit():
        return float(string)
    else:
        return string


def main() -> List[Union[int, float, str]]:
    lst_in = input().split()
    return [return_object(string) for string in lst_in]


if __name__ == "__main__":
    lst_out = main()
