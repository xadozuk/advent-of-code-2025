import unittest

from main import part_1, part_2

EXAMPLE = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


class Day01Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(3, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(6, part_2(EXAMPLE))

    def test_part2_big(self):
        self.assertEqual(11, part_2("R1050"))

    def test_part2_3(self):
        self.assertEqual(2, part_2("R50\nL150"))
