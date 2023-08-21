from typing import Any

import pytest
from _pytest.capture import CaptureFixture, CaptureResult

from s447 import Data, PressureView, Subject, TemperatureView, WetView


@pytest.fixture
def subject():
    return Subject()


@pytest.fixture
def tv():
    return TemperatureView()


@pytest.fixture
def pr():
    return PressureView()


@pytest.fixture
def wet():
    return WetView()


def test_temperature_observer(
    tv: TemperatureView,
    pr: PressureView,
    wet: WetView,
    subject: Subject,
    capfd: CaptureFixture[str],
):
    subject.add_observer(tv)
    subject.add_observer(pr)
    subject.add_observer(wet)

    subject.change_data(Data(23, 150, 83))

    captured: Any = capfd.readouterr()
    expected_output = (
        "Текущая температура 23\n" "Текущее давление 150\n" "Текущая влажность 83\n"
    )
    assert captured.out == expected_output
