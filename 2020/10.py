#!/usr/bin/env python

from collections import Counter
from itertools import groupby
from math import prod


tribonaccish = [1, 1, 1, 2, 4, 7]


def solve(fname):
    adapters = sorted([int(line) for line in open(fname)])
    sequence = [0] + adapters + [adapters[-1] + 3]
    diffs = []
    for i in range(len(sequence) - 1):
        diffs += [sequence[i + 1] - sequence[i]]
    cdiff = Counter(diffs)
    consecutive1s = [list(g) for k, g in groupby(diffs) if k == 1]
    combinations = prod(tribonaccish[len(g) + 1] for g in consecutive1s)
    print(sequence, diffs, cdiff, cdiff[3] * cdiff[1], consecutive1s, combinations)


if __name__ == "__main__":
    # solve("10ex.txt")
    solve("10.txt")
