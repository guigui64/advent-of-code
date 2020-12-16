#!/usr/bin/env python

from collections import deque


def solve(input, target):
    numbers = [int(s) for s in input.split(",")]
    indices = {v: deque([i], maxlen=2) for i, v in enumerate(numbers)}
    i = len(numbers)
    while i < target:
        # try:
        #     previous_numbers = numbers[:-1][::-1]
        #     last = len(previous_numbers) - 1 - previous_numbers.index(numbers[-1])
        #     numbers += [len(numbers) - 1 - last]
        # except ValueError:
        #     numbers += [0]
        last_spoken = numbers[-1]
        if last_spoken not in indices:
            indices[last_spoken] = [i]
            numbers += [0]
        else:
            last_index = indices[last_spoken][-1]
            if last_index == i:
                numbers += [0]
            else:
                numbers += [i - last_index]
                indices[last_spoken] += [i]
        i += 1
        print(i)
    return numbers[-1]


if __name__ == "__main__":
    # input = "8,13,1,0,18,9"
    input = "0,3,6"
    print("part1:", solve(input, 2020))
    # print("part2:", solve(input, 30000000))
