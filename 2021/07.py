#!/usr/bin/env python

import aoc
import sys

if __name__ == "__main__":
    crabs = [int(x) for x in aoc.input()[0].split(",")]
    cost1 = sys.maxsize
    cost2 = sys.maxsize
    for target in range(min(crabs), max(crabs) + 1):
        diffs = [abs(target - crab) for crab in crabs]
        cost1 = min(cost1, sum(diffs))
        sums = [n * (n + 1) / 2 for n in diffs]
        cost2 = min(cost2, sum(sums))
    print(cost1, int(cost2))
