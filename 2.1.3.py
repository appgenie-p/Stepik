"""easy test
>>> clock.set_time(4530)
>>> clock.get_time()
4530
"""
class Clock:
    def __init__(self) -> None:
        self.time: int = 0

    def set_time(self, tm: int) -> None:        
        if self.check_time(tm):
            self.time = tm

    def check_time(self, tm: int) -> bool:
        return isinstance(tm, int) and 0 <= tm <= 100000

    def get_time(self) -> int:
        return self.time


clock = Clock()
clock.set_time(4530)

if __name__ == "__main__":
    import doctest
    doctest.testmod()