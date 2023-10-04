from s555 import Box, BoxDefender

b = Box("name", 2000)
assert (
    b._name == "name" and b._max_weight == 2000
), "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2

else:
    assert False, "не сгенерировалось исключение ValueError"


try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert (
        False
    ), "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"
