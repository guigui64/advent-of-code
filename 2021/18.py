#!/usr/bin/env python

import aoc
from itertools import permutations


def reduce(n):
    reduced = True
    while reduced:
        n, reduced, *_ = explode(n, 0)
        if not reduced:
            n, reduced = split(n)
    return n


def explode(n, level):
    if not isinstance(n, int):
        l, r = n
        if level >= 4:
            return 0, True, l, r
        else:
            l, reduced, expl, expr = explode(l, level + 1)
            if reduced:
                if expr != 0:
                    r = add_left(r, expr)
                    expr = 0
            else:
                r, reduced, expl, expr = explode(r, level + 1)
                if reduced:
                    if expl != 0:
                        l = add_right(l, expl)
                        expl = 0
            if reduced:
                return (l, r), True, expl, expr
    return n, False, 0, 0


def add_left(n, m):
    if isinstance(n, int):
        return n + m
    else:
        a, b = n
        return add_left(a, m), b


def add_right(n, m):
    if isinstance(n, int):
        return n + m
    else:
        a, b = n
        return a, add_right(b, m)


def split(n):
    if isinstance(n, int):
        if n >= 10:
            a = n // 2
            return (a, n - a), True
    else:
        l, r = n
        l, reduced = split(l)
        if not reduced:
            r, reduced = split(r)
        if reduced:
            return (l, r), True
    return n, False


def magnitude(n):
    if isinstance(n, int):
        return n
    l, r = n
    return 3 * magnitude(l) + 2 * magnitude(r)


def main():
    sum = None
    numbers = [eval(line) for line in aoc.input()]
    for number in numbers:
        if sum is None:
            sum = number
        else:
            sum = reduce([sum, number])
    print(magnitude(sum))
    maxmag = 0
    for (n1, n2) in permutations(numbers, 2):
        mag = magnitude(reduce([n1, n2]))
        maxmag = max(maxmag, mag)
    print(maxmag)


__name__ == "__main__" and main()
