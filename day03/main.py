import time


def main():
    with open("day03/input.txt") as f:
        input = f.read().strip()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def parse(input: str) -> list[list[int]]:
    banks = []

    for line in input.splitlines():
        banks.append([int(x) for x in list(line)])

    return banks


def find_max_with(bank: list[int], size: int):
    if size == 0:
        return None

    max = (-1, 0)

    # print("search: ", bank[0 : len(bank) - size + 1])

    for i in range(0, len(bank) - size + 1):
        if max[1] < bank[i]:
            max = (i, bank[i])

    if size > 1:
        next = find_max_with(bank[max[0] + 1 :], size - 1)
        return int(str(max[1]) + str(next))
    else:
        return max[1]


def part_1(input: str):
    banks = parse(input)
    total = 0

    for bank in banks:
        total += find_max_with(bank, 2)

    return total


def part_2(input: str):
    banks = parse(input)
    total = 0

    for bank in banks:
        total += find_max_with(bank, 12)

    return total


if __name__ == "__main__":
    main()
