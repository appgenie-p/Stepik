from math import sqrt


class LineTo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"(x={self.x} y={self.y})"


class PathLines:
    def __init__(self, *args) -> None:
        self.lines = list((LineTo(0, 0),) + args)

    def get_path(self):
        return self.lines[1:]

    def get_length(self):
        lines = ((self.lines[i - 1], self.lines[i]) for i in range(1, len(self.lines)))
        return sum(
            (
                sqrt((line[0].x - line[1].x) ** 2 + (line[0].y - line[1].y) ** 2)
                for line in lines
            )
        )

    def add_line(self, line: LineTo) -> None:
        self.lines.append(line)

    def __repr__(self) -> str:
        return " -> ".join(i.__repr__() for i in self.lines)


p = PathLines(LineTo(1, 2))
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
