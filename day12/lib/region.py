from functools import total_ordering
import os
import time

from lib.shape import Shape, ShapeTransform

type ShapePlacement = tuple[int, tuple[int, int], ShapeTransform]


class Region:
    def __init__(self, width, length, shapes_idx):
        self.width = width
        self.length = length
        self.shapes_idx = shapes_idx

    @staticmethod
    def from_str(input: str) -> Region:
        area, shapes = input.split(": ")
        width, length = list(map(int, area.split("x")))
        shapes_idx = list(map(int, shapes.split(" ")))

        return Region(width, length, shapes_idx)

    def __str__(self):
        return str({"area": (self.width, self.length), "shapes_idx": self.shapes_idx})

    def __repr__(self) -> str:
        return str(self)

    def area(self):
        return self.width * self.length

    def can_fit(self, shapes: list[Shape]) -> bool:
        shapes_tiles_count = sum(
            [n * shapes[i].tiles_count() for i, n in enumerate(self.shapes_idx)]
        )

        if shapes_tiles_count > self.area():
            return False

        shapes_area = 0
        for i, n in enumerate(self.shapes_idx):
            length, width = shapes[i].size()
            shapes_area += (length * width) * n

        if shapes_area <= self.length * self.width:
            return True

        return False

        # Not required for the actual input =)
        shapes_to_place = []
        for i, s in enumerate(self.shapes_idx):
            shapes_to_place.extend([i] * s)

        print(self.shapes_idx, "->", shapes_to_place)

        if self.fill_region(shapes, shapes_to_place, {}, []):
            return True

        return False

    def fill_region(
        self,
        shapes: list[Shape],
        shapes_to_place: list[int],
        region_map: dict[tuple[int, int], bool],
        placements: list[ShapePlacement],
    ):
        if len(shapes_to_place) == 0:
            print("! Found solution")
            print(placements)
            self.print_region_map(region_map)
            return True

        print("=============")
        print("State:")
        self.print_region_map(region_map)
        print("")
        print("Remaining:", shapes_to_place)

        to_place, remaining = shapes_to_place[0], shapes_to_place[1:]

        shape = shapes[to_place]

        # print("Shape to place:")
        # print(shape)

        for pos in self.all_tiles():
            for transformed_shape, transform in shape.all_transforms():
                if not self.can_place_shape(pos, transformed_shape, region_map):
                    continue

                # print("Shape placed", pos)
                # print(shape)

                new_placements = placements.copy()
                new_placements.append((to_place, pos, transform))

                new_region_map = region_map.copy()

                start_i, start_j = pos
                for i, row in enumerate(transformed_shape):
                    for j, tile in enumerate(row):
                        if tile:
                            new_region_map[(start_i + i, start_j + j)] = to_place

                if self.fill_region(shapes, remaining, new_region_map, new_placements):
                    return True

        # print("<<")

        return False

    def can_place_shape(self, pos, tiles, region_map) -> bool:
        # print(pos, tiles)
        for i, row in enumerate(tiles):
            for j, tile in enumerate(row):
                # If we have an active tile (not an empty case)
                if tile:
                    t_i, t_j = pos[0] + i, pos[1] + j
                    if (
                        t_i < 0
                        or t_j < 0
                        or t_i >= self.length
                        or t_j >= self.width
                        or region_map.get((t_i, t_j), None) is not None
                    ):
                        return False

        return True

    def all_tiles(self):
        for i in range(self.length):
            for j in range(self.width):
                yield (i, j)

    def print_region_map(self, region_map):
        for i in range(self.length):
            for j in range(self.width):
                if region_map.get((i, j), None) is not None:
                    print(region_map[(i, j)], sep="", end="")
                else:
                    print(".", sep="", end="")

            print("")

        print("")
