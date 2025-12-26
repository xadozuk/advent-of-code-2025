import unittest

from lib.shape import Shape, ShapeTransform
from main import part_1, part_2

EXAMPLE = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""


class Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(2, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(None, part_2(EXAMPLE))


SIMPLE_FORM = """\
##
#.
"""

SIMPLE_FORM_RL = """\
#.
##
"""

SIMPLE_FORM_RH = """\
.#
##
"""

SIMPLE_FORM_RR = """\
##
.#
"""

SIMPLE_FORM_VF = """\
##
.#
"""

SIMPLE_FORM_HF = """\
#.
##
"""


class ShapeTest(unittest.TestCase):
    def test_shape_rotations(self):
        shape = Shape.from_str(SIMPLE_FORM)

        self.assertEqual(
            shape.get(ShapeTransform.RotateLeft),
            Shape.from_str(SIMPLE_FORM_RL).origin(),
        )

        self.assertEqual(
            shape.get(ShapeTransform.RotateHalf),
            Shape.from_str(SIMPLE_FORM_RH).origin(),
        )

        self.assertEqual(
            shape.get(ShapeTransform.RotateRight),
            Shape.from_str(SIMPLE_FORM_RR).origin(),
        )

    def test_shape_flips(self):
        shape = Shape.from_str(SIMPLE_FORM)

        self.assertEqual(
            shape.get(ShapeTransform.VerticalFlip),
            Shape.from_str(SIMPLE_FORM_VF).origin(),
        )

        self.assertEqual(
            shape.get(ShapeTransform.HorizontalFlip),
            Shape.from_str(SIMPLE_FORM_HF).origin(),
        )
