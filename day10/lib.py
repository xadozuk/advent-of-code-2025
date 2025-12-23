from collections import deque
from z3 import *


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

        voltage = [int(v) for v in voltages_str[1:-1].split(",")]

        return MachineP2(buttons, voltage)

    def __init__(self, buttons, voltage):
        self.buttons: list[list[int]] = buttons
        self.voltage: list[int] = voltage

    def __str__(self):
        return f"{{voltage={self.voltage}, buttons={self.buttons}}}"

    def __repr__(self):
        return str(self)

    def solve(self):
        s = Optimize()

        button_vars = [Int(f"b{i}") for i in range(len(self.buttons))]
        s.add(*[b >= 0 for b in button_vars])

        for i, v in enumerate(self.voltage):
            equation = sum(
                [
                    button_vars[btn_idx]
                    for (btn_idx, btn) in enumerate(self.buttons)
                    if i in btn
                ]
            )

            s.add(simplify(equation == v))

        n_button_presses = sum(button_vars)
        s.minimize(n_button_presses)

        if s.check() == sat:
            model = s.model()
            return sum([model[btn_var].as_long() for btn_var in button_vars])
        else:
            print("No solution found")
            return -1

        # print(s)
        # print(s.check())
        # print(s.model())
