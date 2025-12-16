import unittest

from main import part_1, part_2

EXAMPLE = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

EXAMPLE2 = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


class Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(5, part_1(EXAMPLE))

    def test_part2_example(self):
        self.assertEqual(2, part_2(EXAMPLE2))
