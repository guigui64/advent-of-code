#!/usr/bin/env python

import sys


def input() -> list[str]:
    day = sys.argv[0].split(".py")[0]
    fname = day + ".txt"
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        fname = day + "." + arg
    lines = []
    with open(fname) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]
