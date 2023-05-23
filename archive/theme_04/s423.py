class ListInteger(list):
    def __init__(self, lst: list):
        for val in lst:
            self.__check_val(val)
        super().__init__(lst)

    @staticmethod
    def __check_val(val):
        if type(val) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, index, value):
        self.__check_val(value)
        super().__setitem__(index, value)

    def append(self, value):
        self.__check_val(value)
        super().append(value)
