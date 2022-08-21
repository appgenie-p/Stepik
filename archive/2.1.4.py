"""easy test
>>> mn_1 = Money(10)
>>> mn_2 = Money(20)
>>> mn_1.set_money(100)
>>> mn_2.add_money(mn_1)
>>> mn_1.get_money()
100
>>> mn_2.get_money()
120
"""


class Money:
    def __init__(self, money: int) -> None:
        self.__money: int = 0
        self.set_money(money)

    def set_money(self, money: int) -> None:
        if self.check_money(money):
            self.__money = money

    def check_money(self, money: int) -> bool:
        return isinstance(money, int) and money > 0

    def add_money(self, mn: 'Money') -> None:
        self.__money += mn.get_money()

    def get_money(self):
        return self.__money


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120

if __name__ == "__main__":
    import doctest
    doctest.testmod()