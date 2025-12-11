from collections import deque


class Machine:
    @staticmethod
    def from_str(input: str):
        parts = input.split(" ")
        state, rest = parts[0], parts[1:]

        initial_state = ["1" if c == "#" else "0" for c in state[1:-1]]
        initial_binary_state = int("".join(reversed(initial_state)), 2)

        buttons = []
        voltage = []

        for part in rest:
            if part[0] == "(":
                mask = sum([1 << int(v) for v in part[1:-1].split(",")])
                buttons.append(mask)

        return Machine(initial_binary_state, buttons)

    def __init__(self, state, buttons):
        self.state: int = state
        self.buttons: list[int] = buttons

    def __str__(self):
        state = format(self.state, "b")
        buttons = [format(b, "b") for b in self.buttons]
        return f"{{state={state}, buttons=[{','.join(buttons)}]}}"

    def __repr__(self):
        return str(self)

    def solve(self):
        print("-> Solve", format(self.state, "b"))
        queue = deque()
        seen = set()

        queue.append((self.state, []))

        while queue:
            (state, history) = queue.popleft()

            print(
                "*",
                format(state, "b"),
                format(state ^ history[-1], "b") if len(history) > 0 else "-",
                format(history[-1], "b") if len(history) > 0 else "-",
                history,
            )

            if state == 0:
                print("!", history)
                return history

            if state in seen:
                print("<", "Already visited")
                continue

            seen.add(state)

            for b in self.buttons:
                queue.append((state ^ b, history + [b]))

        return None


class MachineP2:
    @staticmethod
    def from_str(input: str):
        parts = input.split(" ")
        buttons_str, voltages_str = parts[1:-1], parts[-1]

        buttons = []

        for b in buttons_str:
            buttons.append([int(v) for v in b[1:-1].split(",")])

        voltage = tuple([int(v) for v in voltages_str[1:-1].split(",")])

        return MachineP2(buttons, voltage)

    def __init__(self, buttons, voltage):
        self.buttons: list[list[int]] = buttons
        self.voltage: tuple[int] = voltage

    def __str__(self):
        return f"{{voltage={self.voltage}, buttons={self.buttons}}}"

    def __repr__(self):
        return str(self)

    def is_zero(self, voltage):
        return all([v == 0 for v in voltage])

    def apply(self, voltage, button):
        new_voltage = list(voltage)

        for idx in button:
            new_voltage[idx] -= 1

        if all([v >= 0 for v in new_voltage]):
            return tuple(new_voltage)
        else:
            return None

    def solve(self):
        # print("-> Solve", self.voltage)

        queue = deque()
        cache = {}
        solutions = []
        min_steps = None

        queue.append((self.voltage, 0))

        while queue:
            (voltage, steps) = queue.pop()

            print(len(queue))
            print(voltage, steps)

            if self.is_zero(voltage):
                print("!", "Found a good config", steps)
                solutions.append(steps)
                min_steps = min(solutions)

            if (
                min_steps
                and steps >= min_steps
                or voltage in cache
                and steps >= cache[voltage]
            ):
                print("<", "Worse branch")
                continue

            cache[voltage] = steps

            for b in sorted(self.buttons, key=lambda b: len(b)):
                new_voltage = self.apply(voltage, b)
                if new_voltage:
                    print(">", voltage, b, new_voltage)
                    queue.append((new_voltage, steps + 1))

        return min(solutions)
