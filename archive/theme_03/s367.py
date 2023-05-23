from collections import defaultdict
import itertools
import sys
from typing import Set, Union


class Record:
    pk_counter = itertools.count(start=1, step=1)

    def __init__(self, fio: str, description: str, old: int):
        self.fio = fio
        self.descr = description
        self.old = old
        self.pk: int = next(self.pk_counter)

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
        self.dict_db: dict[Record, Set[Record]] = defaultdict(set)
        self.pk_dict: dict[int, Record] = {}

    def read(self, pk: int) -> Union['Record', None]:
        return self.pk_dict.get(pk)

    def write(self, record: 'Record') -> None:
        self.dict_db[record].add(record)
        self.pk_dict[record.pk] = record


lst_in = list(map(str.strip, sys.stdin.readlines()))

# lst_in = [
#     'Балакирев С.М.; программист; 33',
#     'Кузнецов Н.И.; разведчик-нелегал; 35',
#     'Суворов А.В.; полководец; 42',
#     'Иванов И.И.; фигурант всех подобных списков; 26',
#     'Балакирев С.М.; преподаватель; 33',
# ]

db = DataBase('db.txt')

for line in lst_in:
    fio, description, old = line.split(';')
    try:
        record = Record(fio, description, int(old))
    except ValueError:
        print(f"invalid input {line}")
        continue
    else:
        db.write(record)
