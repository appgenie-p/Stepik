# import sys
from typing import Annotated, List, TypeVar, Union
from annotated_types import Gt

PositiveInt = TypeVar('PositiveInt', int, Annotated[int, Gt[0]])


class Record:
    def __init__(self, fio: str, description: str, old: int):
        self.fio = fio
        self.description = description
        self.old = old
        self._pk: Annotated[int, Gt[0]] = 0

    # set pk unique for each object in db

    def __repr__(self):
        return f"Record({self.fio}, {self.description}, {self.old})"

    # calculate hash by fio и old. Register is not important.
    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    # for object with equal hash equality should be true
    def __eq__(self, other):
        if not isinstance(other, Record):
            return False
        return hash(self) == hash(other)


# db = DataBase(path)
class DataBase:
    def __init__(self, path: str):
        self._path = path
        self.dict_db: dict[Record, List[Record]] = {}

    def read(self, pk: PositiveInt) -> Union['Record', None]:
        for record in self.dict_db:
            if record._pk == pk:
                return record
        return None

    def write(self, record: 'Record') -> None:
        if record in self.dict_db:
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]


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

pass