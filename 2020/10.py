#!/usr/bin/env python


def solve(fname, part=1):
    numbers = list(map(int, open(fname).read().split("\n")[:-1]))
    joltage = 0
    diffs = [0] * 3
    while len(numbers) > 0:
        found = False
        for offset in range(1, 4):
            if part == 1 and found:
                break
            for i, jolt in enumerate(numbers):
                if joltage + offset == jolt:
                    joltage = jolt
                    numbers = numbers[:i] + numbers[i + 1 :]
                    diffs[offset - 1] += 1
                    found = True
                    break
    diffs[2] += 1
    return diffs[0] * diffs[2]


if __name__ == "__main__":
    # solve("10ex.txt")
    print("part1:", solve("10.txt"))
    print("part2:", solve("10.txt", 2))
