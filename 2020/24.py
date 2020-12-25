#!/usr/bin/env python

from collections import defaultdict

directions = ["se", "sw", "nw", "ne", "e", "w"]
# https://www.redblobgames.com/grids/hexagons/#coordinates-cube
neighbors = [(0, 1, -1), (-1, 1, 0), (0, -1, 1), (1, -1, 0), (1, 0, -1), (-1, 0, 1)]

floor = defaultdict(lambda: "white")


def flip(tile):
    coords = (0, 0, 0)
    for d in directions:
        c = tile.count(d)
        tile = tile.replace(d, "")
        coords = tuple(
            coords[i] + c * neighbors[directions.index(d)][i] for i in range(3)
        )
    floor[coords] = "black" if floor[coords] == "white" else "white"


def neighbor_tiles(tile):
    x, y, z = tile
    return [(x + n[0], y + n[1], z + n[2]) for n in neighbors]


def live(floor):
    to_flip = []
    tiles = list(k for k, v in floor.items() if v == "black")
    # print(tiles)
    for tile in tiles:
        for t in [tile] + neighbor_tiles(tile):
            if t in to_flip:
                continue
            nt = neighbor_tiles(t)
            cblack = sum(floor[n] == "black" for n in nt)
            if floor[t] == "black":
                if cblack == 0 or cblack > 2:
                    to_flip.append(t)
            else:
                if cblack == 2:
                    to_flip.append(t)
    # print(to_flip)
    return to_flip


if __name__ == "__main__":
    # fname = "24ex.txt"
    fname = "24.txt"
    with open(fname) as f:
        for line in f:
            flip(line.strip())
    print("part1:", sum(tile == "black" for tile in floor.values()))
    for day in range(100):
        # print(f"\rDay {day+1:3d}", end="", flush=True)
        to_flip = live(floor)
        for tile in to_flip:
            floor[tile] = "black" if floor[tile] == "white" else "white"
        s = sum(tile == "black" for tile in floor.values())
        print(f"Day {day+1}: {s}")
    print()
    print("part2:", sum(tile == "black" for tile in floor.values()))
