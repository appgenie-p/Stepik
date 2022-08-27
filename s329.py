class InputDigits:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwds):
        return [int(i) for i in self.func().split()]


@InputDigits
def input_dg():
    return input()


res = input_dg()
