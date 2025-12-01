import unittest

from main import part_1, part_2

EXAMPLE = """\
"""


class Day01Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(None, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(None, part_2(EXAMPLE))
