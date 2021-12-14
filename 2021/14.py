#!/usr/bin/env python

import aoc
from collections import Counter, defaultdict


def main():
    lines = aoc.input()
    polymer = lines[0]
    insertions = dict([line.split(" -> ") for line in lines[2:]])

    # we only need to count the pairs for each step, no need to build the polymer

    pc = defaultdict(int)  # pairs count
    for i in range(len(polymer) - 1):
        pc[polymer[i : i + 2]] += 1

    for step in range(40):
        npc = defaultdict(int)
        for pair, count in pc.items():
            a, b = pair
            e = insertions[pair]
            npc[a + e] += count
            npc[e + b] += count
        pc = npc

        if step == 9 or step == 39:
            c = Counter()
            for pair, count in pc.items():
                c[pair[0]] += count
            c[polymer[-1]] += 1  # last element of polymer will always stay the same
            mc = c.most_common()
            print(mc[0][1] - mc[-1][1])


__name__ == "__main__" and main()
