import unittest

from main import part_1, part_2

EXAMPLE = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""


class Day01Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(357, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(3121910778619, part_2(EXAMPLE))
