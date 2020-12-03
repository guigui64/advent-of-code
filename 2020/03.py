#!/usr/bin/env python

from functools import reduce


def try_slope(slope, map):
    loc = [0, 0]
    trees = 0
    while True:
        loc = [loc[i] + slope[i] for i in [0, 1]]
        if loc[1] >= len(map):
            return trees
        loc[0] %= len(map[loc[1]])
        if map[loc[1]][loc[0]] == "#":
            trees += 1


if __name__ == "__main__":
    map = [line.strip() for line in open("03.txt").readlines()]
    print(try_slope((3, 1), map), "trees encountered")
    print(
        reduce(
            lambda x, y: x * y,
            [try_slope(s, map) for s in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]],
        )
    )
