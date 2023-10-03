import re
from datetime import datetime
from typing import Union


class WrongDate(Exception):
    pass


class DateString:
    def __init__(self, date_string: str):
        check_date_string(date_string)
        self.date_string = datetime.strptime(date_string, "%d.%m.%Y")

    def __str__(self):
        return self.date_string.strftime("%d.%m.%Y")


def check_date_string(date_string: str) -> None:
    matching = re.match(r"^[0-3]{0,1}[1-9]\.\d?[1-9].\d{4}$", date_string)
    if not matching:
        raise WrongDate("Неверный формат даты")


def main() -> Union[DateString, WrongDate]:
    date_string = input()
    try:
        return DateString(date_string)
    except WrongDate as wd:
        return wd


if __name__ == "__main__":
    print(main())