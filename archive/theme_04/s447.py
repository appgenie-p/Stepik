from typing import Any, Dict


class Data:
    def __init__(self, temp: int, press: int, wet: int):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


class Observer:
    def update(self, data: Data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers: Dict[Observer, Observer] = {}
        self.__data: Data

    def add_observer(self, observer: Observer) -> None:
        self.__observers[observer] = observer

    def remove_observer(self, observer: Observer) -> None:
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self) -> None:
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data: Data):
        self.__data = data
        self.__notify_observer()


class TemperatureView(Observer):
    def update(self, data: Data):
        print(f"Текущая температура {data.temp}")


class PressureView(Observer):
    def update(self, data: Data):
        print(f"Текущее давление {data.press}")


class WetView(Observer):
    def update(self, data: Data):
        print(f"Текущая влажность {data.wet}")
