import time


def main():
    with open("day01/input.txt") as f:
        input = f.read().strip()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def parse(input: str) -> list[int]:
    values = []

    for line in input.splitlines():
        dir, n = line[:1], int(line[1:])

        if dir == "L":
            n = -n

        values.append(n)

    return values


def part_1(input: str):
    pointer, password = 50, 0

    for n in parse(input):
        pointer += n
        pointer %= 100

        if pointer == 0:
            password += 1

    return password


def part_2(input: str):
    pointer, password = 50, 0

    for n in parse(input):
        start_at_zero = pointer == 0
        pointer += n

        if pointer == 0:
            password += 1
        elif pointer >= 100:
            password += pointer // 100
        elif pointer < 0:
            password += pointer // -100 + int(not start_at_zero)

        pointer %= 100

    return password


if __name__ == "__main__":
    main()
