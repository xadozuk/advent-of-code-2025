import unittest

from main import part_1, part_2

EXAMPLE = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


class Day01Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(40, part_1(EXAMPLE, 10))

    def test_part2_example(self):
        self.assertEqual(25272, part_2(EXAMPLE))
