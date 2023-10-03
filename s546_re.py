import re
from typing import Union


class WrongDate(Exception):
    pass


class DateString:
    def __init__(self, date_string: str):
        self.match = check_date_string(date_string)
        self.date_string = date_string

    def __str__(self) -> str:
        gr = self.match.group
        return (
            f"{gr('DD'):0>2}.{gr('MM'):0>2}.{gr('YYYY'):0>4}"
        )


def check_date_string(date_string: str) -> re.Match[str]:
    raw = r"^(?P<DD>[0-3]{0,1}[1-9])\.(?P<MM>\d?[1-9]).(?P<YYYY>\d{4})$"
    if matching := re.match(raw, date_string):
        return matching
    raise WrongDate("Неверный формат даты")


def main() -> Union[DateString, WrongDate]:
    date_string = "26.5.2022"
    try:
        return DateString(date_string)
    except WrongDate as wd:
        return wd


if __name__ == "__main__":
    print(main())
