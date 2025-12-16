import unittest

from main import (
    part_1,
    part_2,
)

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

EXAMPLE2 = """\
2,9
2,7
8,7
8,4
2,4
2,1
11,1
11,5
13,5
13,8
11,8
11,9
"""


class Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(50, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(24, part_2(EXAMPLE))

    def test_part2_example2(self):
        self.assertEqual(40, part_2(EXAMPLE2))
