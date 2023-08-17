import pytest

from s476 import Planet, SolarSystem


def test_planet_attributes():
    planet = Planet("Меркурий", 4878, 87.97, 1407.5)
    assert planet._name == "Меркурий"
    assert planet._diametr == 4878
    assert planet._period_solar == 87.97
    assert planet._period == 1407.5


def test_solar_system_planets():
    solar_system = SolarSystem()
    assert solar_system._mercury._name == "Меркурий"
    assert solar_system._venus._name == "Венера"
    assert solar_system._earth._name == "Земля"
    assert solar_system._mars._name == "Марс"
    assert solar_system._jupiter._name == "Юпитер"
    assert solar_system._saturn._name == "Сатурн"
    assert solar_system._uranus._name == "Уран"
    assert solar_system._neptune._name == "Нептун"


def test_solar_system_one_instance():
    solar_system_1 = SolarSystem()
    solar_system_2 = SolarSystem()
    assert solar_system_1 is solar_system_2
