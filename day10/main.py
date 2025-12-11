import time

from lib import Machine, MachineP2


def main():
    with open("day10/input.txt") as f:
        input = f.read()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def parse(input: str, klass) -> list[Machine]:
    return [klass.from_str(line) for line in input.splitlines()]


def part_1(input: str):
    machines = parse(input, Machine)
    print(machines)

    total = 0
    for m in machines:
        r = m.solve()
        if r:
            total += len(r)

    return total


def part_2(input: str):
    machines = parse(input, MachineP2)

    print(machines)

    total = 0
    for i, m in enumerate(machines):
        print(f"[{i}/{len(machines)}]")
        total += m.solve()

    return total


if __name__ == "__main__":
    main()
