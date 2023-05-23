import datetime
import time


class TimeParts:
    def __set_name__(self, obj, name: str):
        self.name = '_' + name

    def __set__(self, obj, val: int):
        if isinstance(val, int) and val >= 0:
            setattr(obj, self.name, val)

    def __get__(self, obj, type=None) -> int:
        return getattr(obj, self.name)


class Clock:
    """
    clock = Clock(hours, minutes, seconds)

    где hours, minutes, seconds - часы, минуты, секунды
    (целые неотрицательные числа).
    """
    hours = TimeParts()
    minutes = TimeParts()
    seconds = TimeParts()

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        """Получаем время в секундах.
        Возвращает текущее время в секундах (то есть, значение hours * 3600
        + minutes * 60 + seconds).
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    """Вычисляет разницу во времени.
    dt = DeltaClock(clock1, clock2)

    str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2
    в формате: часы: минуты: секунды
    len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах
    (целое число) Если разность получается отрицательной, то разницу времен
    считать нулевой.
    print(dt)   # отображает строку разницы времен clock1 - clock2 в формате:
    часы: минуты: секунды. Добавляется незначащий ноль, если число меньше 10.
    """
    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        gm = time.gmtime(len(self))
        return time.strftime("%H: %M: %S", gm)

    def __len__(self):
        diff = self.clock1.get_time() - self.clock2.get_time()
        return diff if diff >= 0 else 0


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
str_dt = str(dt)
print(str_dt)
len_dt = len(dt)
print(dt)       # 01: 30: 00
