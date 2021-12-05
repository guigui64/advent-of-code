#! /usr/bin/env python

import sys
from collections import Counter


def compute_spots(lines, diag=False):
    spots = []
    for line in lines:
        (x1, y1), (x2, y2) = [(int(i), int(j)) for (i, j) in [coord.split(",") for coord in line.strip().split(" -> ")]]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                spots += [(x1, y)]
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                spots += [(x, y1)]
        elif diag:
            xstep = 1 if x1 < x2 else -1
            ystep = 1 if y1 < y2 else -1
            spots += list(zip(range(x1, x2 + xstep, xstep), range(y1, y2 + ystep, ystep)))
    return spots


if __name__ == "__main__":
    fn = sys.argv[1] if len(sys.argv) > 1 else "05.txt"
    with open(fn) as f:
        lines = f.readlines()
    for diag in [False, True]:
        spots = compute_spots(lines, diag)
        c = Counter(spots)
        # print(c)
        sum = 0
        for pair in c.items():
            if pair[1] > 1:
                sum += 1
        print(sum)
