from enum import Flag, auto
from typing import override

type TileMap = list[list[bool]]


class ShapeTransform(Flag):
    Origin = auto()
    RotateLeft = auto()
    RotateHalf = auto()
    RotateRight = auto()
    VerticalFlip = auto()
    HorizontalFlip = auto()


class Shape:
    @staticmethod
    def from_str(input: str) -> Shape:
        return Shape(
            [[True if c == "#" else False for c in row] for row in input.splitlines()]
        )

    def __init__(self, tiles: TileMap):
        self.origin_tiles: TileMap = tiles

        self.compute_variations()

    def compute_variations(self):
        self.transformed: dict[ShapeTransform, TileMap] = {}

        self.transformed[ShapeTransform.RotateLeft] = self.__rotate_left(
            self.origin_tiles
        )

        self.transformed[ShapeTransform.RotateHalf] = self.__rotate_left(
            self.transformed[ShapeTransform.RotateLeft]
        )

        self.transformed[ShapeTransform.RotateRight] = self.__rotate_left(
            self.transformed[ShapeTransform.RotateHalf]
        )

        for flip in [ShapeTransform.VerticalFlip, ShapeTransform.HorizontalFlip]:
            flip_fn = (
                self.__vertical_flip
                if flip == ShapeTransform.VerticalFlip
                else self.__horizontal_flip
            )

            self.transformed[flip] = flip_fn(self.origin_tiles)

            for rotation in [
                ShapeTransform.RotateLeft,
                ShapeTransform.RotateHalf,
                ShapeTransform.RotateRight,
            ]:
                self.transformed[flip | rotation] = flip_fn(self.transformed[rotation])

    def origin(self) -> TileMap:
        return self.origin_tiles

    def get(self, transform: ShapeTransform) -> TileMap:
        if transform == ShapeTransform.Origin:
            return self.origin_tiles

        return self.transformed[transform]

    def tiles_count(self) -> int:
        return sum(map(sum, self.origin_tiles))

    def size(self) -> tuple[int, int]:
        return (len(self.origin_tiles), len(self.origin_tiles[0]))

    def all_transforms(self):
        for transform in ShapeTransform:
            yield (self.get(transform), transform)

    def __rotate_left(self, tiles: TileMap) -> TileMap:
        return [
            [tiles[i][j] for i in range(len(tiles))]
            for j in reversed(range(len(tiles[0])))
        ]

    def __vertical_flip(self, tiles: TileMap) -> TileMap:
        return [
            [tiles[i][j] for j in reversed(range(len(tiles[i])))]
            for i in range(len(tiles))
        ]

    def __horizontal_flip(self, tiles: TileMap) -> TileMap:
        return [
            [tiles[i][j] for j in range(len(tiles))]
            for i in reversed(range(len(tiles)))
        ]

    @override
    def __str__(self):
        r = ""
        # r += "  "
        # for j in range(len(self.origin_tiles[0])):
        #     r += str(j)
        #
        # r += "\n"

        for i in range(len(self.origin_tiles)):
            # r += str(i) + " "
            for j in range(len(self.origin_tiles[i])):
                r += "#" if self.origin_tiles[i][j] else "."

            r += "\n"

        return r

    @override
    def __repr__(self):
        return str(self)
