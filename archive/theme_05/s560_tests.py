import pytest

from s560 import GamePole, Ship


@pytest.fixture
def ship4v() -> Ship:
    return Ship(3, 2, 0, 0)


def test_ship_creation() -> None:
    assert Ship(2)
    assert Ship(2, 1)
    assert Ship(3, 2, 0, 0)


def test_ship_attrs():
    ship = Ship(3, 2, 0, 0)
    assert (
        ship._length == 3
        and ship.direction.value == 2
        and ship.x == 0
        and ship.y == 0
    ), "неверные значения атрибутов объекта класса Ship"
    assert ship.direction.name == "vertical", "неверное значение атрибута tp"


def test_ship_cells_and_move(ship4v: Ship):
    ship = ship4v
    assert ship.cells_condition == [1, 1, 1], "неверный список _cells"
    assert ship.is_moveable, "неверное значение атрибута _is_move"


def test_ship_set_start_coords(ship4v: Ship):
    ship = ship4v
    ship.set_start_coords(1, 2)
    assert (
        ship.x == 1 and ship.y == 2
    ), "неверно отработал метод set_start_coords()"


def test_ship_get_start_coords(ship4v: Ship):
    ship = ship4v
    assert ship.get_start_coords() == (
        0,
        0,
    ), "неверно отработал метод get_start_coords()"


def test_ship_move(ship4v: Ship):
    ship = Ship(3, 2, 0, 0)
    ship.move(1)
    assert ship.get_start_coords() == (0, 1)


def test_ship3h_around():
    s1 = Ship(length=3, tp=1, x=1, y=1)
    above = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)}
    below = {(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)}
    left = {(0, 1)}
    right = {(4, 1)}
    assert s1.cells_around == above.union(below, left, right)


def test_ship2v_around():
    s1 = Ship(length=2, tp=2, x=1, y=1)
    above = {(0, 0), (1, 0), (2, 0)}
    below = {(0, 3), (1, 3), (2, 3)}
    left = {(0, 1), (0, 2)}
    right = {(2, 1), (2, 2)}
    assert s1.cells_around == above.union(below, left, right)


def test_ship1v_around():
    s1 = Ship(length=1, tp=2, x=0, y=0)
    above = {(-1, -1), (0, -1), (1, -1)}
    below = {(-1, 1), (0, 1), (1, 1)}
    left = {(-1, 0)}
    right = {(1, 0)}
    assert s1.cells_around == above.union(below, left, right)


def test_ships():
    s1 = Ship(4, 1, 0, 0)
    s2 = Ship(3, 2, 0, 0)
    s3 = Ship(3, 2, 0, 2)

    assert s1.is_collide(s2), (
        "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и"
        " Ship(3, 2, 0, 0)"
    )
    assert s1.is_collide(s3) is False, (
        "неверно работает метод is_collide() "
        "для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
    )


def test_collide_s1_s2():
    s1 = Ship(4, 1, 0, 0)
    s2 = Ship(3, 2, 1, 1)
    assert s1.is_collide(s2), (
        "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и"
        " Ship(3, 2, 1, 1)"
    )


def test_s2_is_out_pole():
    s2 = Ship(3, 1, 8, 1)
    assert s2.is_out_pole(
        10
    ), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"


def test_s2_is_out_pole1():
    s2 = Ship(3, 2, 1, 5)
    assert (
        s2.is_out_pole(10) is False
    ), "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"


def test_ship_cells_edit_by_index():
    s2 = Ship(3, 2, 1, 5)
    s2[0] = 2
    assert s2[0] == 2, "неверно работает обращение ship[indx]"


def test_set_ship():
    game_pole = GamePole(size=10)
    ship = game_pole._set_ship(4)
    assert ship.direction.name in ["horizontal", "vertical"]
    assert 0 <= ship.x < 10
    assert 0 <= ship.y < 10
    assert len(ship.cells_condition) == 4


def test_ships_init():
    p = GamePole(10)
    p.init()
    p.show()
    for _ in range(5):
        for s in p._ships:
            assert (
                s.is_out_pole(10) is False
            ), "корабли выходят за пределы игрового поля"

            for ship in p.get_ships():
                if s != ship:
                    assert (
                        s.is_collide(ship) is False
                    ), "корабли на игровом поле соприкасаются"
        p.move_ships()


def test_get_pole():
    p = GamePole(10)
    p.init()
    p.show()
    gp = p.get_pole()
    assert (
        type(gp) == tuple and type(gp[0]) == tuple
    ), "метод get_pole должен возвращать двумерный кортеж"
    assert (
        len(gp) == 10 and len(gp[0]) == 10
    ), "неверные размеры игрового поля, которое вернул метод get_pole"


pole_size_8 = GamePole(8)
pole_size_8.init()
