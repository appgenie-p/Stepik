class Line:
    """A line segment between two points."""

    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self) -> int:
        """Return the length of the line."""
        return int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)


# instantiate a line segment
segment1 = Line(0, 0, 3, 4)
print(f"segment1 is {len(segment1)} units long", "\n", bool(segment1))
