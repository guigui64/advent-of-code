#!/usr/bin/env python

from collections import defaultdict
import aoc


def main():
    G = defaultdict(list)
    for line in aoc.input():
        a, b = line.split("-")
        G[a] += [b]
        G[b] += [a]
    # TODO traverse G


__name__ == "__main__" and main()
