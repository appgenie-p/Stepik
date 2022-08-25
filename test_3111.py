import pytest
import time

class Mechanical:
    def __init__(self, date) -> None:
        self.date = date        # положительное вещественное

    def __setattr__(self, __name, __value) -> None:
        if hasattr(self, 'date'):
            return
        if (isinstance(__value, int) or isinstance(__value, float)) \
                and __value >= 0:
            super().__setattr__(__name, __value)


class Aragon:
    def __init__(self, date) -> None:
        self.date = date        # положительное вещественное

    def __setattr__(self, __name, __value) -> None:
        if hasattr(self, 'date'):
            return
        super().__setattr__(__name, __value)


class Calcium:
    def __init__(self, date) -> None:
        self.date = date        # положительное вещественное

    def __setattr__(self, __name, __value) -> None:
        if hasattr(self, 'date'):
            return
        super().__setattr__(__name, __value)


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
        in_slots =  all(i != None for _, i in self.slots.items())
        service_time = all(i.date for _, i in self.slots.items())
        for _, i in self.slots.items():
            print(i) 
        #  (time.time() - i.date) in range(self.MAX_DATE_FILTER)
        return in_slots and service_time


################### TESTS###########################
def test_water_on(create_filters):
    g = GeyserClassic()
    for indx, _ in g.slots.items():
        g.add_filter(indx, create_filters[indx-1])
    assert g.water_on() == True


def test_filter_add_wrong():
    g = GeyserClassic()
    filter = Aragon(time.time())
    g.add_filter(1, filter)
    assert g.slots[1] == None


def test_filter_add():
    g = GeyserClassic()
    filter = Mechanical(time.time())
    g.add_filter(1, filter)
    assert g.slots[1] == filter


@pytest.fixture
def create_filters():
    return (
        Mechanical(time.time()),
        Aragon(time.time()),
        Calcium(time.time()),
    )

def test_mechanical_set_date(create_filters):    
    for i in create_filters:
        assert i.date == 555


def test_mechanical_date_no_change(create_filters):
    for i in (create_filters):
        i.date == 111
        assert i.date == 555

