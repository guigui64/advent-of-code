#! /usr/bin/env python

import aoc
import sys
import numpy as np
from collections import Counter


def most_least(bits):
    matrix = np.array([list(bit) for bit in bits])
    counters = [Counter(matrix[:, i]) for i in range(matrix.shape[1])]
    most = "".join(["1" if counter["1"] >= counter["0"] else "0" for counter in counters])
    least = "".join(["0" if counter["0"] <= counter["1"] else "1" for counter in counters])
    return most, least


if __name__ == "__main__":
    lines = aoc.input()
    gamma, epsilon = most_least(lines)
    print(int(gamma, 2) * int(epsilon, 2))
    o2 = lines.copy()
    idx = 0
    while len(o2) > 1 and idx < len(lines[0]):
        most, _ = most_least(o2)
        o2 = [line for line in o2 if line[idx] == most[idx]]
        if len(o2) == 1:
            break
        idx += 1
    o2 = o2[0]
    co2 = lines.copy()
    idx = 0
    while len(co2) > 1 and idx < len(lines[0]):
        _, least = most_least(co2)
        co2 = [line for line in co2 if line[idx] == least[idx]]
        if len(co2) == 1:
            break
        idx += 1
    co2 = co2[0]
    print(int(o2, 2) * int(co2, 2))
