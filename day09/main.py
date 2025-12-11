from collections import deque
from itertools import combinations
import time


def main():
    with open("day09/input.txt") as f:
        input = f.read()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def parse(input: str):
    return [tuple(map(int, line.split(","))) for line in input.splitlines()]


def area(a, b):
    return abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_neighboors(start, points):
    possible_neighboors = [
        (p, distance(start, p))
        for p in points
        if start != p and (p[0] == start[0] or p[1] == start[1])
    ]

    selected_neighboors = sorted(possible_neighboors, key=lambda n: n[1])[:2]

    return map(lambda n: n[0], selected_neighboors)


def segments(points):
    s = set()

    for p in points:
        for n in find_neighboors(p, points):
            if (n[0] == p[0] or n[1] == p[1]) and not (n, p) in s:
                s.add((p, n))

    return list(s)


def intersect(rectangle, segment):
    # print(rectangle, segment)
    (ca_x, ca_y), (cb_x, cb_y) = rectangle
    (sa_x, sa_y), (sb_x, sb_y) = sorted(segment)

    ca_x, cb_x = min(ca_x, cb_x), max(ca_x, cb_x)
    ca_y, cb_y = min(ca_y, cb_y), max(ca_y, cb_y)

    # One of the segment edge inside the rectangle
    if (
        sa_x > ca_x
        and sa_x < cb_x
        and sa_y > ca_y
        and sa_y < cb_y
        or sb_x > ca_x
        and sb_x < cb_x
        and sb_y > ca_y
        and sb_y < cb_y
    ):
        # print("Hit1")
        return True

    # One of the segment traversing the rectangle
    if (
        sa_x == sb_x
        and sa_x > ca_x
        and sa_x < cb_x
        and (sa_y >= ca_y and sa_y <= cb_y or sb_y >= ca_y and sb_y <= cb_y)
        or sa_y == sb_y
        and sa_y > ca_y
        and sa_y < cb_y
        and (sa_y >= ca_y and sa_y <= cb_y or sb_y >= ca_y and sb_y <= cb_y)
    ):
        # print("Hit2")
        return True

    return False


def print_grid(rect, all_segments, size):
    grid = [[None] * size[1] for i in range(size[0])]

    ((rax, ray), (rbx, rby)) = rect
    for x in range(min(rax, rbx), max(rax, rbx) + 1):
        for y in range(min(ray, rby), max(ray, rby) + 1):
            grid[x][y] = "-"

    for s in all_segments:
        for e in s:
            grid[e[0]][e[1]] = "#"

    print("")
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print(grid[x][y] or ".", end="")
        print("")


def part_1(input: str):
    points = parse(input)

    rectangles = [(area(a, b), (a, b)) for (a, b) in combinations(points, 2)]

    largest_rectangle = sorted(rectangles, key=lambda r: r[0], reverse=True)[0]

    return largest_rectangle[0]


def part_2(input: str):
    points = parse(input)
    rectangles = sorted(
        [(area(a, b), (a, b)) for (a, b) in combinations(points, 2)],
        key=lambda r: r[0],
        reverse=True,
    )

    width = max(map(lambda p: p[0], points)) + 3
    height = max(map(lambda p: p[1], points)) + 2

    all_segments = segments(points)

    # print(all_segments)

    for a, r in rectangles:
        ok = True
        # print_grid(r, all_segments, (width, height))
        for segment in all_segments:
            if intersect(r, segment):
                ok = False
                break

        if ok:
            return a

    return None


if __name__ == "__main__":
    main()
