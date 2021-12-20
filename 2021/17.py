#!/usr/bin/env python

import aoc
import re


def main():
    for line in aoc.input():
        xtmin, xtmax, ytmin, ytmax = map(int, re.findall(r"-?\d+", line))


__name__ == "__main__" and main()
