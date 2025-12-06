import time


def main():
    with open("day06/input.txt") as f:
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
    parsed_lines = [[x.strip() for x in line.split()] for line in input.splitlines()]

    transposed = [
        [parsed_lines[i][j] for i in range(len(parsed_lines))]
        for j in range(len(parsed_lines[0]))
    ]

    problems = [(list(map(int, parts[:-1])), parts[-1]) for parts in transposed]

    return problems


def product(iterable):
    total = 1

    for n in iterable:
        total *= n

    return total


def solution(problems):
    return sum(
        [sum(numbers) if op == "+" else product(numbers) for (numbers, op) in problems]
    )


def parse_p2(input: str):
    lines = input.splitlines()
    operators = list(reversed([op for op in lines[-1].split()]))
    numbers_grid = [list(l) for l in lines[:-1]]

    grid_height, grid_width = len(numbers_grid), len(numbers_grid[0])

    problems = []
    curr_problem = []

    for j in reversed(range(grid_width)):
        column = "".join([numbers_grid[i][j] for i in range(grid_height)])

        if column.strip() == "":
            problems.append(curr_problem)
            curr_problem = []
        else:
            curr_problem.append(column)

    problems.append(curr_problem)

    return [(list(map(int, problems[i])), operators[i]) for i in range(len(problems))]


def part_1(input: str):
    return solution(parse(input))


def part_2(input: str):
    return solution(parse_p2(input))


if __name__ == "__main__":
    main()
