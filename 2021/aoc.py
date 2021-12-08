#!/usr/bin/env python

import sys


def input() -> list[str]:
    day = sys.argv[0].split(".py")[0]
    fname = day + (".ex" if len(sys.argv) > 1 and sys.argv[1] == "ex" else ".txt")
    lines = []
    with open(fname) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]
