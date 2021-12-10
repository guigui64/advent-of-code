#!/usr/bin/env python

import aoc


def main():
    c2o = {  # closing to opening
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    o2c = {v: k for k, v in c2o.items()}  # opening to closing
    openings = c2o.values()
    # part 1: find corrupted lines
    scores1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total1 = 0
    # part 2: complete incomplete lines
    scores2 = {")": 1, "]": 2, "}": 3, ">": 4}
    totals2 = []
    for line in aoc.input():
        hist = []
        incomplete = True
        for c in line:
            if c in openings:
                hist.append(c)
            else:  # closing
                last = hist.pop()
                if o2c[last] != c:
                    total1 += scores1[c]
                    incomplete = False
                    break
        if incomplete:
            stotal = 0
            for o in hist[::-1]:
                stotal = stotal * 5 + scores2[o2c[o]]
            totals2.append(stotal)
    print(total1, sorted(totals2)[int(len(totals2) / 2)])


__name__ == "__main__" and main()
