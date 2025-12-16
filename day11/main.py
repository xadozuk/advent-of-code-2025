import time


def main():
    with open("day11/input.txt") as f:
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
    connections = {}

    for line in input.splitlines():
        s, to = line.split(": ")
        connections[s] = to.split()

    return connections


def traverse(start, end, connections, cache):
    if start == end:
        # print("<-", [[end]])
        return [[end]]

    if (start, end) in cache:
        return cache[(start, end)]

    results = []

    for next in connections.get(start, []):
        # print("->", start, next)
        paths = traverse(next, end, connections, cache)

        if len(paths) > 0:
            results.extend([[start] + p for p in paths])

    cache[(start, end)] = results
    return results


def part_1(input: str):
    cnx = parse(input)

    results = traverse("you", "out", cnx, {})

    return len(results)


def part_2(input: str):
    cnx = parse(input)

    cache = {}

    print("fft -> dac")
    left, right = "fft", "dac"
    middle = traverse(left, right, cnx, cache)

    if len(middle) == 0:
        print("dac -> fft")
        left, right = "dac", "fft"
        middle = traverse(left, right, cnx, cache)

    print(right, "-> end")
    end = traverse(right, "out", cnx, cache)

    print("svr ->", left)
    start = traverse("svr", left, cnx, cache)

    print(len(start), len(middle), len(end))

    return len(start) * len(middle) * len(end)


if __name__ == "__main__":
    main()
