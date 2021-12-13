#!/usr/bin/env python

import aoc


def main():
    dots = set()
    folds = []

    lines = aoc.input()
    sep = lines.index("")
    for line in lines[:sep]:
        x, y = map(int, line.split(","))
        dots.add((x, y))
    for line in lines[sep + 1 :]:
        axis, idx = line.split()[-1].split("=")
        folds.append((axis, int(idx)))

    def print_dots():
        H = max(y for _, y in dots) + 1
        W = max(x for x, _ in dots) + 1
        for y in range(H):
            for x in range(W):
                print("#" if (x, y) in dots else ".", end="")
            print()
        print()

    for axis, idx in folds:
        ddots = set()
        for x, y in dots:
            if axis == "y":
                if y > idx:
                    y = 2 * idx - y
            elif axis == "x":
                if x > idx:
                    x = 2 * idx - x
            ddots.add((x, y))
        dots = ddots
        print(len(dots))

    print_dots()


__name__ == "__main__" and main()
