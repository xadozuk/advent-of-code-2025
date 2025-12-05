import unittest

from main import part_1, part_2

EXAMPLE = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

EXAMPLE2 = """\
0-9
10-19
20-29
30-39
40-49
20-40
0-50

1
"""

EXAMPLE3 = """\
0-20
10-30
20-40
30-50

1
"""

EXAMPLE4 = """\
1-9
2-8
3-7

1
"""


class Day01Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(3, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(14, part_2(EXAMPLE))

    def test_part2_example2(self):
        self.assertEqual(51, part_2(EXAMPLE2))

    def test_part2_example3(self):
        self.assertEqual(51, part_2(EXAMPLE3))

    def test_part2_example4(self):
        self.assertEqual(9, part_2(EXAMPLE4))
