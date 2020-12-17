#!/usr/bin/env python

"""
Inspired by solution of u/jupiter126126 on reddit
"""


def solve(input, rounds):
    ind = [0] * rounds
    *first, last = input.split(",")
    for i, v in enumerate(first):
        ind[int(v)] = i + 1
    pos = len(first) + 1
    last = int(last)
    while pos <= rounds:
        if ind[last] == 0:
            spoken = 0
        else:
            spoken = pos - ind[last]
        ind[last] = pos
        last = spoken
        pos += 1
    return ind.index(rounds)


if __name__ == "__main__":
    input = "8,13,1,0,18,9"
    print("part1:", solve(input, 2020))
    print("part1:", solve(input, 30000000))
