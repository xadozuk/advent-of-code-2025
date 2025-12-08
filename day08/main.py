import time
import itertools

from lib import Point, Circuit


def main():
    with open("day08/input.txt") as f:
        input = f.read().strip()

    start = time.time_ns()
    print(
        "Part 1: ", part_1(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )

    start = time.time_ns()
    print(
        "Part 2: ", part_2(input), " [", (time.time_ns() - start) / 1e6, "ms]", sep=""
    )


def parse(input: str) -> list[Point]:
    return [Point(*line.split(",")) for line in input.splitlines()]


def combine_and_sort(boxes):
    box_pairs = [
        (pair, Point.distance(*pair)) for pair in itertools.combinations(boxes, 2)
    ]

    return sorted(box_pairs, key=lambda p: p[1])


def connect_all_boxes(boxes, max_connections=None):
    box_mapping = {}
    circuits = []

    for b in boxes:
        c = Circuit([b])
        box_mapping[b] = c
        circuits.append(c)

    box_pairs = combine_and_sort(boxes)

    for (a, b), _ in box_pairs[:max_connections]:
        a_circuit, b_circuit = box_mapping[a], box_mapping[b]

        if a_circuit != b_circuit:
            for box in b_circuit.boxes:
                box_mapping[box] = box_mapping[a]

            box_mapping[a].merge(b_circuit)

    return sorted(
        [c for c in circuits if len(c) > 0], key=lambda c: len(c), reverse=True
    )


def connect_until(boxes):
    box_mapping = {}
    circuits = []

    for b in boxes:
        c = Circuit([b])
        box_mapping[b] = c
        circuits.append(c)

    box_pairs = combine_and_sort(boxes)

    for (a, b), _ in box_pairs:
        a_circuit, b_circuit = box_mapping[a], box_mapping[b]

        if a_circuit != b_circuit:
            for box in b_circuit.boxes:
                box_mapping[box] = box_mapping[a]

            box_mapping[a].merge(b_circuit)

        if len(a_circuit) == len(boxes):
            return (a, b)

    return (None, None)


def product(iterable):
    total = 1

    for i in iterable:
        total *= i

    return total


def part_1(input: str, max_connections=1000):
    circuits = connect_all_boxes(parse(input), max_connections)

    return product([len(c) for c in circuits[:3]])


def part_2(input: str):
    pair = connect_until(parse(input))

    return pair[0].x * pair[1].x


if __name__ == "__main__":
    main()
