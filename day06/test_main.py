import unittest

from main import part_1, part_2

EXAMPLE = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


class Day01Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(4277556, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(3263827, part_2(EXAMPLE))
