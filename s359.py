from typing import Union


class Body:
    def __init__(
        self, name: str, ro: Union[int, float], volume: Union[int, float]
    ):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.mass = ro * volume

    def __repr__(self):
        return f"{self.name}({self.ro}, {self.volume})"

    def _choose_type(self, other):
        if isinstance(other, (int, float)):
            return other
        if isinstance(other, Body):
            return other.mass
        raise ValueError("Not a number or Body")

    def __eq__(self, other):
        return self.mass == self._choose_type(other)

    def __gt__(self, other):
        return self.mass > self._choose_type(other)

    def __lt__(self, other):
        return self.mass < self._choose_type(other)


# Test class Body with assert.
if __name__ == "__main__":
    b1 = Body("b1", 1, 1)
    b2 = Body("b2", 2, 2)
    b3 = Body("b3", 3, 3)
    assert b1 == 1
    assert b2 == 4
    assert b3 == 9
    assert b1 > 0
    assert b2 > 1
    assert b3 > 4
    assert b1 < 2
    assert b2 > 3
    assert b3 < 10
    print("OK")
