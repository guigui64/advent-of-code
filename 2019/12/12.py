import os
import re
from itertools import combinations
from copy import deepcopy
from math import gcd

regexp = r"(-?\d+).*?(-?\d+).*?(-?\d+)"


def apply_gravity(moons, k):
    for (i, j) in combinations(range(len(moons)), 2):
        if moons[i][0][k] == moons[j][0][k]:
            continue
        delta = moons[j][0][k] - moons[i][0][k]
        delta = delta / abs(delta)
        moons[i][1][k] += delta
        moons[j][1][k] -= delta


def apply_velocity(moons, k):
    for i in range(len(moons)):
        moons[i][0][k] += moons[i][1][k]


def part1(moons):
    for step in range(1000):
        for k in range(3):
            apply_gravity(moons, k)
            apply_velocity(moons, k)
    energy = sum(
        [
            sum([abs(moon[0][i]) for i in range(3)])
            * sum([abs(moon[1][i]) for i in range(3)])
            for moon in moons
        ]
    )
    return int(energy)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def part2(moons):
    periods = [0, 0, 0]
    start = deepcopy(moons)
    for k in range(3):
        step = 0
        while True:
            apply_gravity(moons, k)
            apply_velocity(moons, k)
            step += 1
            same = True
            for i in range(len(moons)):
                if moons[i][0][k] != start[i][0][k] or moons[i][1][k] != start[i][1][k]:
                    same = False
                    break
            if same:
                periods[k] = step
                break
    return lcm(periods[0], lcm(*periods[1:]))


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        moons = []
        for line in input:
            m = re.search(regexp, line)
            moons.append((list(map(int, m.group(1, 2, 3))), [0, 0, 0]))
        print(f"Part1 solution : {part1(deepcopy(moons))}")
        print(f"Part2 solution : {part2(deepcopy(moons))}")
