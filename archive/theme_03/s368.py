import sys


# bs = BookStudy(name, author, year)
class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))

# lst_in = [
#     'Python; Балакирев С.М.; 2020',
#     'Python ООП; Балакирев С.М.; 2021',
#     'Python ООП; Балакирев С.М.; 2022',
#     'Python; Балакирев С.М.; 2021',
# ]

lst_bs = [
    BookStudy(name, author, int(year))
    for name, author, year in (line.split(";") for line in lst_in)
]

unique_books = len(set(lst_bs))
