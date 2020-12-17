#!/usr/bin/env python

from collections import defaultdict, deque


def solve(input, target):
    numbers = [int(s) for s in input.split(",")]
    indices = defaultdict(lambda: deque([], maxlen=2))
    for i, v in enumerate(numbers):
        indices[v].append(i)
    i = len(numbers)
    while i < target:
        last_spoken = numbers[-1]
        if len(indices[last_spoken]) > 1:
            spoken = indices[last_spoken][1] - indices[last_spoken][0]
        else:
            spoken = 0
        numbers += [spoken]
        indices[spoken].append(i)
        i += 1
        # print(i)
    return numbers[-1]


if __name__ == "__main__":
    input = "8,13,1,0,18,9"
    # input = "0,3,6"
    print("part1:", solve(input, 2020))
    print("part2:", solve(input, 30000000))
