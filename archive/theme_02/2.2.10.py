from dataclasses import dataclass


class PhoneBook:
    def __init__(self) -> None:
        self.phones: list = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, indx: int):
        try:
            self.phones.pop(indx)
        except IndexError:
            raise "index is not exist"

    def get_phone_list(self):
        return self.phones


@dataclass
class PhoneNumber:
    def __init__(self, number: int, fio: str) -> None:
        self._number = number
        self.fio = fio

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: int):
        if len(str(number)) == 11:
            self._number = number
            return None
        raise Exception("Number of digits is not 11")


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
# print(vars(p))
phones = p.get_phone_list()
pass
