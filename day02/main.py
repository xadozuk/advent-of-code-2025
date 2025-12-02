import time


def main():
    with open("day02/input.txt") as f:
        input = f.read().strip()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def chunks(input, size: int):
    return [input[i : i + size] for i in range(0, len(input), size)]


def parse(input: str):
    parsed_ranges = []
    for ranges in input.split(","):
        (a, b) = ranges.split("-")
        parsed_ranges.append((int(a), int(b)))

    return parsed_ranges


def is_pattern_simple(number: int) -> bool:
    str_num = str(number)
    a, b = str_num[: len(str_num) // 2], str_num[len(str_num) // 2 :]

    return a == b


def is_pattern_complex(number: int) -> bool:
    str_num = str(number)
    end = len(str_num) // 2

    for i in range(1, end + 1):
        cs = chunks(str_num, i)
        if all(c == cs[0] for c in cs):
            return True

    return False


def part_1(input: str):
    total = 0
    ranges = parse(input)

    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if is_pattern_simple(n):
                total += n

    return total


def part_2(input: str):
    total = 0
    ranges = parse(input)

    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if is_pattern_complex(n):
                print(n)
                total += n

    return total


if __name__ == "__main__":
    main()
