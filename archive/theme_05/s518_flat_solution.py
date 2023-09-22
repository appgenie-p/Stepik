from curses.ascii import isdigit
from typing import Union


def return_object(string: str) -> Union[int, float, str]:
    if string.isdigit() or string[0] == "-" and string[1:].isdigit():
        return int(string)
    elif string[0] == "-" and string[1:].replace(".", "", 1).isdigit():
        return float(string)
    elif string.replace(".", "", 1).isdigit():
        return float(string)
    else:
        return string


lst_in = input().split()
lst_out = [return_object(string) for string in lst_in]
