import time


def main():
    with open("day04/input.txt") as f:
        input = f.read().strip()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def parse(input: str) -> list[list[bool]]:
    return [[x == "@" for x in list(line)] for line in input.splitlines()]


def count_neighboors_at(pos: tuple[int, int], plan: list[list[bool]]):
    total = 0
    (pos_x, pos_y) = pos

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue

            x = pos_x + i
            y = pos_y + j

            if x < 0 or y < 0 or x >= len(plan) or y >= len(plan[x]):
                continue

            total += int(plan[x][y])

    return total


def part_1(input: str):
    plan = parse(input)
    total = 0

    for i in range(0, len(plan)):
        for j in range(0, len(plan[i])):
            if plan[i][j] and count_neighboors_at((i, j), plan) < 4:
                total += 1

    return total


def part_2(input: str):
    plan = parse(input)
    total = 0

    while True:
        sub_total = 0
        to_remove = []

        for i in range(0, len(plan)):
            for j in range(0, len(plan[i])):
                if plan[i][j] and count_neighboors_at((i, j), plan) < 4:
                    sub_total += 1
                    to_remove.append((i, j))

        total += sub_total

        if not sub_total:
            break

        for i, j in to_remove:
            plan[i][j] = False

    return total


if __name__ == "__main__":
    main()
