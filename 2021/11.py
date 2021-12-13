#!/usr/bin/env python

import aoc
from itertools import product


def main():
    nrj = {}
    for y, line in enumerate(aoc.input()):
        for x, c in enumerate(line):
            nrj[(x, y)] = int(c)
    W = max(x for x, _ in nrj.keys()) + 1
    H = max(y for _, y in nrj.keys()) + 1

    def neighbors(x, y):
        directions = product((-1, 0, 1), repeat=2)
        for dx, dy in directions:
            if dx == 0 and dy == 0:
                continue
            if x + dx < 0 or y + dy < 0:
                continue
            if x + dx >= W or y + dy >= H:
                continue
            yield (x + dx, y + dy)

    # def print_nrj():
    #     for y in range(H):
    #         for x in range(W):
    #             print(nrj[(x, y)], end="")
    #         print()
    #     print()

    def inc(x, y):
        flashes = 0
        nrj[(x, y)] += 1
        if nrj[(x, y)] == 10:
            flashes += 1
            for n in neighbors(x, y):
                flashes += inc(*n)
        return flashes

    flashes = 0
    step = 0
    while True:
        # print_nrj()
        for x, y in nrj.keys():
            flashes += inc(x, y)
        for x, y in nrj.keys():
            if nrj[(x, y)] > 9:
                nrj[(x, y)] = 0
        step += 1
        if step == 100:
            print(flashes)  # part 1: number of flashes after 100 steps
        if all(v == 0 for v in nrj.values()):
            print(step)  # part 2: step when all octopuses flash
            break


__name__ == "__main__" and main()
