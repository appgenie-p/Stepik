class ListInteger(list):
    def __init__(self, lst):
        if not isinstance(lst, (tuple, list)):
            raise TypeError('можно передавать только кортеж или список')
        self.lst = list(lst)

    def __setitem__(self, index: int, value: int) -> None:
        self.lst[index] = value


s = ListInteger([1, 2, 3])
s[1] = 10
print(s)
s.append(11)
print(s)
# s[0] = 10.5 # TypeError