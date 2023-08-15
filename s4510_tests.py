from s4510 import BreadFood, FishFood, SoupFood


def test_bread_food_init():
    bread = BreadFood("bread", 100, 250, True)
    assert bread.name == "bread"
    assert bread.weight == 100
    assert bread.calories == 250
    assert bread.white is True


def test_soup_food_init():
    soup = SoupFood("soup", 100, 250, True)
    assert soup.name == "soup"
    assert soup.weight == 100
    assert soup.calories == 250
    assert soup.dietary is True


def test_fish_food_init():
    fish_food = FishFood("salmon", 200, 300, "salmon")
    assert fish_food.name == "salmon"
    assert fish_food.weight == 200
    assert fish_food.calories == 300
    assert fish_food.fish == "salmon"
