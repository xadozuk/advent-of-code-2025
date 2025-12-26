import time

from lib.shape import *
from lib.region import *


def main():
    with open("day12/input.txt") as f:
        input = f.read()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def parse(input: str) -> tuple[list[Shape], list[Region]]:
    parts = input.split("\n\n")

    shapes = [Shape.from_str("\n".join(shape.splitlines()[1:])) for shape in parts[:-1]]

    regions = [Region.from_str(r) for r in parts[-1].splitlines()]

    return (shapes, regions)


def part_1(input: str):
    shapes, regions = parse(input)

    # print(shapes, regions)

    result = 0
    for r in regions:
        result += r.can_fit(shapes)

    return result


def part_2(input: str):
    return 0


if __name__ == "__main__":
    main()
