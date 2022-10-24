from typing import Union


class Person:
    TypesUsed = Union[str, int, float]

    def __init__(
            self,
            fio: str,
            job: str,
            old: int,
            salary: Union[int, float],
            year_job: int
        ) -> None:
        self.fio, self.job, self.old, self.salary, self.year_job = (
                fio, job, old, salary, year_job)
        self.attr_index = list(enumerate(self.__dict__.keys()))

    def get_key_by_index(self, index: int) -> str:
        try:
            return self.attr_index[index][1]
        except IndexError:
            raise IndexError('неверный индекс')
        
    def __getitem__(self, index: int) -> TypesUsed:
        return self.__dict__[self.get_key_by_index(index)]
    
    def __setitem__(self, index: int, value: TypesUsed) -> None:
        self.__dict__[self.get_key_by_index(index)] = value

    def __iter__(self):
        self.iter_val = 0
        return self
    
    def __next__(self):
        if self.iter_val < len(self.__dict__) - 2:
            val = self[self.iter_val]
            self.iter_val += 1
            return val
        else:
            raise StopIteration
        

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers[0])
pers[0] = 'Балакирев С.М.'

for v in pers:
    print(v)

# pers[5] = 123 # IndexError