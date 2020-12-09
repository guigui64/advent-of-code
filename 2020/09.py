#!/usr/bin/env python

from itertools import combinations


def solve(fname, size):
    numbers = list(map(int, open(fname).read().split("\n")[:-1]))
    for i in range(size, len(numbers)):
        sums = map(sum, combinations(numbers[i - size : i], 2))
        if numbers[i] not in sums:
            incorrect = numbers[i]
            print("first incorrect number", incorrect)
            break
    for n in range(2, len(numbers)):
        for i in range(len(numbers) - n):
            seq = numbers[i : i + n]
            if sum(seq) == incorrect:
                print("weakness", min(seq) + max(seq))
                return


if __name__ == "__main__":
    # solve("09ex.txt", 5)
    solve("09.txt", 25)
