#!/usr/bin/env python

import math


def solve(notes):
    current = int(notes[0])
    buses = [(int(s), i) for i, s in enumerate(notes[1].split(",")) if s != "x"]

    # Part 1 : find closest departure from current
    time, busid = min(
        [(math.ceil(current / bus) * bus, bus) for bus, _ in buses if bus != -1]
    )
    print("part1:", (time - current) * busid)

    # Part 2 : find timestamp when all buses depart in a consecutive manner
    cycle = t = buses[0][0]  # start with cycle being the one of the 1st bus
    # for each next bus, find when they are consecutive
    for bus, offset in buses[1:]:
        while (t + offset) % bus != 0:
            t += cycle
        cycle *= (
            bus  # new cycle is the product of cycle and the one of this new new bus
        )
    print("part2:", t)


if __name__ == "__main__":
    # example = ["939", "7,13,x,x,59,x,31,19"]
    # solve(example)
    with open("13.txt") as f:
        notes = [line.strip() for line in f]
    solve(notes)
