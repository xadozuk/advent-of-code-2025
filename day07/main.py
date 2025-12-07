import time
from collections import deque


def main():
    with open("day07/input.txt") as f:
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
    start = (None, None)
    grid = []

    for i, line in enumerate(input.splitlines()):
        grid.append([])
        for j, c in enumerate(list(line)):
            if c == "S":
                start = (i, j)
                c = "."
            grid[i].append(c)

    return (start, grid)


def run_beam(start, grid):
    beams = deque()

    height = len(grid)
    width = len(grid[0])
    last_line_i = height - 1

    splits = {}
    cache = {}

    beams.append(start)

    while beams:
        (beam_i, beam_j) = beams.pop()

        if not cache.get((beam_i, beam_j), None):
            for i in range(beam_i, height):
                if grid[i][beam_j] == "^":
                    splits[(i, beam_j)] = True

                    if beam_j > 0:
                        beams.append((i, beam_j - 1))
                    if beam_j < width - 1:
                        beams.append((i, beam_j + 1))
                    break

            cache[(beam_i, beam_j)] = True

    return splits


def run_quantum_beam(
    start: tuple[int, int], grid: list[list[str]], cache: dict[tuple[int, int], int]
) -> int:
    if cache.get(start, None):
        return cache[start]

    start_i, start_j = start

    if start_j < 0 or start_j >= len(grid[0]):
        return 0

    for i in range(start_i + 1, len(grid)):
        if grid[i][start_j] == "^":
            timelines = run_quantum_beam((i, start_j - 1), grid, cache)
            timelines += run_quantum_beam((i, start_j + 1), grid, cache)

            cache[start] = timelines
            return timelines

    return 1


def part_1(input: str):
    start, grid = parse(input)

    result = run_beam(start, grid)

    return len(result)


def part_2(input: str):
    start, grid = parse(input)

    result = run_quantum_beam(start, grid, cache={})

    return result


if __name__ == "__main__":
    main()
