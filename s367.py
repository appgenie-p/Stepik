import sys
from typing import List, Union


class Record:
    pk_counter = 0

    def __init__(self, fio: str, description: str, old: int):
        self.fio = fio
        self.descr = description
        self.old = old
        self.pk: int = self._pk_generator()

    @classmethod
    def _pk_generator(cls):
        cls.pk_counter += 1
        return cls.pk_counter

    def __repr__(self):
        return f"Record({self.fio}, {self.descr}, {self.old})"

    # calculate hash by fio и old. Register is not important.
    def __hash__(self) -> int:
        return hash((self.fio.lower(), self.old))

    # for object with equal hash equality should be true
    def __eq__(self, other) -> bool:
        if not isinstance(other, Record):
            return False
        return hash(self) == hash(other)


class DataBase:
    def __init__(self, path: str):
        self._path = path
        self.dict_db: dict[Record, List[Record]] = {}

    def read(self, pk: int) -> Union['Record', None]:
        for record in self.dict_db:
            if record.pk == pk:
                return record
        return None

    def write(self, record: 'Record') -> None:
        self.dict_db.setdefault(record, []).append(record)


# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = [
    'Балакирев С.М.; программист; 33',
    'Кузнецов Н.И.; разведчик-нелегал; 35',
    'Суворов А.В.; полководец; 42',
    'Иванов И.И.; фигурант всех подобных списков; 26',
    'Балакирев С.М.; преподаватель; 33',
]

db = DataBase('db.txt')

# read lst_in line by line and write to db
for line in lst_in:
    fio, description, old = line.split(';')
    record = Record(fio, description, int(old))
    db.write(record)

dict.setdefault