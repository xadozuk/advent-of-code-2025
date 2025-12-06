import time


def main():
    with open("day00/input.txt") as f:
        input = f.read()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def part_1(input: str):
    return 0


def part_2(input: str):
    return 0


if __name__ == "__main__":
    main()
