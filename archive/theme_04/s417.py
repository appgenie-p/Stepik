class Base:
    def __new__(cls, *args, **kwargs):
        print("Base.__new__ called")
        obj = super().__new__(cls)
        setattr(obj, "args", args)
        setattr(obj, "kwargs", kwargs)
        return obj


class Singleton(Base):
    """An abstract python singleton class"""

    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Game(Singleton):
    """A class for game"""

    def __init__(self, name: str):
        if not hasattr(self, "name"):
            self.name = name


game1 = Game("game1")
game2 = Game("game2")

print(game1.name)
print(game2._instance)
