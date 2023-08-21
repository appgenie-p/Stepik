from s434 import ArtObject, Computer, Auto, Mercedes, Toyota


def test_art_object():
    art = ArtObject("Mona Lisa", 10.5, "Leonardo da Vinci", "1503-1506")
    assert art.name == "Mona Lisa"
    assert art.weight == 10.5
    assert art.author == "Leonardo da Vinci"
    assert art.date == "1503-1506"


def test_computer():
    comp = Computer("MacBook Pro", 2.0, 16, "Intel Core i7")
    assert comp.name == "MacBook Pro"
    assert comp.weight == 2.0
    assert comp.memory == 16
    assert comp.cpu == "Intel Core i7"


def test_auto():
    auto = Auto("Car", 1500.0, (2.0, 4.5, 1.5))
    assert auto.name == "Car"
    assert auto.weight == 1500.0
    assert auto.dims.width == 2.0
    assert auto.dims.length == 4.5
    assert auto.dims.height == 1.5


def test_mercedes():
    merc = Mercedes("Mercedes-Benz", 2000.0, (2.5, 5.0, 1.8), "S-Class", 5)
    assert merc.name == "Mercedes-Benz"
    assert merc.weight == 2000.0
    assert merc.dims.width == 2.5
    assert merc.dims.length == 5.0
    assert merc.dims.height == 1.8
    assert merc.model == "S-Class"
    assert merc.old == 5


def test_toyota():
    toyota = Toyota("Toyota Camry", 1500.0, (2.4, 4.5, 1.5), "Camry", 4)
    assert toyota.name == "Toyota Camry"
    assert toyota.weight == 1500.0
    assert toyota.dims.width == 2.4
    assert toyota.dims.length == 4.5
    assert toyota.dims.height == 1.5
    assert toyota.model == "Camry"
    assert toyota.wheel == 4
