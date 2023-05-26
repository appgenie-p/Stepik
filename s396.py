class TriangleListIterator:
    def __init__(self, lst: list) -> None:
        self.lst = lst

    def __iter__(self):
        return (
            self.lst[row][col]
            for row in range(len(self.lst))
            for col in range(len(self.lst[row]))
        )


lst = [
    ['x00', 'x01', 'x02'],
    ['x10', 'x11'],
    ['x20', 'x21', 'x22', 'x23', 'x24'],
    ['x30', 'x31', 'x32', 'x33'],
]

it = TriangleListIterator(lst)

# for x in it:
#     print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)
