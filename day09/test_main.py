import unittest

from main import part_1, part_2

EXAMPLE = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


class Day01Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(50, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(24, part_2(EXAMPLE))
