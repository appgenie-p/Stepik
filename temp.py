class Test:
    def __init__(self, a):
        self.a = a

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        a = 'HUI'
        self.__a = a

    def __repr__(self):
        return f'Test({self.a})'


t = Test('a')
print(t)