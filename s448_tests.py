import pytest

from s448 import Aircraft, PassengerAircraft, WarPlane


def test_aircraft_creation():
    aircraft = Aircraft("Boeing 737", 100_000, 900, 12_000)
    assert aircraft.model == "Boeing 737"
    assert aircraft.mass == 100_000
    assert aircraft.speed == 900
    assert aircraft.top == 12_000


def test_aircraft_creation_with_negative_mass():
    with pytest.raises(TypeError):
        Aircraft("Boeing 737", -100_000, 900, 12_000)


def test_passenger_aircraft_creation_error():
    with pytest.raises(TypeError):
        PassengerAircraft('model', 1, 2, 3, 1.2)

def test_passenger_aircraft_creation_error():
    with pytest.raises(TypeError):
        WarPlane('model', 1, 2, 3, [1, 2])


def test_aircraft_creation_with_not_str_name():
    with pytest.raises(TypeError):
        Aircraft(5555, 100_000, 900, 12_000)


def test_planes():
    planes = [
        PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
        PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
        WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
        WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
    ]
    assert len(planes) == 4


def test_int_validator():
    with pytest.raises(TypeError):
        PassengerAircraft('МС-21', 1250, 8000, 12000.5, '140')