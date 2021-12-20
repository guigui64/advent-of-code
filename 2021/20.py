#!/usr/bin/env python

import aoc


def bounds(lit):
    x = min(x for x, _ in lit)
    y = min(y for _, y in lit)
    X = max(x for x, _ in lit)
    Y = max(y for _, y in lit)
    return (x - 2, X + 2), (y - 2, Y + 2)


def index(lit, x, y):
    sb = ""
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if (x + dx, y + dy) in lit:
                sb += "1"
            else:
                sb += "0"
    return int(sb, base=2)


def main():
    lines = aoc.input()
    enhancement = lines[0]
    lit = set()
    for y, line in enumerate(lines[2:]):
        for x, pix in enumerate(line):
            if pix == "#":
                lit.add((x, y))
    print(index(lit, 2, 2))


__name__ == "__main__" and main()
