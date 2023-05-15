class Body:
    def __init__(self, name, ro, volume):
        if type(name) == str:
            self.name = name
        if isinstance(ro, (int, float)):
            self.ro = ro
        if isinstance(volume, (int, float)):
            self.volume = volume

    def weight(self):
        return self.ro * self.volume

    @staticmethod
    def choose(other):
        if isinstance(other, Body):
            return other.weight()
        elif isinstance(other, (int, float)):
            return other
        raise ValueError("Неведома зверюшка")

    def __eq__(self, other):
        return self.weight() == self.choose(other)

    def __lt__(self, other):
        return self.weight() < self.choose(other)


# Test class Body with assert.
if __name__ == "__main__":
    b1 = Body("b1", 1, 1)
    b2 = Body("b2", 2, 2)
    b3 = Body("b3", 3, 3)
    assert b1 == 1
    assert b2 == 4
    assert b3 == 9
    # assert b1 > 0
    # assert b2 > 1
    # assert b3 > 4
    assert b1 < 2
    # assert b2 > 3
    assert b3 < 10
    print("OK")
