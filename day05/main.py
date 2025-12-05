import time


def main():
    with open("day05/input.txt") as f:
        input = f.read().strip()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def parse(input: str):
    ranges = []
    ranges_str, ids_str = input.split("\n\n")

    for range_str in ranges_str.splitlines():
        start, end = range_str.split("-")
        ranges.append((int(start), int(end)))

    ids = list(map(lambda x: int(x), ids_str.splitlines()))

    return (ranges, ids)


def in_ranges(id, ranges):
    for start, end in ranges:
        if id >= start and id <= end:
            return True

    return False


def unique_ranges(ranges):
    ranges.sort(key=lambda r: r[0])

    uniq_ranges = []
    curr = ranges[0]

    for r in ranges[1:]:
        if r[0] <= curr[1]:
            curr = (curr[0], max(curr[1], r[1]))
        else:
            uniq_ranges.append(curr)
            curr = r

    uniq_ranges.append(curr)

    return uniq_ranges


def part_1(input: str):
    ranges, ids = parse(input)
    u_ranges = unique_ranges(ranges)
    total = 0

    return sum([int(in_ranges(id, u_ranges)) for id in ids])


def part_2(input: str):
    ranges, _ = parse(input)
    return sum([end - start + 1 for start, end in unique_ranges(ranges)])


if __name__ == "__main__":
    main()
