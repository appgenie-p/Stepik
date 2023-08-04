from s435 import Agency, Flat, House, SellItem


def test_sell_item():
    item = SellItem("item1", 100)
    assert item.name == "item1"
    assert item.price == 100


def test_flat():
    flat = Flat("flat1", 200, 50, 2)
    assert flat.name == "flat1"
    assert flat.price == 200
    assert flat.size == 50
    assert flat.rooms == 2


def test_house():
    house = House("house1", 300, "wood", 100)
    assert house.name == "house1"
    assert house.price == 300
    assert house.material == "wood"
    assert house.square == 100


def test_agency():
    agency = Agency("agency1")
    assert agency.name == "agency1"

    item1 = SellItem("item1", 100)
    item2 = Flat("flat1", 200, 50, 2)
    item3 = House("house1", 300, "wood", 100)

    agency.add_object(item1)
    agency.add_object(item2)
    agency.add_object(item3)

    assert len(list(agency.get_objects())) == 3

    agency.remove_object(item2)

    assert len(list(agency.get_objects())) == 2
