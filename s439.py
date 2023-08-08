from collections import UserString


class StringDigit(UserString):
    def __init__(self, data: str):
        if not all([char.isdigit() for char in data]):
            raise ValueError("StringDigit must contain only digits")
        super().__init__(data)
