#!/usr/bin/env python

from math import prod
import aoc


def find_adjacent(hmap, x, y):
    adj = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        xx = x + dx
        yy = y + dy
        if xx < 0 or yy < 0 or xx >= len(hmap[y]) or yy >= len(hmap):
            continue
        adj += [(hmap[yy][xx], xx, yy)]
    return adj


def locate_basin(hmap, h, x, y, basin):
    for a in find_adjacent(hmap, x, y):
        ah, ax, ay = a
        if a not in basin and ah != 9 and ah > h:
            basin += [a]
            basin = locate_basin(hmap, ah, ax, ay, basin)
    return basin


def main():
    hmap = [[int(c) for c in line] for line in aoc.input()]
    # find low points (values and coordinates)
    low_points = []
    for y in range(len(hmap)):
        for x in range(len(hmap[y])):
            adj = find_adjacent(hmap, x, y)
            if all([hmap[y][x] < a[0] for a in adj]):
                low_points += [(hmap[y][x], x, y)]
    # part1: risk
    print(sum([lp[0] + 1 for lp in low_points]))
    # part2: find basins from low points
    basins = []
    for h, x, y in low_points:
        basins += [locate_basin(hmap, h, x, y, [(h, x, y)])]
    print(prod(sorted([len(b) for b in basins])[::-1][:3]))


__name__ == "__main__" and main()
