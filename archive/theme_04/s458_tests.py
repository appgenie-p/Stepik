from s458 import Country


def test_class_country():
    country = Country("Россия", 140000000, 324005489.55)
    assert country.name == "Россия"
    assert country.population == 140000000
    assert country.square == 324005489.55
    assert country.get_info() == "Россия: 324005489.55, 140000000"
