from s547_h import (
    CellException,
    CellFloat,
    CellFloatException,
    CellInteger,
    CellIntegerException,
    CellString,
    CellStringException,
    TupleData,
)

t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, "sergey")
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"


cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"


cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"


cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert (
    issubclass(CellIntegerException, CellException)
    and issubclass(CellFloatException, CellException)
    and issubclass(CellStringException, CellException)
), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
