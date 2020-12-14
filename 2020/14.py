#!/usr/bin/env python

from collections import defaultdict
import re

pat = re.compile(r"mem\[(\d+)\] = (\d+)")

if __name__ == "__main__":
    with open("14.txt") as f:
        lines = [line.strip() for line in f]
    memory = defaultdict(int)
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            address, value = pat.fullmatch(line).group(1, 2)
            value = list(f"{int(value):036b}")
            for i, x in [(i, x) for i, x in enumerate(mask) if x != "X"]:
                value[i] = x
            memory[address] = int("".join(value), 2)
    print("part1:", sum(memory.values()))
    memory = defaultdict(int)
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            address, value = pat.fullmatch(line).group(1, 2)
            value = int(value)
            address = list(f"{int(address):036b}")
            for i, x in [(i, x) for i, x in enumerate(mask) if x != "0"]:
                address[i] = x
            floatings = [i for i, x in enumerate(address) if x == "X"]

            def combine(floatings, address):
                idx = floatings[0]
                a0, a1 = [address[:idx] + [d] + address[idx + 1 :] for d in "01"]
                if len(floatings) == 1:
                    memory[int("".join(a0), 2)] = value
                    memory[int("".join(a1), 2)] = value
                else:
                    combine(floatings[1:], a0)
                    combine(floatings[1:], a1)

            combine(floatings, address)
    print("part2:", sum(memory.values()))
