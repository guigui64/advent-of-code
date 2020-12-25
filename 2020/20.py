#!/usr/bin/env python

from math import sqrt


def rearrangements(tile):
    re = [tile]
    # rotate +90deg, +180deg and +270deg
    for _ in range(3):
        old = re[-1]
        re += [
            [
                [old[j][i] for j in range(len(old))]
                for i in range(len(old[0]) - 1, -1, -1)
            ]
        ]
    # flip horizontally
    re += [[t[:] for t in tile[::-1]]]
    # print("flip horizontally\n" + "\n".join(re[-1]))
    # flip vertically
    re += [[t[::-1] for t in tile]]
    # print("flip vertically\n" + "\n".join(re[-1]))
    return re


def solve(fname):
    with open(fname) as f:
        blocks = f.read()[:-1].split("\n\n")
    tiles = {}
    for block in blocks:
        number = int(block.split("\n")[0].split()[1][:-1])
        content = block.split("\n")[1:]
        tiles[number] = rearrangements(content)
    square_len = int(sqrt(len(tiles)))
    print(square_len)


if __name__ == "__main__":
    solve("20ex.txt")
