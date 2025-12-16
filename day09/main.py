from collections import deque
from itertools import combinations, pairwise
import math
import time
from colorama import Fore


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
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def compress_coords(points, func):
    coords = set([func(p) for p in points])
    # Add border so we have empty space around the polygon
    coords.update([-math.inf, math.inf])

    sorted_coords = sorted(list(coords))

    # Return a mapping of original coord -> compressed coords
    return dict([(value, i) for i, value in enumerate(sorted_coords)])


IN = 1
OUT = 2


def floodfill(compressed, width, height):
    grid = {}

    # Fill the grid with the known edges
    for a, b in pairwise(compressed + [compressed[0]]):
        (ax, ay), (bx, by) = minmax((a, b))
        for x in range(ax, bx + 1):
            for y in range(ay, by + 1):
                grid[(x, y)] = IN

    # Start outside and fill everything possible (not already IN or OUT)
    todo = deque([(0, 0)])

    while todo:
        (x, y) = todo.popleft()

        if x < 0 or x >= width + 1 or y < 0 or y >= height + 1:
            continue

        if (x, y) not in grid:
            grid[(x, y)] = OUT

            todo.extendleft([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    return grid


def is_valid_compressed_rect(rect, grid):
    ((ax, ay), (bx, by)) = minmax(rect)

    for x in range(ax, bx + 1):
        for y in range(ay, by + 1):
            if grid.get((x, y), IN) == OUT:
                # print(rect, area((ax, ay), (bx, by)), "cause", (x, y), False)
                return False

    # print(rect, area((ax, ay), (bx, by)), True)
    return True


def origin_coords(coords, compressed_x: dict[int, int], compressed_y: dict[int, int]):
    cx_values = list(compressed_x.values())
    cx_keys = list(compressed_x.keys())
    cy_values = list(compressed_y.values())
    cy_keys = list(compressed_y.keys())

    return [
        (cx_keys[cx_values.index(x)], cy_keys[cy_values.index(y)]) for x, y in coords
    ]


def is_in_rect(point, rect):
    x, y = point
    (ax, ay), (bx, by) = rect

    l, r = min(ax, bx), max(ax, bx)
    b, t = min(ay, by), max(ay, by)

    return l <= x <= r and b <= y <= t


def minmax(rect):
    (ax, ay), (bx, by) = rect

    return (min(ax, bx), min(ay, by)), (max(ax, bx), max(ay, by))


def compress_rect(rect, compressed_x, compressed_y):
    return (
        (compressed_x[rect[0][0]], compressed_y[rect[0][1]]),
        (compressed_x[rect[1][0]], compressed_y[rect[1][1]]),
    )


def print_grid(points, rect=None, grid=None):
    # Add empty border around
    width = max([p[0] for p in points]) + 2
    height = max([p[1] for p in points]) + 2

    print("")
    for y in range(height):
        for x in range(width):
            color = ""

            if grid:
                if grid.get((x, y), IN) == OUT:
                    color = Fore.RED
                else:
                    color = Fore.GREEN

            if (x, y) in points:
                print(color + "#", sep="", end="")
            elif rect and is_in_rect((x, y), rect):
                print(color + "-", sep="", end="")
            else:
                print(color + ".", sep="", end="")
            print(Fore.RESET, end="", sep="")
        print("")


def part_1(input: str):
    points = parse(input)

    rectangles = [(area(a, b), (a, b)) for (a, b) in combinations(points, 2)]

    largest_rectangle = sorted(rectangles, key=lambda r: r[0], reverse=True)[0]

    return largest_rectangle[0]


def part_2(input: str):
    points = parse(input)

    compressed_x = compress_coords(points, lambda p: p[0])
    compressed_y = compress_coords(points, lambda p: p[1])
    compressed = [(compressed_x[x], compressed_y[y]) for x, y in points]

    floodfilled_grid = floodfill(compressed, len(compressed_x), len(compressed_y))

    # print_grid(points)
    # print_grid(compressed, None, floodfilled_grid)

    rectangles = sorted(
        [(area(a, b), (a, b)) for (a, b) in combinations(points, 2)], reverse=True
    )

    for a, r in rectangles:
        c_r = compress_rect(r, compressed_x, compressed_y)
        # print(a, r, c_r)

        if is_valid_compressed_rect(c_r, floodfilled_grid):
            return a

    return None


if __name__ == "__main__":
    main()
