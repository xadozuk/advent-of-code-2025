import unittest

from main import part_1, part_2

EXAMPLE = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""


class Day01Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(1227775554, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(4174379265, part_2(EXAMPLE))
