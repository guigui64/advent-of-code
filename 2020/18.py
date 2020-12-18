#!/usr/bin/env python

import re


parens = re.compile(r"\([^()]+\)")


def parse(line, part=1):
    compute = computeP1 if part == 1 else computeP2
    while "(" in line:
        m = parens.search(line)
        value = compute(m.group()[1:-1])
        line = line[: m.start()] + str(value) + line[m.end() :]
    return compute(line)


def computeP1(expression):
    fields = expression.split()
    value = int(fields[0])
    for field in fields[1:]:
        if field in "+*":
            operator = field
        else:
            if operator == "+":
                value += int(field)
            else:
                value *= int(field)
    return value


def computeP2(expression):
    fields = expression.split(" * ")
    value = 1
    for field in fields:
        value *= sum(int(f) for f in field.split(" + "))
    return value


if __name__ == "__main__":
    # example = "1 + (2 * 3) + (4 * (5 + 6))"
    # example = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    with open("18.txt") as f:
        lines = [line.strip() for line in f]
    print("part1:", sum(parse(line) for line in lines))
    print("part2:", sum(parse(line, 2) for line in lines))
