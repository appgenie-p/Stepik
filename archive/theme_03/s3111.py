import time


class Filter:
    def __init__(self, date) -> None:
        self.date = date

    def __setattr__(self, __name, __value) -> None:
        if hasattr(self, "date"):
            return
        if (isinstance(__value, int) or isinstance(__value, float)) and __value >= 0:
            super().__setattr__(__name, __value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self) -> None:
        self.slots = {
            1: None,
            2: None,
            3: None,
        }

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and type(filter) == Mechanical:
            self.slots[slot_num] = filter
        if slot_num == 2 and type(filter) == Aragon:
            self.slots[slot_num] = filter
        if slot_num == 3 and type(filter) == Calcium:
            self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num] = None

    def get_filters(self):
        return tuple([i for _, i in self.slots.items()])

    def water_on(self):
        return all(
            i is not None and (0 <= time.time() - i.date <= self.MAX_DATE_FILTER)
            for _, i in self.slots.items()
        )
