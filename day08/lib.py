from math import sqrt


class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __str__(self):
        return f"(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return str(self)

    @staticmethod
    def distance(a: Point, b: Point):
        return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)


class Circuit:
    id = 1

    def __init__(self, iterable=[]):
        self.id, Circuit.id = Circuit.id, Circuit.id + 1
        self.boxes = set(iterable)

    def __len__(self):
        return len(self.boxes)

    def __str__(self):
        return str(f"{{id={self.id}, len={len(self)}, boxes={self.boxes}}}")

    def __repr__(self):
        return str(self)

    def add(self, box):
        self.boxes.add(box)

    def merge(self, other: Circuit):
        self.boxes.update(other.boxes)
        other.boxes.clear()
