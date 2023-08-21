from typing import Any, Dict, Generic, Type, TypeVar, Union

T = TypeVar("T", bound="Aircraft")
Numbers = Union[int, float]


class PositiveNumberDescriptor(Generic[T]):
    def __set_name__(self, owner: Type[T], name: str) -> None:
        self.name = "_" + name

    def __get__(self, obj: T, objtype: Type[T]) -> Numbers:
        return obj.__dict__[self.name]

    def __set__(self, obj: T, value: Any) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise TypeError("Value must be positive")
        obj.__dict__[self.name] = value


class Aircraft:
    slots = ("model", "mass", "speed", "top")

    mass = PositiveNumberDescriptor["T"]()
    speed = PositiveNumberDescriptor["T"]()
    top = PositiveNumberDescriptor["T"]()

    def __init__(self, model: str, mass: Numbers, speed: Numbers, top: Numbers):
        self.model = model
        self.mass = mass
        self.speed = speed
        self.top = top

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: Any) -> None:
        self._validate_data(value, str)
        self._model = value

    def _validate_data(self, value: Any, value_type: Type[object]) -> None:
        if not isinstance(value, value_type):
            raise TypeError("Data validation failed")


class PassengerAircraft(Aircraft):
    slots = ("model", "mass", "speed", "top", "chairs")

    def __init__(
        self,
        model: str,
        mass: Numbers,
        speed: Numbers,
        top: Numbers,
        chairs: int,
    ):
        super().__init__(model, mass, speed, top)
        self.chairs = chairs

    @property
    def chairs(self) -> int:
        return self._chairs

    @chairs.setter
    def chairs(self, value: Any) -> None:
        self._validate_data(value, int)
        self._chairs = value


class WarPlane(Aircraft):
    slots = ("model", "mass", "speed", "top", "weapons")

    WeaponName = str
    WeaponCount = int
    FlyHigh = Numbers

    def __init__(
        self,
        model: str,
        mass: Numbers,
        speed: Numbers,
        top: FlyHigh,
        weapons: Dict[WeaponName, WeaponCount],
    ):
        super().__init__(model, mass, speed, top)
        self.weapons = weapons

    @property
    def weapons(self) -> Dict[WeaponName, WeaponCount]:
        return self._weapons

    @weapons.setter
    def weapons(self, value: Any) -> None:
        self._validate_data(value, dict)
        self._weapons = value


planes = [
    PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
    PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
    WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
]
