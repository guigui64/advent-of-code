#!/usr/bin/env python

from copy import deepcopy
from itertools import product


def count_occupied(seats, x, y, part=1):
    H, W = len(seats), len(seats[0])
    count = 0
    # all directions around current seat
    directions = list(product((1, 0, -1), repeat=2))
    directions.remove((0, 0))
    for dx, dy in directions:
        xi, yi = x, y
        while True:
            xi += dx
            yi += dy
            # out of space
            if xi < 0 or xi >= W or yi < 0 or yi >= H:
                break
            # empty seat
            if seats[yi][xi] == "L":
                break
            # occupied seat
            if seats[yi][xi] == "#":
                count += 1
                break
            # stop at first belt for part 1
            if part == 1:
                break
    return count


def solve(fname, part=1):
    limit = 4 if part == 1 else 5
    seats = [list(line.strip()) for line in open(fname)]
    while True:
        # print("\n".join(["".join(s) for s in seats]))
        # print("---")
        changes = 0
        new_seats = deepcopy(seats)
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if seats[y][x] == ".":
                    continue
                occupied = count_occupied(seats, x, y, part)
                if seats[y][x] == "#" and occupied >= limit:
                    new_seats[y][x] = "L"
                    changes += 1
                elif seats[y][x] == "L" and occupied == 0:
                    new_seats[y][x] = "#"
                    changes += 1
        if changes == 0:
            return sum([s == "#" for row in seats for s in row])
        seats = new_seats


if __name__ == "__main__":
    # fname = "11ex.txt"
    fname = "11.txt"
    print("part1:", solve(fname))
    print("part2:", solve(fname, 2))
