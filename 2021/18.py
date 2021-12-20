#!/usr/bin/env python

import aoc


def magnitude(pair):
    l, r = pair
    if type(l) != int:
        l = magnitude(l)
    if type(r) != int:
        r = magnitude(r)
    return 3 * l + 2 * r


def reduce(pair, depth=0):
    l, r = pair
    if depth == 3:
        pass
    return pair


def main():
    # for line in aoc.input():
    #     print(line)
    #     # TODO
    print(magnitude([[1, 2], [[3, 4], 5]]))
    print(magnitude([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]))
    print(magnitude([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]))
    print(magnitude([[[[3, 0], [5, 3]], [4, 4]], [5, 5]]))
    print(magnitude([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]))
    print(magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]))


__name__ == "__main__" and main()
