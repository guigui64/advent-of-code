#!/usr/bin/env python

from itertools import combinations

if __name__ == "__main__":

    with open("01.txt") as f:
        numbers = [int(x) for x in f.readlines()]
    for a, b in combinations(numbers, 2):
        if a + b == 2020:
            print(a * b)
    for a, b, c in combinations(numbers, 3):
        if a + b + c == 2020:
            print(a * b * c)
