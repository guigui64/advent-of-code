#! /usr/bin/env python

import aoc

if __name__ == "__main__":
    # part 1
    count = 0
    previous = None
    for line in aoc.input():
        depth = int(line)
        if previous is not None:
            if depth > previous:
                count += 1
        previous = depth
    print(count)
    # part 2
    depths = [int(line) for line in aoc.input()]
    three_measurements = [sum(depths[i : i + 3]) for i in range(len(depths) - 2)]
    # print(three_measurements)
    count = 0
    previous = None
    for three in three_measurements:
        if previous is not None:
            if three > previous:
                count += 1
        previous = three
    print(count)
